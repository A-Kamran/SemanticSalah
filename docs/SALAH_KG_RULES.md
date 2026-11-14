# Salah KG Rule Catalog

> Sections 1.2 to 1.4 are **generated from `SemanticSalahOntology.owl`** and sections 2.2 to 2.4 from `SemanticSalahRules.owl` (the executed rules, in the final vocabulary) by `generate_catalog.py`; do not edit them by hand. Section 2.1 (posture-type rules) keeps the original catalogue names and is not part of the executed module: the knowledge-graph generator assigns the posture types directly.

Exhaustive reusable catalog of Formal rules - retained alongside a best-effort normalized view intended for documentation, review, and downstream KG-generation code.

## Inventory

- **salah unit equivalent class rules:** 3
- **complete rakah equivalent class rules:** 9 (13 accepted shapes)
- **incomplete rakah classes:** 9
- **incomplete rakah scenarios:** 124 (generated from the ontology)
- **swrl posture type rules:** 9
- **swrl missed posture rules:** 29
- **swrl missed rakah rules:** 3
- **swrl extra rakah rules:** 3

<!-- ## Applied corrections

- **TwoUnitRakah2 / Scenario 5** — Replaced duplicated Scenario 5 with Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud.
- **TwoUnitExtraRakah1** — Changed consequent from hasMissedRakah(?count, Count1) to hasExtraRakah(?count, Count1). -->

## 1. OWL-style equivalent-class rules

### 1.1 Salah unit types

#### `FourSalahUnit`
**Normalized view:** Classify a Salah unit as FourSalahUnit when its rakah count is exactly 4.
```text
equivalent_to = [hasUnitRakahCount.value(4)]
```

#### `ThreeSalahUnit`
**Normalized view:** Classify a Salah unit as ThreeSalahUnit when its rakah count is exactly 3.
```text
equivalent_to = [hasUnitRakahCount.value(3)]
```

#### `TwoSalahUnit`
**Normalized view:** Classify a Salah unit as TwoSalahUnit when its rakah count is exactly 2.
```text
equivalent_to = [hasUnitRakahCount.value(2)]
```

<!-- BEGIN GENERATED FROM ONTOLOGY -->
### 1.2 Complete rakah classes

*Generated from the ontology. A complete rakah has the posture count shown; the classes for rakahs that are followed directly by standing accept an optional short sitting (Jalsa2) at the end.*

#### `CompletedTwoUnitRakah1`
**Normalized view:** Complete-rakah class with 2 accepted shapes.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(6)
```

**Shape 2**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(7)
```

#### `CompletedTwoUnitRakah2`
**Normalized view:** Complete-rakah class with 1 accepted shape.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(7)
```

#### `CompletedThreeUnitRakah1`
**Normalized view:** Complete-rakah class with 2 accepted shapes.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(6)
```

**Shape 2**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(7)
```

#### `CompletedThreeUnitRakah2`
**Normalized view:** Complete-rakah class with 1 accepted shape.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(7)
```

#### `CompletedThreeUnitRakah3`
**Normalized view:** Complete-rakah class with 1 accepted shape.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(7)
```

#### `CompletedFourUnitRakah1`
**Normalized view:** Complete-rakah class with 2 accepted shapes.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(6)
```

**Shape 2**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(7)
```

#### `CompletedFourUnitRakah2`
**Normalized view:** Complete-rakah class with 1 accepted shape.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(7)
```

#### `CompletedFourUnitRakah3`
**Normalized view:** Complete-rakah class with 2 accepted shapes.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(6)
```

**Shape 2**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(7)
```

#### `CompletedFourUnitRakah4`
**Normalized view:** Complete-rakah class with 1 accepted shape.

**Shape 1**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4; posture count 7.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4) & hasPostureCount.value(7)
```

### 1.3 Incomplete rakah classes and all scenarios

*Generated from the ontology. Where a posture count is shown, the scenario describes a rakah that stopped early; the count prevents a complete rakah from matching it.*

#### `IncompletedTwoUnitRakah1`
**Normalized view:** Incomplete-rakah class IncompletedTwoUnitRakah1 with 9 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(5)
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 9**
**Normalized view:** Qoum → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1)
```

#### `IncompletedTwoUnitRakah2`
**Normalized view:** Incomplete-rakah class IncompletedTwoUnitRakah2 with 17 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 2; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(5)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 2; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(6)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 10**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 11**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 12**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 13**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 14**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 15**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 16**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 17**
**Normalized view:** Qoum → Jalsa; belongs to TwoSalahUnit; rakah number 2.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2)
```

#### `IncompletedThreeUnitRakah1`
**Normalized view:** Incomplete-rakah class IncompletedThreeUnitRakah1 with 9 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(5)
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 9**
**Normalized view:** Qoum → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1)
```

#### `IncompletedThreeUnitRakah2`
**Normalized view:** Incomplete-rakah class IncompletedThreeUnitRakah2 with 17 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(5)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 2; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(6)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 10**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 11**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 12**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 13**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 14**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 15**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 16**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 17**
**Normalized view:** Qoum → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2)
```

#### `IncompletedThreeUnitRakah3`
**Normalized view:** Incomplete-rakah class IncompletedThreeUnitRakah3 with 20 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(5)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(6)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 10**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 11**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 12**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 13**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 14**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 15**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 16**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 17**
**Normalized view:** Qoum → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 18**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 19**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 20**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3)
```

#### `IncompletedFourUnitRakah1`
**Normalized view:** Incomplete-rakah class IncompletedFourUnitRakah1 with 9 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1) & hasPostureCount.value(5)
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

**Scenario 9**
**Normalized view:** Qoum → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1)
```

#### `IncompletedFourUnitRakah2`
**Normalized view:** Incomplete-rakah class IncompletedFourUnitRakah2 with 17 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(5)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 2; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2) & hasPostureCount.value(6)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 10**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 11**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 12**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 13**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 14**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 15**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 16**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

**Scenario 17**
**Normalized view:** Qoum → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2)
```

#### `IncompletedFourUnitRakah3`
**Normalized view:** Incomplete-rakah class IncompletedFourUnitRakah3 with 9 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3) & hasPostureCount.value(5)
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

**Scenario 9**
**Normalized view:** Qoum → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3)
```

#### `IncompletedFourUnitRakah4`
**Normalized view:** Incomplete-rakah class IncompletedFourUnitRakah4 with 17 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 4; posture count 5.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4) & hasPostureCount.value(5)
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 4; posture count 6.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4) & hasPostureCount.value(6)
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 10**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 11**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 12**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 13**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 14**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 15**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 16**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

**Scenario 17**
**Normalized view:** Qoum → Jalsa; belongs to FourSalahUnit; rakah number 4.
```text
containsPosture.some(Qoum & followedBy.some(Jalsa)) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4)
```

### 1.4 Unit rule (not in the original catalog)

#### `IncompleteSalahUnit`
**Normalized view:** A Salah unit with fewer rakahs recorded than prescribed.

- hasUnitRakahCount 2 and hasRecordedRakahCount 1
- hasUnitRakahCount 3 and hasRecordedRakahCount 1
- hasUnitRakahCount 3 and hasRecordedRakahCount 2
- hasUnitRakahCount 4 and hasRecordedRakahCount 1
- hasUnitRakahCount 4 and hasRecordedRakahCount 2
- hasUnitRakahCount 4 and hasRecordedRakahCount 3

<!-- END GENERATED FROM ONTOLOGY -->

## 2. SWRL rules

### 2.1 Posture type rules

#### `RukuPosture`
**Normalized view:** If a posture is named Ruku, classify it as RukuType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Ruku")
```
Consequent:
```text
hasPostureType(?pos, RukuType)
```

#### `QoumPosture`
**Normalized view:** If a posture is named Qoum, classify it as QoumType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Qoum")
```
Consequent:
```text
hasPostureType(?pos, QoumType)
```

#### `SajdaPosture`
**Normalized view:** If a posture is named Sajda, classify it as SajdaType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Sajda")
```
Consequent:
```text
hasPostureType(?pos, SajdaType)
```

#### `Sajda1Posture`
**Normalized view:** If a posture is named Sajda1, classify it as SajdaType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Sajda1")
```
Consequent:
```text
hasPostureType(?pos, SajdaType)
```

#### `Sajda2Posture`
**Normalized view:** If a posture is named Sajda2, classify it as SajdaType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Sajda2")
```
Consequent:
```text
hasPostureType(?pos, SajdaType)
```

#### `JalsaPosture`
**Normalized view:** If a posture is named Jalsa, classify it as JalsaType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Jalsa")
```
Consequent:
```text
hasPostureType(?pos, JalsaType)
```

#### `Jalsa1Posture`
**Normalized view:** If a posture is named Jalsa1, classify it as JalsaType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Jalsa1")
```
Consequent:
```text
hasPostureType(?pos, JalsaType)
```

#### `TashahudPosture`
**Normalized view:** If a posture is named Tashahud, classify it as TashahudType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Tashahud")
```
Consequent:
```text
hasPostureType(?pos, TashahudType)
```

#### `QayamPosture`
**Normalized view:** If a posture is named Qayam, classify it as QayamType.
Antecedent:
```text
Rakah(?r)
Contains(?r, ?p)
hasRakahNumber(?r, ?n)
hasPostureName(?pos, "Qayam")
```
Consequent:
```text
hasPostureType(?pos, QayamType)
```

<!-- BEGIN GENERATED FROM RULES MODULE -->
*Generated from `SemanticSalahRules.owl` (the module that is executed), in the final vocabulary of the ontology.*

### 2.2 Missed posture rules

#### `TwoUnitMissedSajda2Rakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?tashahud1)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `TwoUnitMissedSajda2Rakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?qayam2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `TwoUnitMissedRukuRakah2`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `TwoUnitMissedRukuRakah1`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `TwoUnitMissedQoumRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: TwoSalahUnit; rakah number 2; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `TwoUnitMissedQoumRakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: TwoSalahUnit; rakah number 1; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
TwoSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `ThreeUnitMissedTashahudRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 2; infer missed posture TashahudType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, TashahudType)
```

#### `ThreeUnitMissedSajdaRakah3`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?tashahud1)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `ThreeUnitMissedSajdaRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?tashahud1)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `ThreeUnitMissedSajdaRakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?qayam2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `ThreeUnitMissedRukuRakah3`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `ThreeUnitMissedRukuRakah2`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `ThreeUnitMissedRukuRakah1`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `ThreeUnitMissedQoumRakah3`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 3; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `ThreeUnitMissedQoumRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: ThreeSalahUnit; rakah number 2; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `ThreeUnitMissedQoumRakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: ThreeSalahUnit; rakah number 1; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
ThreeSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `FourUnitMissedTashahudRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 2; infer missed posture TashahudType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, TashahudType)
```

#### `FourUnitMissedSajdaRakah4`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?tashahud1)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 4)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `FourUnitMissedSajdaRakah3`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?qayam2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `FourUnitMissedSajdaRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?tashahud1)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `FourUnitMissedSajdaRakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Qoum → Sajda → Jalsa → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture SajdaType.
Antecedent:
```text
followedBy(?jalsa1, ?qayam2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?ruku1, ?qoum1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, SajdaType)
```

#### `FourUnitMissedRukuRakah4`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 4)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `FourUnitMissedRukuRakah3`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `FourUnitMissedRukuRakah2`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `FourUnitMissedRukuRakah1`
**Normalized view:** Observed sequence: Qayam → Qoum → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture RukuType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?qoum1, ?sajda1)
followedBy(?qayam1, ?qoum1)
QayamPosture(?qayam1)
QoumPosture(?qoum1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, RukuType)
```

#### `FourUnitMissedQoumRakah4`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 4; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 4)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `FourUnitMissedQoumRakah3`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 3; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 3)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `FourUnitMissedQoumRakah2`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; unit type: FourSalahUnit; rakah number 2; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?tashahud1)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
TashahudPosture(?tashahud1)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 2)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

#### `FourUnitMissedQoumRakah1`
**Normalized view:** Observed sequence: Qayam → Ruku → Sajda → Jalsa → Sajda → Qayam; unit type: FourSalahUnit; rakah number 1; infer missed posture QoumType.
Antecedent:
```text
followedBy(?sajda2, ?qayam2)
followedBy(?jalsa1, ?sajda2)
followedBy(?sajda1, ?jalsa1)
followedBy(?ruku1, ?sajda1)
followedBy(?qayam1, ?ruku1)
QayamPosture(?qayam1)
RukuPosture(?ruku1)
SajdaPosture(?sajda1)
JalsaPosture(?jalsa1)
SajdaPosture(?sajda2)
QayamPosture(?qayam2)
containsPosture(?rakah, ?qayam1)
belongsToUnit(?rakah, ?su)
FourSalahUnit(?su)
hasRakahNumber(?rakah, 1)
```
Consequent:
```text
hasMissedPosture(?rakah, QoumType)
```

### 2.3 Missed rakah rules

#### `FourUnitMissedRakah2`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 3 → 4; infer missing RakahTwo.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 4)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 3)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 4)
```
Consequent:
```text
hasMissedRakah(?su, RakahTwo)
```

#### `FourUnitMissedRakah3`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 2 → 4; infer missing RakahThree.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 4)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 4)
```
Consequent:
```text
hasMissedRakah(?su, RakahThree)
```

#### `ThreeUnitMissedRakah2`
**Normalized view:** Expected 3 rakahs; observed rakah-number chain 1 → 3; infer missing RakahTwo.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 3)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 3)
```
Consequent:
```text
hasMissedRakah(?su, RakahTwo)
```

### 2.4 Extra rakah rules

#### `FourUnitExtraRakah1`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 2 → 3 → 4 → 5; infer Count1 extra rakah.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 4)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 3)
rakahFollowedByRakah(?r3, ?r4)
hasRakahNumber(?r4, 4)
rakahFollowedByRakah(?r4, ?r5)
hasRakahNumber(?r5, 5)
```
Consequent:
```text
hasExtraRakah(?su, Count1)
```

#### `ThreeUnitExtraRakah1`
**Normalized view:** Expected 3 rakahs; observed rakah-number chain 1 → 2 → 3 → 4; infer Count1 extra rakah.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 3)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 3)
rakahFollowedByRakah(?r3, ?r4)
hasRakahNumber(?r4, 4)
```
Consequent:
```text
hasExtraRakah(?su, Count1)
```

#### `TwoUnitExtraRakah1`
**Normalized view:** Expected 2 rakahs; observed rakah-number chain 1 → 2 → 3; infer Count1 extra rakah.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?su, 2)
containsRakah(?su, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 3)
```
Consequent:
```text
hasExtraRakah(?su, Count1)
```

<!-- END GENERATED FROM RULES MODULE -->

## 3. Reuse guidance

Use `salah_kg_rules.json` as the machine-readable source of truth. For each rule, `normalized_view` is documentation-oriented, while `expression`, `antecedent`, and `consequent` are the formal fields to use when generating ontology/KG artifacts.
