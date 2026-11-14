#!/usr/bin/env python3
"""Regenerate the OWL part of the rule catalog (sections 1.2 to 1.4) FROM the ontology.

The ontology is the single source of truth for the complete / incomplete definitions; the catalog is
documentation, so it must be generated, not edited by hand.

Usage:   python generate_catalog.py SemanticSalahOntology.owl SALAH_KG_RULES.md [output.md] [SemanticSalahRules.owl]
         (without an output name the catalog file is updated in place)
Needs:   rdflib
What it does: replaces everything between the markers  <!-- BEGIN GENERATED FROM ONTOLOGY -->  and
<!-- END GENERATED FROM ONTOLOGY -->  (the first time: sections 1.2 up to '## 2. SWRL rules'), and refreshes
the inventory counts. With the rules module as fourth argument it also regenerates sections 2.2 to 2.4 (the SWRL diagnosis
rules) from the module that is actually executed, in the final vocabulary. Sections 1.1 and 2.1 are left untouched.
"""
import re, sys
from rdflib import Graph, RDF, RDFS, OWL, URIRef, BNode
from rdflib.collection import Collection

NS = "http://www.semanticsalah.com/ontology/"
BEGIN, END = "<!-- BEGIN GENERATED FROM ONTOLOGY -->", "<!-- END GENERATED FROM ONTOLOGY -->"
ln = lambda x: str(x).split("/")[-1].split("#")[-1]
SIZE = {"Two": 2, "Three": 3, "Four": 4}

def load(path):
    g = Graph(); g.parse(path, format="xml"); return g

def conj(g, x):
    """members of an intersection, flattening nested intersections"""
    if isinstance(x, BNode) and (x, OWL.intersectionOf, None) in g:
        out = []
        for q in Collection(g, g.value(x, OWL.intersectionOf)): out += conj(g, q)
        return out
    return [x]

def chain(g, x):
    names, nxt = [], None
    for m in conj(g, x):
        if isinstance(m, URIRef): names.append(ln(m).replace("Posture", ""))
        elif g.value(m, OWL.onProperty) == URIRef(NS + "followedBy"): nxt = g.value(m, OWL.someValuesFrom)
    return names + (chain(g, nxt) if nxt is not None else [])

def alternatives(g, cls):
    """list of dicts: sequence, unit, rakah, count (None if the definition has no posture count)"""
    out = []
    for e in g.objects(URIRef(NS + cls), OWL.equivalentClass):
        alts = list(Collection(g, g.value(e, OWL.unionOf))) if (e, OWL.unionOf, None) in g else [e]
        for d in alts:
            r = {"sequence": None, "unit": None, "rakah": None, "count": None}
            for q in conj(g, d):
                p = ln(g.value(q, OWL.onProperty)) if g.value(q, OWL.onProperty) is not None else ""
                if p == "belongsToUnit": r["unit"] = ln(g.value(q, OWL.someValuesFrom))
                elif p == "hasRakahNumber": r["rakah"] = int(g.value(q, OWL.hasValue))
                elif p == "hasPostureCount": r["count"] = int(g.value(q, OWL.hasValue))
                elif p == "containsPosture": r["sequence"] = chain(g, g.value(q, OWL.someValuesFrom))
            out.append(r)
    return out

def dl(seq):
    s = seq[-1]
    for name in reversed(seq[:-1]): s = f"{name} & followedBy.some({s})"
    return f"containsPosture.some({s})"

def entry(label, r):
    text = " → ".join(r["sequence"]) + f"; belongs to {r['unit']}; rakah number {r['rakah']}" + (f"; posture count {r['count']}" if r["count"] is not None else "") + "."
    formal = f"{dl(r['sequence'])} & (belongsToUnit.some({r['unit']})) & hasRakahNumber.value({r['rakah']})" + (f" & hasPostureCount.value({r['count']})" if r["count"] is not None else "")
    return f"**{label}**\n**Normalized view:** {text}\n```text\n{formal}\n```\n\n"

def classes(g, prefix):
    names = [ln(c) for c in g.subjects(RDF.type, OWL.Class) if re.match(prefix + r"(Two|Three|Four)UnitRakah\d$", ln(c)) and list(g.objects(c, OWL.equivalentClass))]
    return sorted(names, key=lambda n: (SIZE[re.search(r"(Two|Three|Four)", n).group(1)], int(n[-1])))

def generate(g):
    comp, inc = classes(g, "Completed"), classes(g, "Incompleted")
    parts = ["### 1.2 Complete rakah classes\n\n*Generated from the ontology. A complete rakah has the posture count shown; the classes for rakahs that are followed directly by standing accept an optional short sitting (Jalsa2) at the end.*\n\n"]
    n_shapes = 0
    for c in comp:
        alts = alternatives(g, c); n_shapes += len(alts)
        parts.append(f"#### `{c}`\n**Normalized view:** Complete-rakah class with {len(alts)} accepted shape{'s' if len(alts) != 1 else ''}.\n\n")
        for i, r in enumerate(alts, 1): parts.append(entry(f"Shape {i}", r))
    parts.append("### 1.3 Incomplete rakah classes and all scenarios\n\n*Generated from the ontology. Where a posture count is shown, the scenario describes a rakah that stopped early; the count prevents a complete rakah from matching it.*\n\n")
    n_scen = 0
    for c in inc:
        alts = alternatives(g, c); n_scen += len(alts)
        parts.append(f"#### `{c}`\n**Normalized view:** Incomplete-rakah class {c} with {len(alts)} alternative observed sequences.\n\n")
        for i, r in enumerate(alts, 1): parts.append(entry(f"Scenario {i}", r))
    parts.append("### 1.4 Unit rule (not in the original catalog)\n\n#### `IncompleteSalahUnit`\n**Normalized view:** A Salah unit with fewer rakahs recorded than prescribed.\n\n")
    for e in g.objects(URIRef(NS + "IncompleteSalahUnit"), OWL.equivalentClass):
        for d in Collection(g, g.value(e, OWL.unionOf)):
            v = {ln(g.value(q, OWL.onProperty)): int(g.value(q, OWL.hasValue)) for q in conj(g, d)}
            parts.append(f"- hasUnitRakahCount {v['hasUnitRakahCount']} and hasRecordedRakahCount {v['hasRecordedRakahCount']}\n")
    parts.append("\n")
    return "".join(parts), len(comp), n_shapes, len(inc), n_scen

SWRL = "http://www.w3.org/2003/11/swrl#"
RBEGIN, REND = "<!-- BEGIN GENERATED FROM RULES MODULE -->", "<!-- END GENERATED FROM RULES MODULE -->"

def rules_section(path):
    """Sections 2.2 to 2.4 from the SWRL rules module (final vocabulary), in the order of the module."""
    r = Graph(); r.parse(path, format="xml")
    order = re.findall(r"<swrl:Imp>\s*<rdfs:label>([^<]+)</rdfs:label>", open(path, encoding="utf-8").read())
    def arg(x):
        if x is None: return None
        sx = str(x)
        return "?" + sx.split("#")[-1] if sx.startswith("urn:swrl#") else (ln(x) if isinstance(x, URIRef) else sx)
    def lines(imp, part):
        out = []
        for a in Collection(r, r.value(imp, URIRef(SWRL + part))):
            cp = r.value(a, URIRef(SWRL + "classPredicate")); pp = r.value(a, URIRef(SWRL + "propertyPredicate"))
            a1 = arg(r.value(a, URIRef(SWRL + "argument1"))); a2 = arg(r.value(a, URIRef(SWRL + "argument2")))
            out.append(f"{ln(cp)}({a1})" if cp is not None else f"{ln(pp)}({a1}, {a2})")
        return out
    byname = {}
    for imp in r.subjects(RDF.type, URIRef(SWRL + "Imp")): byname[str(r.value(imp, RDFS.label))] = imp
    fam = {"hasMissedPosture": [], "hasMissedRakah": [], "hasExtraRakah": []}
    for name in order:
        imp = byname[name]; head = lines(imp, "head")
        key = re.match(r"(\w+)\(", head[0]).group(1)
        com = str(r.value(imp, RDFS.comment)); m = re.match(r"Rule catalog: (.*?)(?: Correction note| Translation to the final vocabulary)", com, re.S)
        fam[key].append(f"#### `{name}`\n**Normalized view:** {m.group(1).strip()}\nAntecedent:\n```text\n" + "\n".join(lines(imp, "body")) + "\n```\nConsequent:\n```text\n" + "\n".join(head) + "\n```\n")
    titles = [("hasMissedPosture", "### 2.2 Missed posture rules"), ("hasMissedRakah", "### 2.3 Missed rakah rules"), ("hasExtraRakah", "### 2.4 Extra rakah rules")]
    body = "*Generated from `SemanticSalahRules.owl` (the module that is executed), in the final vocabulary of the ontology.*\n\n"
    return body + "\n".join(f"{t}\n\n" + "\n".join(fam[k]) for k, t in titles), {k: len(v) for k, v in fam.items()}

def main(onto_path, catalog_path, out_path=None, rules_path=None):
    g = load(onto_path); text = open(catalog_path, encoding="utf-8").read()
    block, n_comp, n_shapes, n_inc, n_scen = generate(g)
    block = BEGIN + "\n" + block + END + "\n\n"
    if BEGIN in text: text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*", lambda m: block, text, flags=re.S)
    else:
        a = text.index("### 1.2"); b = text.index("## 2. SWRL rules"); text = text[:a] + block + text[b:]
    text = re.sub(r"- \*\*complete rakah equivalent class rules:\*\* \d+( \(.*?\))?", f"- **complete rakah equivalent class rules:** {n_comp} ({n_shapes} accepted shapes)", text)
    text = re.sub(r"- \*\*incomplete rakah classes:\*\* \d+", f"- **incomplete rakah classes:** {n_inc}", text)
    text = re.sub(r"- \*\*incomplete rakah scenarios:\*\* \d+( \(.*?\))?", f"- **incomplete rakah scenarios:** {n_scen} (generated from the ontology)", text)
    if rules_path:
        rtext, counts = rules_section(rules_path)
        rblock = RBEGIN + "\n" + rtext + "\n" + REND + "\n\n"
        if RBEGIN in text: text = re.sub(re.escape(RBEGIN) + r".*?" + re.escape(REND) + r"\n*", lambda m: rblock, text, flags=re.S)
        else:
            a = text.index("### 2.2 Missed posture rules"); b = text.index("## 3. Reuse guidance"); text = text[:a] + rblock + text[b:]
        print("rules regenerated from the module:", counts)
    note = "\n> Sections 1.2 to 1.4 are **generated from `SemanticSalahOntology.owl`** and sections 2.2 to 2.4 from `SemanticSalahRules.owl` (the executed rules, in the final vocabulary) by `generate_catalog.py`; do not edit them by hand. Section 2.1 (posture-type rules) keeps the original catalogue names and is not part of the executed module: the knowledge-graph generator assigns the posture types directly.\n"
    text = re.sub(r"\n> Sections 1\.2 to 1\.4 .*?\n", "", text, count=1)
    text = text.replace("# Salah KG Rule Catalog\n", "# Salah KG Rule Catalog\n" + note, 1)
    open(out_path or catalog_path, "w", encoding="utf-8").write(text)
    print(f"{n_comp} complete classes ({n_shapes} shapes), {n_inc} incomplete classes ({n_scen} scenarios) written to {out_path or catalog_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit(__doc__)
    main(*sys.argv[1:5])
