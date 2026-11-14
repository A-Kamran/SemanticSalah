# Semantic Salah and SemanticStructuredActivity

Two ontologies, a knowledge graph and a set of SWRL rules. **SemanticStructuredActivity** is a generic ontology of structured human activities, their components, ordering, observations, agents and validation results. **Semantic Salah** extends it to the Islamic prayer: a prayer is a structured activity, a prayer has units, a unit has rakahs, a rakah has postures. OWL definitions let a reasoner recognise complete and incomplete rakahs and incomplete units, and an optional SWRL module names what was missed or added. The knowledge graph holds 42 recorded prayers.

## The two ontologies

| | SemanticStructuredActivity | Semantic Salah |
|---|---|---|
| Role | generic ontology of structured activities | domain ontology of Salah |
| Ontology IRI | `http://www.semanticstructuredactivity.com/ontology` | `http://www.semanticsalah.com` |
| Namespace | `http://www.semanticstructuredactivity.com/ontology/` (prefix `activity`) | `http://www.semanticsalah.com/ontology/` |
| Version | 1.2.0 | 1.0.0 |
| Authors (as in the headers) | Amna Binte Kamran | Amna Binte Kamran, Amna Basharat |
| File | `ontology/SemanticStructuredActivity.owl` | `ontology/SemanticSalahOntology.owl` |

**SemanticStructuredActivity** defines `StructuredActivity`, `ActivityComponent` (with `ActivitySegment`, `ActivityUnit` and `Action` below it) and `ValidationResult`. Its properties are `hasComponent` and `hasDirectComponent`, `precedes` and `directlyPrecedes`, and `hasValidationResult`, together with the data properties `hasStartTime`, `hasEndTime`, `hasSequencePosition`, `hasConfidenceValue` and `hasValidationMessage`. It reuses terms from PROV-O (`prov:Activity`, `prov:Agent`) and SOSA (`sosa:Observation`, `sosa:hasResult`). It declares `StructuredActivity` and `ActivityComponent` disjoint, and `Action`, `ActivitySegment` and `ActivityUnit` pairwise disjoint.

**How Semantic Salah extends it**

| Semantic Salah | extends |
|---|---|
| `Salah` | `activity:StructuredActivity` |
| `SalahUnit` | `activity:ActivitySegment` |
| `Rakah` | `activity:ActivityUnit` |
| `Posture` | `activity:Action` |
| `hasSalahUnit`, `containsRakah`, `containsPosture` | `activity:hasDirectComponent` |
| `followedBy` (postures), `rakahFollowedByRakah` (rakahs) | `activity:directlyPrecedes` |
| `isStartedAtTime`, `postureStartsAtTime` | `activity:hasStartTime` |
| `isCompletedAtTime`, `postureEndsAtTime` | `activity:hasEndTime` |

The Salah ontology re-declares the structured-activity terms it uses and does not import the file, so the two can be opened together or separately. Open both to see the generic classes and their disjointness axioms.

## Contents

```
ontology/   SemanticStructuredActivity.owl   the generic structured-activity ontology (version 1.2.0)
            SemanticSalahOntology.owl        the Salah ontology (classes, properties, OWL definitions)
            SemanticSalahRules.owl           35 SWRL diagnosis rules; imports the Salah ontology
            catalog-v001.xml                 lets Protégé find the ontologies when it opens the rules module
kg/         SalahKG_ABox.rdf                 the knowledge graph: 42 recorded prayers, individuals only
            SalahKG_inferred_types.rdf       the classes HermiT inferred for every individual of the graph
queries/    competency_questions.md          12 competency questions, each with a SPARQL query
            one_salah_figure.rq              SPARQL CONSTRUCT that returns one prayer as a small subgraph
tests/      SemanticSalahOntology_TestCases.owl   the Salah ontology plus 24 test cases; TESTCASES_EXPECTED.csv lists the expected results
            rules_demo/                      three self-contained files for running and checking the SWRL rules
            kg_verification/                 the Salah ontology with the graph, in one file and in seven batches, for reasoning
generator/  GRAPH_GENERATOR_v2.ipynb         builds the knowledge graph from the raw recordings and checks it
docs/       HOW_TO_VERIFY.md                 step-by-step checks in Protégé, with the expected numbers
            SALAH_KG_RULES.md                the rule catalog, generated from the Salah ontology and the rules module
            RULES_TRACEABILITY.md            where each rule lives and how it was checked
            generate_catalog.py              regenerates the rule catalog
            competency_questions_results.md  how each competency question is answered, with the results on the graph
figures/    the figures of the paper (SVG and PNG)
```

## Quick start

1. Open `ontology/SemanticStructuredActivity.owl` and `ontology/SemanticSalahOntology.owl` in Protégé. The OWL rules are the *Equivalent To* axioms of the Salah classes, for example `CompletedTwoUnitRakah2` and `IncompleteSalahUnit`.
2. To see inferences on the recorded prayers, open a file from `tests/kg_verification/` (the Salah ontology and the prayers together, no imports), start the HermiT reasoner, and compare with the expected numbers in `docs/HOW_TO_VERIFY.md`. Use HermiT: the Pellet plug-in does not work in current Protégé versions.
3. To see which posture or rakah was missed, open one of the files in `tests/rules_demo/` with HermiT. The rules module is separate because not every triple store runs SWRL.
4. `queries/competency_questions.md` has the SPARQL queries. Questions 1 to 4 use the generic `activity:` properties, so load the two ontologies with `kg/SalahKG_ABox.rdf` into a store that applies sub-property inference; load `kg/SalahKG_inferred_types.rdf` as well for questions 5 and 9 to 11. The comments in each query say what it needs.

## What the knowledge graph contains

42 Salah executions by 18 participants (anonymised), with 128 rakahs and 865 postures. They were annotated with a data-collection app. The raw recordings are not published, because their folder names are participants' names. `generator/GRAPH_GENERATOR_v2.ipynb` shows how the graph was built from them, and `generator/generator_cache.json` holds the anonymised identifiers and prescribed time windows.

## Results in brief

- Recorded graph: 126 of 128 rakahs are classified complete, none incomplete, and two match no defined pattern; 37 of 42 prayers are fully complete; 5 units have fewer rakahs than prescribed (`IncompleteSalahUnit`).
- Test file: 120 rakahs and 45 units; HermiT classified 70 rakahs as complete, 41 as incomplete and 9 as unmatched, and 3 units as `IncompleteSalahUnit`, as expected, with no inconsistency.
- Rules: all 35 SWRL rules produce the expected inference on the scenario they describe.
- The consistency checks were also run with SemanticStructuredActivity merged in, including its disjointness axioms; all were consistent.

## Limitations

- Completeness is classified at rakah and unit level; a completion status for a whole prayer is not inferred.
- OWL treats missing information as unknown, so the data carry counts (`hasPostureCount`, `hasRecordedRakahCount`) that the definitions use to recognise sequences that stopped early.
- Obligation is modelled as obligatory or non-obligatory prayers and as farz or sunnah units. Wajib, nafl, Witr, the Eid and funeral prayers and shortened prayers while travelling are not modelled.
- The SWRL rules name only some missing postures (Ruku, Qoum, the second Sajda, Tashahud), a missing rakah 2 or 3, and one extra rakah.
- SemanticStructuredActivity provides `sosa:Observation` and `ValidationResult`, but the Salah knowledge graph contains no observation or validation-result individuals; its completeness results are inferred classes, not `ValidationResult` instances.
- `Takbir` (the opening takbir) and `RY` (Raf' al-Yadayn) are recorded events and are not written as postures. `Jalsa2` is the optional short sitting before standing up.

## Licence

SemanticStructuredActivity, Semantic Salah and the rules module declare CC BY-SA 4.0 in their headers.
