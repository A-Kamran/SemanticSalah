# How to verify the artifacts (Protégé with HermiT)

Every "expected" number in this guide comes from a separate Python evaluation of the ontology's definitions, **not** from HermiT. If HermiT disagrees, one of the two is wrong: report the individual and the class.

## 0. Setup
- The consistency checks of the authors were also run with `ontology/SemanticStructuredActivity.owl` merged in, including its disjointness axioms; all were consistent. The Salah ontology does not import that file, so open or merge it yourself if you want to repeat this.
- **Use HermiT. Do not use Pellet or "Pellet (Incremental)".** In recent Protégé versions that plug-in fails in a background thread with `NoSuchMethodError ... OWLEntityCollector.setCollectDatatypes` (a mismatch with the OWL API that Protégé ships), so it looks as if it ran but it infers nothing.
- HermiT cannot read `xsd:dateTime` values with more than three fractional-second digits (error "Literal ... is malformed"). All files here use at most three.
- Protégé 5.x. Start the reasoner with *Reasoner > HermiT*, then *Start reasoner*.
- For the rule demos: *Reasoner > Configure…* and tick the inference of **object property assertions** (the label may differ between versions).
- To count or list individuals: *Window > Tabs > DL Query*, type a class expression, tick *Instances*, *Execute*.
- To read the 35 rules: open one of the demo files, then *Window > Tabs > SWRLTab* (view only).
- Large files (the test copy) need a lot of memory and time. If Protégé runs out of memory, raise its Java heap size.

## 1. The ontology (`ontology/SemanticSalahOntology.owl`)
After *Start reasoner*:
1. No "inconsistent ontology" message.
2. In the **inferred** class hierarchy, `owl:Nothing` has no subclasses (no unsatisfiable class).
3. DL Query, instances (the file contains 6 example prayers):

| Query | Expected |
|---|---|
| `CompleteRakah` | 19 |
| `InCompleteRakah` | 0 |
| `TwoSalahUnit` / `ThreeSalahUnit` / `FourSalahUnit` | 2 / 1 / 3 |
| `IncompleteSalahUnit` | 0 |
| `ObligatorySalah` | 5 |

Per individual: `tests/ONTOLOGY_EXAMPLES_EXPECTED.csv`.

## 2. The test cases (`tests/SemanticSalahOntology_TestCases.owl`)
This is the ontology plus 24 test cases (978 individuals), **without the rules**. It checks the OWL classification only. After *Start reasoner* (slow):
1. No inconsistency message, and `owl:Nothing` empty. The disjointness of `CompleteRakah` and `InCompleteRakah` means that a rakah that is both would make the whole file inconsistent, so a clean run already proves there is none.
2. DL Query, instances:

| Query | Expected |
|---|---|
| `CompleteRakah` | 70 |
| `InCompleteRakah` | 41 |
| `TwoSalahUnit` / `ThreeSalahUnit` / `FourSalahUnit` | 28 / 7 / 10 |
| `IncompleteSalahUnit` | 3 (`TC6`, `TC13`, `TC20`) |
| `ObligatorySalah` / `NonObligatorySalah` | 7 / 3 |

3. **Observed with HermiT** (the final test file reasoned in five batches of independent test cases): every batch consistent, 70 `CompleteRakah`, 41 `InCompleteRakah`, 9 rakahs in neither group, 28 / 7 / 10 `TwoSalahUnit` / `ThreeSalahUnit` / `FourSalahUnit`, 3 `IncompleteSalahUnit`; all 165 rakahs and units agree with `TESTCASES_EXPECTED.csv`.
4. Nine rakahs are in neither group on purpose, because no definition covers them: the extra rakahs (`TC3` rakah 3, `TC10` rakah 4, `TC11` rakah 4, `TC12` rakah 3, `TC17` rakah 5, `TC18` rakah 5) and three unusual ones (`TC6` rakah 1 with an extra Tashahud, `TC17` rakah 3 and `TC20` rakah 3, which end with a Tashahud although rakah 3 of a 4-rakah prayer does not).
5. Spot checks (full list of all 165 rakahs and units: `tests/TESTCASES_EXPECTED.csv`):

| Individual | Expected inferred classes |
|---|---|
| `TC1_IC_2UNIT_RAKAH1` | `IncompletedTwoUnitRakah1`, `InCompleteRakah` |
| `TC5_IC_2UNIT_RAKAH1` | `IncompletedTwoUnitRakah1`, `InCompleteRakah` (missed Sajda 1) |
| `TC6_IC_2UNIT` | `TwoSalahUnit`, `IncompleteSalahUnit` |
| `TC13_IC_3UNIT` | `ThreeSalahUnit`, `IncompleteSalahUnit` |
| `TC21_FAJR_FARZ_SUNNAH_U2_Farz_RAKAH2` | `CompletedTwoUnitRakah2`, `CompleteRakah` |
| `TC23_TARAWIH_10UNIT_U1_RAKAH1` | `CompletedTwoUnitRakah1`, `CompleteRakah` |

## 3. The rules (`ontology/SemanticSalahRules.owl`)
### Why the rules file alone shows nothing
It holds 35 SWRL rules and no individuals; a rule only acts on individuals. It also imports the core ontology by IRI, which Protégé cannot download until the ontology is published at that address. The `catalog-v001.xml` next to the file maps the IRI to the local ontology file (keep it in the `ontology/` folder next to `SemanticSalahOntology.owl`); this catalog has not been tested in Protégé. Use the self-contained demo files in `tests/rules_demo/` (ontology + rules + individuals, no imports).

### Demo files
| File | Contents | Run time (HermiT, on the authors' computer) |
|---|---|---|
| `DemoA_unit_rules` | 10 synthetic units: missing rakah 2 or 3, extra rakah, complete units | seconds |
| `DemoB_missed_posture` | the 29 catalog scenarios, test cases `TC1`, `TC2`, `TC7`, `TC14`, two real complete prayers | about a minute |
| `DemoC_extra_rakah_testcases` | test cases `TC3`, `TC10`, `TC17`, `TC18` (extra rakah) | seconds |

After *Start reasoner* (with object property assertions ticked), run these DL queries (*Instances*). Per-individual expectations: `tests/rules_demo/RULES_DEMO_EXPECTED.csv`.

| Demo | Query | Expected instances |
|---|---|---|
| A | `hasMissedRakah value RakahTwo` | 2 |
| A | `hasMissedRakah value RakahThree` | 1 |
| A | `hasExtraRakah value Count1` | 3 |
| B | `hasMissedPosture value RukuType` | 18 |
| B | `hasMissedPosture value SajdaType` | 11 |
| B | `hasMissedPosture value QoumType` | 9 |
| B | `hasMissedPosture value TashahudType` | 2 |
| C | `hasExtraRakah value Count1` | 4 (`TC3_IC_2UNIT`, `TC10_IC_3UNIT`, `TC17_IC_4UNIT`, `TC18_IC_4UNIT`) |

In Demo B the two real complete prayers (`S3_FZ_Salah_Rakah*`, `S9_FZ_Salah_Rakah*`) must have **no** `hasMissedPosture` value.

### Do the test cases verify the rules?
- **The test copy by itself: no.** It contains no rules, so reasoning on it checks only the OWL classification.
- **Demo files: yes.** They contain the rules. Together they exercise every rule on its own scenario (29 missed-posture rules in Demo B, the 6 unit-level rules in Demo A) and four of the older test cases with the rules loaded (Demo B and C).
- **The older test cases were repaired** so that the rules can act on them: rakahs that belonged to no unit (`TC3` rakah 3, `TC10` rakah 4, `TC11` rakah 4, `TC17` rakahs 3 to 5) are now contained in their unit, the unit counts are corrected, and the extra-rakah units carry the `rakahFollowedByRakah` chain that the extra-rakah rules need.

### What no rule covers
A missed Sajda 1 (cases `TC5`, `TC9`, `TC16`), a prayer that stops early (`TC13`, `TC20`) and extra postures (`TC4`, `TC12`, `TC19`) are flagged as incomplete by the OWL definitions, but no rule says *what* was missed.

## 4. The knowledge graph (`kg/`)
`kg/SalahKG_ABox.rdf` holds individuals only and declares no import, so Protégé does not try to download anything. **On its own it has no definitions, so nothing is inferred.** To see inferences, load it together with the ontology: use the files in `tests/kg_verification/`, which are self-contained (ontology + prayers, no imports, no example prayers).

| File | Contents |
|---|---|
| `SemanticSalahKG_full.owl` | all 42 prayers (slow in HermiT: on the author's computer classification took about 30 minutes, followed by the instance computation; the expected counts below were confirmed) |
| `SemanticSalahKG_batch1_S3-S8.owl` ... `batch7_S39-S44.owl` | six prayers each (about 10 to 15 seconds each in HermiT on the authors' computer) |
| `KG_EXPECTED.csv` (in `tests/kg_verification/`) | expected inferred classes for each of the 128 rakahs and 42 units |

After *Start reasoner*: no inconsistency message, `owl:Nothing` empty, and DL Query instance counts:

| Batch | Prayers | Complete rakahs | Not classified | `TwoSalahUnit` / `ThreeSalahUnit` / `FourSalahUnit` | `IncompleteSalahUnit` |
|---|---|---|---|---|---|
| 1 | S3 to S8 | 17 | 1 | 2 / 1 / 3 | 1 (S7) |
| 2 | S9 to S14 | 17 | 0 | 2 / 1 / 3 | 1 (S14) |
| 3 | S15 to S20 | 20 | 0 | 1 / 2 / 3 | 0 |
| 4 | S21 to S26 | 19 | 0 | 1 / 3 / 2 | 0 |
| 5 | S27 to S32 | 18 | 0 | 2 / 2 / 2 | 0 |
| 6 | S33 to S38 | 15 | 1 | 1 / 1 / 4 | 3 (S35, S36, S37) |
| 7 | S39 to S44 | 20 | 0 | 1 / 2 / 3 | 0 |

**Whole graph (the full file or all seven batches added up):** 126 `CompleteRakah`, 2 rakahs without a Completed/Incompleted class (`S7_FZ_Salah_Rakah3` and `S37_FZ_Salah_Rakah3`), `TwoSalahUnit` 10, `ThreeSalahUnit` 12, `FourSalahUnit` 20, `IncompleteSalahUnit` 5 (`S7`, `S14`, `S35`, `S36`, `S37`), and no `InCompleteRakah`. Examples to look at: `S3_FZ_Salah_Rakah1` ends with a short sitting (`Jalsa2`) and is `CompletedTwoUnitRakah1`; `S14_FZ_Salah` is a `FourSalahUnit` with only 2 rakahs, hence `IncompleteSalahUnit`.

## 5. Saving the inferences
- `kg/SalahKG_inferred_types.rdf` holds the class memberships (including superclasses) that HermiT inferred for all 1,077 individuals of the graph (42 prayers, 42 units, 128 rakahs, 865 postures). It declares no import; open it next to the graph and the ontology. It was computed in the seven batches, and it matches `tests/kg_verification/KG_EXPECTED.csv` for all 170 rakahs and units (126 `CompleteRakah`, 0 `InCompleteRakah`, units 10 / 12 / 20, 5 `IncompleteSalahUnit`, 42 `ObligatorySalah`).
- To save your own run from Protégé: *Reasoner > Export inferred axioms as ontology…*, **tick "Class assertions"** (and "Object property assertions" if you ran the rules), give a new ontology IRI such as `http://www.semanticsalah.com/kg-inferred`, and do it while the reasoner is still active in that window. Without "Class assertions" the file contains the hierarchy but no memberships.
- The export contains only what you tick, so check it afterwards: it should contain `rdf:type` statements such as `CompleteRakah` for individuals like `S10_FZ_Salah_Rakah1`.
