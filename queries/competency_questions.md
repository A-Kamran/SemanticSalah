# Competency questions for the Semantic Salah ontology

The given SPARQL are _examples_ that may be reinterpreted and reused for applications. They were run on the recorded knowledge graph (`SalahKG_ABox.rdf`), the inferred classes (`SalahKG_inferred_types.rdf`) and the ontology; the comments in a query say what it needs.

### Competency Question 1:
**Question:** What components constitute a structured activity?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX sa: <http://www.semanticstructuredactivity.com/ontology/>

# Needs sub-property inference (the Salah properties are sub-properties of sa:hasDirectComponent).
# Without it, use:  :S3 (:hasSalahUnit|:containsRakah|:containsPosture)+ ?component
SELECT DISTINCT ?component
WHERE {
  :S3 sa:hasDirectComponent+ ?component .
}
```

### Competency Question 2:
**Question:** Which components are direct constituents of a given activity or activity component?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX sa: <http://www.semanticstructuredactivity.com/ontology/>

SELECT ?component
WHERE {
  :S3_FZ_Salah_Rakah1 sa:hasDirectComponent ?component .
}
```

### Competency Question 3:
**Question:** Which component directly precedes or follows another component?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX sa: <http://www.semanticstructuredactivity.com/ontology/>

SELECT ?previous ?next
WHERE {
  OPTIONAL { ?previous sa:directlyPrecedes :S3_FZ_Rakah1_P2 . }
  OPTIONAL { :S3_FZ_Rakah1_P2 sa:directlyPrecedes ?next . }
}
```

### Competency Question 4:
**Question:** Which start and end times are recorded for a given activity component?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX sa: <http://www.semanticstructuredactivity.com/ontology/>

SELECT ?posture ?startTime ?endTime
WHERE {
  :S3_FZ_Salah_Rakah1 :containsPosture ?posture .
  ?posture sa:hasStartTime ?startTime .
  OPTIONAL { ?posture sa:hasEndTime ?endTime . }
}
ORDER BY ?startTime
```

### Competency Question 5:
**Question:** Is an observed Rakah or Salah unit complete and, if not, what was missed?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# Needs the inferred classes (SalahKG_inferred_types.rdf). The missed posture needs the rules module and HermiT.
SELECT ?unit ?unitStatus ?recorded ?prescribed ?rakah ?rakahStatus ?missedPosture
WHERE {
  VALUES ?unit { :S14_FZ_Salah }
  ?unit :hasRecordedRakahCount ?recorded ;
        :hasUnitRakahCount     ?prescribed ;
        :containsRakah         ?rakah .
  BIND(IF(EXISTS { ?unit a :IncompleteSalahUnit }, "incomplete", "not flagged incomplete") AS ?unitStatus)
  OPTIONAL { ?rakah a ?rakahStatus .
             FILTER(?rakahStatus IN (:CompleteRakah, :InCompleteRakah)) }
  OPTIONAL { ?rakah :hasMissedPosture ?missedPosture . }
}
```

### Competency Question 6:
**Question:** What postures constitute a Rakah, and in what order do they occur?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# The order is derived from the followedBy relation, not from the identifiers.
SELECT (COUNT(?earlier) + 1 AS ?position) ?posture ?postureType
WHERE {
  VALUES ?rakah { :S3_FZ_Salah_Rakah2 }
  ?rakah   :containsPosture ?posture .
  ?posture :hasPostureType  ?postureType .
  OPTIONAL { ?rakah :containsPosture ?earlier .
             ?earlier :followedBy+ ?posture . }
}
GROUP BY ?posture ?postureType
ORDER BY ?position
```

### Competency Question 7:
**Question:** What is the expected sequence of postures in rakah k of an n-rakah Salah unit?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# Run on the ontology file: it contains reference complete units (here a 4-rakah unit, rakah 2).
# The sequence is the one the Completed...Rakah classes define (rule catalog, section 1.2).
SELECT (COUNT(?earlier) + 1 AS ?position) ?expectedPostureType
WHERE {
  VALUES ?rakah { :FZ_4_Zuhr_C_RAKAH2 }
  ?rakah   :containsPosture ?posture .
  ?posture :hasPostureType  ?expectedPostureType .
  OPTIONAL { ?rakah :containsPosture ?earlier .
             ?earlier :followedBy+ ?posture . }
}
GROUP BY ?posture ?expectedPostureType
ORDER BY ?position
```

### Competency Question 8:
**Question:** How many Rakahs are prescribed for a given Salah unit?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT ?unit ?prescribed ?recorded
WHERE {
  VALUES ?unit { :S14_FZ_Salah }
  ?unit :hasUnitRakahCount     ?prescribed ;
        :hasRecordedRakahCount ?recorded .
}
```

### Competency Question 9:
**Question:** Is a required posture missing from an observed Rakah?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# Needs the inferred classes and, for the missed posture, the rules module with a reasoner that supports SWRL.
SELECT ?rakah ?missedPosture
WHERE {
  ?rakah a :InCompleteRakah .
  OPTIONAL { ?rakah :hasMissedPosture ?missedPosture . }
}
```

### Competency Question 10:
**Question:** Does an observed Salah unit contain a missing or additional Rakah?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# Needs the inferred classes; the named missing or extra rakah needs the rules module and HermiT.
SELECT ?unit ?finding ?detail
WHERE {
  { ?unit a :IncompleteSalahUnit ;
          :hasRecordedRakahCount ?recorded ;
          :hasUnitRakahCount     ?prescribed .
    BIND("fewer rakahs than prescribed" AS ?finding)
    BIND(CONCAT(STR(?recorded), " of ", STR(?prescribed)) AS ?detail) }
  UNION
  { ?unit :hasMissedRakah ?missed .
    BIND("missing rakah" AS ?finding)
    BIND(STR(?missed) AS ?detail) }
  UNION
  { ?unit :hasExtraRakah ?extra .
    BIND("extra rakah" AS ?finding)
    BIND(STR(?extra) AS ?detail) }
}
ORDER BY ?unit
```

### Competency Question 11:
**Question:** Does the observed posture ordering conform to the expected Rakah structure?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

# Needs the inferred classes (SalahKG_inferred_types.rdf).
SELECT ?rakah ?conformance
WHERE {
  :S7 :hasSalahUnit/:containsRakah ?rakah .
  BIND(IF(EXISTS { ?rakah a :CompleteRakah }, "conforms",
       IF(EXISTS { ?rakah a :InCompleteRakah }, "does not conform", "cannot be classified")) AS ?conformance)
}
ORDER BY ?rakah
```

### Competency Question 12:
**Question:** Which prescribed time window and which recorded start time are associated with a Salah?

**SPARQL Query:**
```
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT ?salahType ?startTime ?windowStart ?windowEnd
WHERE {
  :S3 :hasSalahType        ?salahType ;
      :isStartedAtTime     ?startTime ;
      :hasPrescribedWindow ?window .
  ?window :hasWindowStartTime ?windowStart ;
          :hasWindowEndTime   ?windowEnd .
}
```
