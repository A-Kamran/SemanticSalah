# Competency questions: how each one is answered, with the result on the recorded graph

Every query below was run on the recorded knowledge graph (`SalahKG_ABox.rdf`, 42 prayers) together with the classes inferred by HermiT (`SalahKG_inferred_types.rdf`). `:` is `http://www.semanticsalah.com/ontology/` and `sa:` is `http://www.semanticstructuredactivity.com/ontology/`.

**Requirements.** CQ1 to CQ4 use the SemanticStructuredActivity properties, so the store needs *sub-property inference* (the Salah properties such as `containsPosture` are sub-properties of `hasDirectComponent`; the time properties are sub-properties of `hasStartTime` and `hasEndTime`). CQ5, CQ10 and CQ11 need the inferred classes loaded. CQ9 and CQ10 (named missed postures and rakahs) need the rules module and a reasoner that supports SWRL (HermiT). The results marked *rule demo* come from the demo files in `tests/rules_demo/`.

## Summary

| CQ | Question | Answered by | Result on the recorded graph |
|---|---|---|---|
| CQ1 | What components constitute a structured activity? | sub-property inference + property path | 17 components of S3 (unit, rakahs, postures) |
| CQ2 | Which components are direct constituents of a given activity or activity component? | sub-property inference | 7 direct components of a rakah; the unit of a prayer |
| CQ3 | Which component directly precedes or follows another component? | sub-property inference | previous and next posture or rakah returned |
| CQ4 | Which start and end times are recorded for a given activity component? | sub-property inference | 7 postures with start and end times |
| CQ5 | Is an observed Rakah or Salah unit complete and, if not, what was missed? | reasoner (inferred classes) + SWRL rules | 5 incomplete units; 126 complete rakahs |
| CQ6 | What postures constitute a Rakah? | asserted data | 7 postures of a rakah, in order |
| CQ7 | What is the expected sequence of postures in rakah k of an n-rakah Salah unit? | class definition | definition of the complete rakah class |
| CQ8 | How many Rakahs are prescribed for a given Salah unit? | asserted data / defined classes | 2, 3, 4 rakahs: 10, 12, 20 units |
| CQ9 | Is a required posture missing from an observed Rakah? | SWRL rules (hasMissedPosture) and incomplete classes | none on the recorded graph; 40 diagnoses in the rule demo |
| CQ10 | Does an observed Salah unit contain a missing or additional Rakah? | reasoner (IncompleteSalahUnit) and SWRL rules | 5 units with fewer rakahs than prescribed |
| CQ11 | Does the observed posture ordering conform to the expected Rakah structure? | reasoner (inferred classes) | 126 conforming, 0 non-conforming, 2 unclassified |
| CQ12 | Which prescribed time window and which recorded start time are associated with a Salah? | asserted data | window and recorded start time returned |

## Queries and results

### CQ1. What components constitute a structured activity?

*Answered by:* sub-property inference + property path

```sparql
SELECT DISTINCT ?c WHERE { :S3 sa:hasDirectComponent+ ?c }
```

**Result:** 17 components of S3 (1 unit, 2 rakahs, 14 postures)

*Note:* Without sub-property inference use: :S3 (:hasSalahUnit|:containsRakah|:containsPosture)+ ?c

### CQ2. Which components are direct constituents of a given activity or activity component?

*Answered by:* sub-property inference

```sparql
SELECT ?c WHERE { :S3_FZ_Salah_Rakah1 sa:hasDirectComponent ?c }
```

**Result:** 7 direct components of rakah 1 of S3 (its postures); :S3 has 1 (its unit)

### CQ3. Which component directly precedes or follows another component?

*Answered by:* sub-property inference

```sparql
SELECT ?prev ?next WHERE { ?prev sa:directlyPrecedes :S3_FZ_Rakah1_P2 . :S3_FZ_Rakah1_P2 sa:directlyPrecedes ?next }
```

**Result:** before posture 2 of rakah 1: S3_FZ_Rakah1_P1; after it: S3_FZ_Rakah1_P3; rakah 1 is directly followed by S3_FZ_Salah_Rakah2

*Note:* SemanticStructuredActivity has no inverse property, so "follows" is the same pattern read backwards.

### CQ4. Which start and end times are recorded for a given activity component?

*Answered by:* sub-property inference

```sparql
SELECT ?p ?start ?end WHERE { :S3_FZ_Salah_Rakah1 :containsPosture ?p . ?p sa:hasStartTime ?start . OPTIONAL { ?p sa:hasEndTime ?end } } ORDER BY ?start
```

**Result:** 7 postures of rakah 1 with start times; 7 with end times

### CQ5. Is an observed Rakah or Salah unit complete and, if not, what was missed?

*Answered by:* reasoner (inferred classes) + SWRL rules

```sparql
SELECT ?u ?rec ?pres WHERE { ?u a :IncompleteSalahUnit ; :hasRecordedRakahCount ?rec ; :hasUnitRakahCount ?pres } ORDER BY ?u
```

**Result:** S14_FZ_Salah: 2 of 4 rakahs; S35_FZ_Salah: 2 of 4 rakahs; S36_FZ_Salah: 2 of 4 rakahs; S37_FZ_Salah: 3 of 4 rakahs; S7_FZ_Salah: 3 of 4 rakahs (5 incomplete units; 126 complete rakahs, 0 incomplete rakahs)

*Note:* Needs the inferred types loaded (SalahKG_inferred_types.rdf). The missed posture of an incomplete rakah comes from hasMissedPosture (see CQ9).

### CQ6. What postures constitute a Rakah?

*Answered by:* asserted data

```sparql
SELECT ?posture ?type WHERE { :S3_FZ_Salah_Rakah1 :containsPosture ?posture . ?posture :hasPostureType ?type } ORDER BY ?posture
```

**Result:** 7 postures: Qayam, Ruku, Qoum, Sajda, Jalsa, Sajda, Jalsa

### CQ7. What is the expected sequence of postures in rakah k of an n-rakah Salah unit?

*Answered by:* class definition

```sparql
# answered by the equivalent-class definition of Completed<n>UnitRakah<k>, e.g. CompletedFourUnitRakah2;
# the rule catalog (generated from the ontology, section 1.2) lists every definition
```

**Result:** rakah 2 of a 4-rakah unit: Qayam, Ruku, Qoum, Sajda, Jalsa, Sajda, Tashahud (7 postures); rakah 1 accepts an optional short sitting at the end

*Note:* A question about the design (types), not about instances; there is no instance data to query.

### CQ8. How many Rakahs are prescribed for a given Salah unit?

*Answered by:* asserted data / defined classes

```sparql
SELECT ?n (COUNT(?u) AS ?units) WHERE { ?u :hasUnitRakahCount ?n } GROUP BY ?n ORDER BY ?n
```

**Result:** 2 rakahs: 10 units, 3 rakahs: 12 units, 4 rakahs: 20 units

### CQ9. Is a required posture missing from an observed Rakah?

*Answered by:* SWRL rules (hasMissedPosture) and incomplete classes

```sparql
SELECT ?rakah ?missed WHERE { ?rakah :hasMissedPosture ?missed }
```

**Result:** on the recorded graph: 0 (no rakah misses a posture: 126 complete, 0 incomplete, 2 unclassified). On the rule demo B (HermiT): Ruku 18, Sajda 11, Qoum 9, Tashahud 2 rakahs

*Note:* Needs the rules module and a reasoner with SWRL support (HermiT). Only a missed Ruku, Qoum, second Sajda or Tashahud is named; other missing postures are flagged incomplete.

### CQ10. Does an observed Salah unit contain a missing or additional Rakah?

*Answered by:* reasoner (IncompleteSalahUnit) and SWRL rules

```sparql
SELECT ?unit ?missed ?extra WHERE { ?unit a :SalahUnit . OPTIONAL { ?unit :hasMissedRakah ?missed } OPTIONAL { ?unit :hasExtraRakah ?extra } FILTER(BOUND(?missed) || BOUND(?extra)) }
```

**Result:** recorded graph: 5 units with fewer rakahs than prescribed (IncompleteSalahUnit, see CQ5), 0 with a named missing or extra rakah. Rule demos (HermiT): missing rakah 2: 2 units, missing rakah 3: 1 unit, one extra rakah: 3 units (demo A) and 4 test cases (demo C)

*Note:* A missing last rakah is flagged by IncompleteSalahUnit but not named.

### CQ11. Does the observed posture ordering conform to the expected Rakah structure?

*Answered by:* reasoner (inferred classes)

```sparql
SELECT ?r WHERE { ?r a :Rakah . FILTER NOT EXISTS { ?r a :CompleteRakah } FILTER NOT EXISTS { ?r a :InCompleteRakah } }
```

**Result:** conforming (CompleteRakah): 126; non-conforming (InCompleteRakah): 0; cannot be classified: 2 (S7_FZ_Salah_Rakah3, S37_FZ_Salah_Rakah3)

*Note:* The NOT EXISTS query is closed-world SPARQL over the materialised inferences, not an OWL inference.

### CQ12. Which prescribed time window and which recorded start time are associated with a Salah?

*Answered by:* asserted data

```sparql
SELECT ?type ?start ?windowStart ?windowEnd WHERE { :S3 :hasSalahType ?type ; :isStartedAtTime ?start ; :hasPrescribedWindow ?w . ?w :hasWindowStartTime ?windowStart ; :hasWindowEndTime ?windowEnd }
```

**Result:** S3: Fajr, window 05:21 (PKT) to 06:48 (PKT), recorded start 2021-11-24T20:23:47

*Note:* Whether the start lies inside the window is not inferred (the window is stored as text). Computed outside the ontology, 28 of the 42 recordings started outside their window, because they are data-collection recordings, not prayers at prayer time.

## Limits to state in the paper
- CQ9 names only a missed Ruku, Qoum, second Sajda or Tashahud; other missing postures are flagged incomplete without a name.
- CQ10: a missing last rakah is flagged by `IncompleteSalahUnit` but not named.
- CQ11: a deviation that matches no known pattern is neither conforming nor non-conforming; the answer is "cannot be classified" (2 rakahs here, both ending with a Tashahud in rakah 3 of a 4-rakah prayer).
- CQ12 retrieves the window and the start time; the comparison is not inferred, and on this graph it would not be meaningful (the recordings were made for data collection, not at prayer time).
