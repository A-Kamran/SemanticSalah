# Rules traceability

Where every rule of the rule catalog (`SALAH_KG_RULES.md`) lives in the artifacts, what was changed, and how it was checked.

## 1. Summary

| Rule family (catalog) | Count | Where it lives now | Status |
|---|---|---|---|
| Salah unit classes (`TwoSalahUnit`, `ThreeSalahUnit`, `FourSalahUnit`) | 3 | `ontology/SemanticSalahOntology.owl` (OWL equivalent classes) | matches the catalog |
| Complete rakah classes (`FourUnit_Rakah1` ... `TwoUnit_Rakah2`; in the ontology `CompletedFourUnitRakah1` ...) | 9 | ontology | changed, see section 3 |
| Incomplete rakah classes (`TwoUnitRakah1` ...; in the ontology `IncompletedTwoUnitRakah1` ...) | 9 classes; the original catalog listed 78 entries (75 distinct) | ontology, 124 alternatives | reconciled, see section 3; the catalog section is now generated from the ontology |
| Posture type rules (9, raw name -> posture type) | 9 | the mapping table of the generator notebook (`POSTURE_TYPE`) | the generator assigns the types directly; not written as SWRL |
| Missed posture rules (SWRL) | 29 | `ontology/SemanticSalahRules.owl` | translated, 29 of 29 verified |
| Missed rakah rules (SWRL) | 3 | `ontology/SemanticSalahRules.owl` | translated, 3 of 3 verified |
| Extra rakah rules (SWRL) | 3 | `ontology/SemanticSalahRules.owl` | translated, 3 of 3 verified |
| Unit rule: fewer rakahs recorded than prescribed | not in the catalog | ontology, class `IncompleteSalahUnit` | added |

The **knowledge graph** (`kg/SalahKG_ABox.rdf`) contains no rules, only individuals. The **core ontology** has no SWRL rules; the diagnosis rules are in a separate optional module that imports it.

## 2. Separation of concerns
- **Core ontology**: terms and OWL definitions that decide what *complete* and *incomplete* mean. Any OWL reasoner can run them.
- **Rules module** (`SemanticSalahRules.owl`): SWRL rules that say *what* was missed or added. Optional, because not every triple store runs SWRL.
- **Generator**: the mapping from the recorded labels to the ontology terms, and the structural checks.

## 3. Changes compared with the catalog
1. **Posture count.** All 9 complete definitions and 14 of the "stopped early" incomplete alternatives also check `hasPostureCount`. Reason: OWL cannot conclude that a sequence *ended* from the absence of further postures, so a complete rakah also matched the "stopped early" patterns.
2. **Optional short sitting (`Jalsa2`).** `CompletedTwoUnitRakah1`, `CompletedThreeUnitRakah1`, `CompletedFourUnitRakah1` and `CompletedFourUnitRakah3` accept two shapes: the standard six postures, or the same six followed by a short sitting before standing up (recorded as `Jalsa2`). Confirmed by the data-collection team.
3. **Disjointness.** `CompleteRakah` and `InCompleteRakah` are disjoint.
4. **Alternatives added to the incomplete classes (12).** Nine "missed Sajda 1" alternatives (a Qoum directly followed by a Jalsa), one per class, and three extra-posture alternatives for rakah 3 of a 3-rakah unit (Sajda-Jalsa-Sajda repeated, without a final Tashahud) that the catalog listed but the ontology did not.
5. **Incomplete scenarios: catalog versus ontology.** The original ontology had 112 alternatives and the original catalog 78 entries (75 distinct; three were listed twice). 71 are common. The 41 that only the ontology had are, for the rakahs that end with a Tashahud (rakah 2 of every unit, rakah 3 of a 3-rakah unit, rakah 4 of a 4-rakah unit), the missed or extra posture patterns in both versions, with and without the final Tashahud; the catalog often listed only one. The catalog scenario "Qayam, Ruku, Qoum, Sajda, Jalsa, Sajda, Tashahud" under `TwoUnitRakah2` is the *complete* sequence of rakah 2, so it is deliberately not in the ontology. **Resolution:** the ontology is authoritative; the catalog sections for the complete rakahs, the incomplete rakahs and the unit rule are generated from it (see section 7).
6. **Diagnosis rules.** Variables were renamed for clarity (the `?unit` of a rakah is `?rakah`; the count variable of a unit is `?su`), `Contains` is `containsPosture`, `consistsOfRakah` is `containsRakah`, and posture classes are the defined classes `QayamPosture` ... `TashahudPosture`. In the missed-rakah and extra-rakah rules the catalog used one variable for two things; it is now the unit `?su`. The individuals `RakahTwo`, `RakahThree` and `Count1` (outputs of the rules) are not in the core ontology and are declared in the rules module.

## 4. How the rules were checked (reasoner: HermiT via owlready2)
- **Each rule on its own catalog scenario.** For each of the 29 missed-posture rules a minimal rakah with exactly the observed sequence from the catalog was generated; all 29 rules inferred the expected posture and no other rule fired. For the 6 unit-level rules a unit with the observed rakah-number chain was generated (missing rakah 2 or 3, extra rakah in 2-, 3- and 4-rakah units); all 6 fired, and normal units produced nothing.
- **Test cases.** On `TC1` (missed Ruku), `TC2` (missed Sajda 2), `TC7` (3-rakah, missed Ruku in every rakah) and `TC14` (4-rakah, missed Ruku) the rules inferred the expected diagnosis in every rakah. On two real complete prayers (S3, S9) no diagnosis was inferred. On the extra-rakah cases `TC3`, `TC10`, `TC17` and `TC18` the rules inferred one extra rakah each.
- **Demo files.** `demo/` holds three self-contained files that reproduce these checks (Demo A: 10 of 10 units as expected; Demo B: 46 of 46 rakahs; Demo C: 4 of 4 units); `demo/RULES_DEMO_EXPECTED.csv` lists the expected value per individual and `../HOW_TO_VERIFY.md` explains how to check them in Protégé.
- **Test-case repair.** The older extra-rakah test cases had rakahs that belonged to no unit (`TC3` rakah 3, `TC10` rakah 4, `TC11` rakah 4, `TC17` rakahs 3 to 5) and no `rakahFollowedByRakah` links, so the unit-level rules could never fire on them. The rakahs are now contained in their units, the unit counts are corrected and the extra-rakah units carry the ordering chain.
- **Not done:** a reasoner run over the whole knowledge graph; the remaining test cases were not run with the rules.

## 5. What no rule diagnoses (gaps in the catalog)
- A **missed Sajda 1**: the ontology flags the rakah as incomplete, but there is no rule saying which posture was missed.
- A prayer that **stops early** (for example 3 of 4 rakahs, or the last rakah missing): `IncompleteSalahUnit` flags it, but there is no "which rakah" diagnosis; the missed-rakah rules only cover a missing rakah 2 or 3.
- **Extra postures** (for example an extra Jalsa and Sajda): flagged as incomplete, no diagnosis.

## 6. The 35 diagnosis rules
### Missed posture (29): infers `hasMissedPosture` on the rakah

| Rule | What it recognises | Note |
|---|---|---|
| `TwoUnitMissedSajda2Rakah2` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture SajdaType. |  |
| `TwoUnitMissedSajda2Rakah1` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture SajdaType. |  |
| `TwoUnitMissedRukuRakah2` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture RukuType. |  |
| `TwoUnitMissedRukuRakah1` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture RukuType. |  |
| `TwoUnitMissedQoumRakah2` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture QoumType. |  |
| `TwoUnitMissedQoumRakah1` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture QoumType. |  |
| `ThreeUnitMissedTashahudRakah2` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 2; infer missed posture TashahudType. |  |
| `ThreeUnitMissedSajdaRakah3` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture SajdaType. |  |
| `ThreeUnitMissedSajdaRakah2` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture SajdaType. |  |
| `ThreeUnitMissedSajdaRakah1` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture SajdaType. |  |
| `ThreeUnitMissedRukuRakah3` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture RukuType. |  |
| `ThreeUnitMissedRukuRakah2` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture RukuType. |  |
| `ThreeUnitMissedRukuRakah1` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture RukuType. |  |
| `ThreeUnitMissedQoumRakah3` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture QoumType. |  |
| `ThreeUnitMissedQoumRakah2` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture QoumType. |  |
| `ThreeUnitMissedQoumRakah1` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture QoumType. |  |
| `FourUnitMissedTashahudRakah2` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 2; infer missed posture TashahudType. |  |
| `FourUnitMissedSajdaRakah4` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture SajdaType. |  |
| `FourUnitMissedSajdaRakah3` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture SajdaType. |  |
| `FourUnitMissedSajdaRakah2` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture SajdaType. |  |
| `FourUnitMissedSajdaRakah1` | Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture SajdaType. |  |
| `FourUnitMissedRukuRakah4` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture RukuType. |  |
| `FourUnitMissedRukuRakah3` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture RukuType. |  |
| `FourUnitMissedRukuRakah2` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture RukuType. |  |
| `FourUnitMissedRukuRakah1` | Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture RukuType. |  |
| `FourUnitMissedQoumRakah4` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture QoumType. |  |
| `FourUnitMissedQoumRakah3` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture QoumType. |  |
| `FourUnitMissedQoumRakah2` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture QoumType. |  |
| `FourUnitMissedQoumRakah1` | Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture QoumType. |  |

### Missed rakah (3): infers `hasMissedRakah` on the unit

| Rule | What it recognises | Note |
|---|---|---|
| `FourUnitMissedRakah2` | Expected 4 rakahs; observed rakah-number chain 1 → 3 → 4; infer missing RakahTwo. |  |
| `FourUnitMissedRakah3` | Expected 4 rakahs; observed rakah-number chain 1 → 2 → 4; infer missing RakahThree. |  |
| `ThreeUnitMissedRakah2` | Expected 3 rakahs; observed rakah-number chain 1 → 3; infer missing RakahTwo. |  |

### Extra rakah (3): infers `hasExtraRakah` on the unit

| Rule | What it recognises | Note |
|---|---|---|
| `FourUnitExtraRakah1` | Expected 4 rakahs; observed rakah-number chain 1 → 2 → 3 → 4 → 5; infer Count1 extra rakah. |  |
| `ThreeUnitExtraRakah1` | Expected 3 rakahs; observed rakah-number chain 1 → 2 → 3 → 4; infer Count1 extra rakah. |  |
| `TwoUnitExtraRakah1` | Expected 2 rakahs; observed rakah-number chain 1 → 2 → 3; infer Count1 extra rakah. | Catalog correction: Corrected from hasMissedRakah(?count, Count1) because this rule belongs to Extra Rakah and detects a third rakah in a two-rakah Salah unit. |

## 7. Keeping the catalog in sync
`generate_catalog.py` regenerates sections 1.2 to 1.4 of the catalog (complete rakahs, incomplete rakahs, unit rule) and the inventory counts from the ontology, and, when the rules module is given as a fourth argument, sections 2.2 to 2.4 (the 35 diagnosis rules, in the final vocabulary) from the module that is actually executed:

```
python generate_catalog.py ../ontology/SemanticSalahOntology.owl SALAH_KG_RULES.md SALAH_KG_RULES.md ../ontology/SemanticSalahRules.owl
```
It needs `rdflib`, only touches the text between the `BEGIN` and `END GENERATED FROM ONTOLOGY` markers, and gives the same result when run twice. Run it whenever the ontology's definitions change. Section 1.1 (unit classes) and section 2.1 (the nine posture-type rules, which keep the original catalogue names and are not part of the executed module) are not generated.
