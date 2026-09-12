# Salah KG Rule Catalog

Exhaustive reusable catalog extracted from the supplied LaTeX. Formal rules are retained alongside a best-effort normalized view intended for documentation, review, and downstream KG-generation code.

## Inventory

- **salah unit equivalent class rules:** 3
- **complete rakah equivalent class rules:** 9
- **incomplete rakah classes:** 9
- **incomplete rakah scenarios:** 78
- **swrl posture type rules:** 9
- **swrl missed posture rules:** 29
- **swrl missed rakah rules:** 3
- **swrl extra rakah rules:** 3

## Applied corrections

- **TwoUnitRakah2 / Scenario 5** — Replaced duplicated Scenario 5 with Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud.
- **TwoUnitExtraRakah1** — Changed consequent from hasMissedRakah(?count, Count1) to hasExtraRakah(?count, Count1).

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

### 1.2 Complete rakah classes

#### `FourUnit_Rakah1`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
equivalent_to = [Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit) & hasRakahNumber.value(1))]
```

#### `FourUnit_Rakah2`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))]
```

#### `FourUnit_Rakah3`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))]
```

#### `FourUnit_Rakah4`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))]
```

#### `ThreeUnit_Rakah1`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))]
```

#### `ThreeUnit_Rakah2`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))]
```

#### `ThreeUnit_Rakah3`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 3.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))]
```

#### `TwoUnit_Rakah1`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))]
```

#### `TwoUnit_Rakah2`
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
equivalent_to = [Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))]
```

### 1.3 Incomplete rakah classes and all scenarios

#### `TwoUnitRakah1`
**Normalized view:** Incomplete-rakah class TwoUnitRakah1 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to TwoSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(1))
```

#### `TwoUnitRakah2`
**Normalized view:** Incomplete-rakah class TwoUnitRakah2 with 9 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 3**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
**Correction note:** Corrected from a duplicate of Scenario 4. The replacement follows the structurally consistent second-rakah pattern with both Sajdas and Tashahud.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 9**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to TwoSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(TwoSalahUnit)) & hasRakahNumber.value(2))
```

#### `ThreeUnitRakah1`
**Normalized view:** Incomplete-rakah class ThreeUnitRakah1 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(1))
```

#### `ThreeUnitRakah2`
**Normalized view:** Incomplete-rakah class ThreeUnitRakah2 with 11 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 10**
**Normalized view:** Qayam → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 11**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to ThreeSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(2))
```

#### `ThreeUnitRakah3`
**Normalized view:** Incomplete-rakah class ThreeUnitRakah3 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to ThreeSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(ThreeSalahUnit)) & hasRakahNumber.value(3))
```

#### `FourUnitRakah1`
**Normalized view:** Incomplete-rakah class FourUnitRakah1 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 1.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(1))
```

#### `FourUnitRakah2`
**Normalized view:** Incomplete-rakah class FourUnitRakah2 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 4**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 5**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 2.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(2))
```

#### `FourUnitRakah3`
**Normalized view:** Incomplete-rakah class FourUnitRakah3 with 8 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa)))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 3**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda; belongs to FourSalahUnit; rakah number 3.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(3))
```

#### `FourUnitRakah4`
**Normalized view:** Incomplete-rakah class FourUnitRakah4 with 10 alternative observed sequences.

**Scenario 1**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 2**
**Normalized view:** Qayam → Qoum → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 3**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & (followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 4**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum &followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 5**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 6**
**Normalized view:** Qayam → Ruku → Qoum → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Qoum & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 7**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Tashahud))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 8**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 9**
**Normalized view:** Qayam → Ruku → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Ruku & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud)))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

**Scenario 10**
**Normalized view:** Qayam → Sajda → Jalsa → Sajda → Jalsa → Sajda → Tashahud; belongs to FourSalahUnit; rakah number 4.
```text
Contains.some(Qayam & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Jalsa & followedBy.some(Sajda & followedBy.some(Tashahud))))))) & (belongsToUnit.some(FourSalahUnit)) & hasRakahNumber.value(4))
```

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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?twounit)
TwoSalahUnit(?twounit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, TashahudType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?threeunit)
ThreeSalahUnit(?threeunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, TashahudType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 4)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, SajdaType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 4)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Qoum(?qoum1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, RukuType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 4)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 3)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Tashahud(?tashahud1)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 2)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
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
Qayam(?qayam1)
Ruku(?ruku1)
Sajda(?sajda1)
Jalsa(?jalsa1)
Sajda(?sajda2)
Qayam(?qayam2)
Contains(?unit, ?qayam1)
belongsToUnit(?unit, ?fourunit)
FourSalahUnit(?fourunit)
hasRakahNumber(?unit, 1)
```
Consequent:
```text
hasMissedPosture(?unit, QoumType)
```

### 2.3 Missed rakah rules

#### `FourUnitMissedRakah2`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 3 → 4; infer missing RakahTwo.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 4)
consistsOfRakah(?count, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 3)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 4)
```
Consequent:
```text
hasMissedRakah(?count, RakahTwo)
```

#### `FourUnitMissedRakah3`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 2 → 4; infer missing RakahThree.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 4)
consistsOfRakah(?count, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 4)
```
Consequent:
```text
hasMissedRakah(?count, RakahThree)
```

#### `ThreeUnitMissedRakah2`
**Normalized view:** Expected 3 rakahs; observed rakah-number chain 1 → 3; infer missing RakahTwo.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 3)
consistsOfRakah(?count, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 3)
```
Consequent:
```text
hasMissedRakah(?count, RakahTwo)
```

### 2.4 Extra rakah rules

#### `FourUnitExtraRakah1`
**Normalized view:** Expected 4 rakahs; observed rakah-number chain 1 → 2 → 3 → 4 → 5; infer Count1 extra rakah.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 4)
consistsOfRakah(?count, ?r1)
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
hasExtraRakah(?count, Count1)
```

#### `ThreeUnitExtraRakah1`
**Normalized view:** Expected 3 rakahs; observed rakah-number chain 1 → 2 → 3 → 4; infer Count1 extra rakah.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 3)
consistsOfRakah(?count, ?r1)
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
hasExtraRakah(?count, Count1)
```

#### `TwoUnitExtraRakah1`
**Normalized view:** Expected 2 rakahs; observed rakah-number chain 1 → 2 → 3; infer Count1 extra rakah.
**Correction note:** Corrected from hasMissedRakah(?count, Count1) because this rule belongs to Extra Rakah and detects a third rakah in a two-rakah Salah unit.
Antecedent:
```text
SalahUnit(?su)
hasUnitRakahCount(?count, 2)
consistsOfRakah(?count, ?r1)
hasRakahNumber(?r1, 1)
rakahFollowedByRakah(?r1, ?r2)
hasRakahNumber(?r2, 2)
rakahFollowedByRakah(?r2, ?r3)
hasRakahNumber(?r3, 3)
```
Consequent:
```text
hasExtraRakah(?count, Count1)
```

## 3. Reuse guidance

Use `salah_kg_rules.json` as the machine-readable source of truth. For each rule, `normalized_view` is documentation-oriented, while `expression`, `antecedent`, and `consequent` are the formal fields to use when generating ontology/KG artifacts.