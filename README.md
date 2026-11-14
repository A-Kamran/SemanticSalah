# Semantic Salah

An ontology of Salah (the Islamic prayer) and a knowledge graph of recorded prayers. A prayer is modelled as a structured activity: a prayer has units, a unit has rakahs, a rakah has postures. OWL definitions let a reasoner recognise complete and incomplete rakahs and incomplete units, and an optional SWRL module names what was missed or added.

Version 1.0.0 · ontology IRI `http://www.semanticsalah.com` · namespace `http://www.semanticsalah.com/ontology/`
Authors (as in the ontology header): Amna Binte Kamran, Amna Basharat.
The Salah ontology extends the SemanticStructuredActivity ontology (version 1.2.0), a generic ontology of structured activities; it is included in `ontology/`. The Salah ontology re-declares the structured-activity terms it uses and does not import the file, so the two can be opened together or separately.

## Contents

```
ontology/   SemanticSalahOntology.owl        the Salah ontology (classes, properties, OWL definitions)
            SemanticStructuredActivity.owl   the generic structured-activity ontology that it extends (version 1.2.0)
            SemanticSalahRules.owl           35 SWRL diagnosis rules; imports the ontology
            catalog-v001.xml                 lets Protégé find the ontologies when it opens the rules module
kg/         SalahKG_ABox.rdf                 the knowledge graph: 42 recorded prayers, individuals only
            SalahKG_inferred_types.rdf       the classes HermiT inferred for every individual of the graph
queries/    competency_questions.md          12 competency questions, each with a SPARQL query
            one_salah_figure.rq              SPARQL CONSTRUCT that returns one prayer as a small subgraph
tests/      SemanticSalahOntology_TestCases.owl   the ontology plus 24 test cases; TESTCASES_EXPECTED.csv lists the expected results
            rules_demo/                      three self-contained files for running and checking the SWRL rules
            kg_verification/                 the ontology with the graph, in one file and in seven batches, for reasoning
generator/  GRAPH_GENERATOR_v2.ipynb         builds the knowledge graph from the raw recordings and checks it
docs/       HOW_TO_VERIFY.md                 step-by-step checks in Protégé, with the expected numbers
            SALAH_KG_RULES.md                the rule catalog, generated from the ontology and the rules module
            RULES_TRACEABILITY.md            where each rule lives and how it was checked
            generate_catalog.py              regenerates the rule catalog
            competency_questions_results.md  how each competency question is answered, with the results on the graph
figures/    the figures of the paper (SVG and PNG)
```

## Quick start

1. Open `ontology/SemanticSalahOntology.owl` in Protégé (open `ontology/SemanticStructuredActivity.owl` as well to see the generic classes it extends, including their disjointness axioms). The OWL rules are the *Equivalent To* axioms of the classes, for example `CompletedTwoUnitRakah2` and `IncompleteSalahUnit`.
2. To see inferences on the recorded prayers, open a file from `tests/kg_verification/` (ontology and prayers together, no imports), start the HermiT reasoner, and compare with the expected numbers in `docs/HOW_TO_VERIFY.md`. Use HermiT: the Pellet plug-in does not work in current Protégé versions.
3. To see which posture or rakah was missed, open one of the files in `tests/rules_demo/` with HermiT. The rules module is separate because not every triple store runs SWRL.
4. `queries/competency_questions.md` has the SPARQL queries. Load `kg/SalahKG_ABox.rdf` and `kg/SalahKG_inferred_types.rdf` into a triple store; the comments in each query say what it needs.

## What the knowledge graph contains

42 Salah executions by 18 participants (anonymised), with 128 rakahs and 865 postures. They were annotated with a data-collection app. The raw recordings are not published, because their folder names are participants' names. `generator/GRAPH_GENERATOR_v2.ipynb` shows how the graph was built from them, and `generator/generator_cache.json` holds the anonymised identifiers and prescribed time windows.

## Results in brief

- Recorded graph: 126 of 128 rakahs are classified complete, none incomplete, and two match no defined pattern; 37 of 42 prayers are fully complete; 5 units have fewer rakahs than prescribed (`IncompleteSalahUnit`).
- Test file: 120 rakahs and 45 units; HermiT classified 70 rakahs as complete, 41 as incomplete and 9 as unmatched, and 3 units as `IncompleteSalahUnit`, as expected, with no inconsistency.
- Rules: all 35 SWRL rules produce the expected inference on the scenario they describe.

## Limitations

- Completeness is classified at rakah and unit level; a completion status for a whole prayer is not inferred.
- OWL treats missing information as unknown, so the data carry counts (`hasPostureCount`, `hasRecordedRakahCount`) that the definitions use to recognise sequences that stopped early.
- Obligation is modelled as obligatory or non-obligatory prayers and as farz or sunnah units. Wajib, nafl, Witr, the Eid and funeral prayers and shortened prayers while travelling are not modelled.
- The SWRL rules name only some missing postures (Ruku, Qoum, the second Sajda, Tashahud), a missing rakah 2 or 3, and one extra rakah.
- `Takbir` (the opening takbir) and `RY` (Raf' al-Yadayn) are recorded events and are not written as postures. `Jalsa2` is the optional short sitting before standing up.

## Licence

The two ontologies and the rules module declare CC BY-SA 4.0 in their headers.
