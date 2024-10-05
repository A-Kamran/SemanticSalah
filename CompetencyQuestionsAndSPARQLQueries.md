# Competency questions for the Semantic Salah ontology

The given SPARQL are _examples_ that may be reinterpreted and reused for applications.

### Competency Question 1:
**Question:** What are the essential postures in Salah?

**SPARQL Query:**
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT DISTINCT ?posture ?label
WHERE {
  ?posture rdfs:subClassOf :Postures.
  ?posture rdfs:label ?label.  
  FILTER (lang(?label) = 'en')

}
```

### Competency Question 2:
**Question:** How many rakahs are in a specific prayer?

**SPARQL Query:**
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT (COUNT(?rakah) AS ?rakahCount)
WHERE {
  :S1_Maghrib :hasSalahUnit ?unit.
  ?unit :hasSalahUnitType ?unitType.
  ?unit :containsRakah ?rakah.

}
```
### Competency Question 3:
**Question:** Which postures precede or follow each other in Salah?

**SPARQL Query:**
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT distinct ?posture ?posture2
WHERE {
  ?posture1 a :Posture;
    :hasPostureType ?posture;
    :followedBy ?NextPosture.
  ?NextPosture :hasPostureType ?posture2.  
    
   
}
```
### Competency Question 4:
**Question:** What is the correct sequence of Salah postures?

**SPARQL Query:**
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT ?rakahUnit  ?postureName
WHERE {
  :FZ_2_Fajar_C :containsRakah  ?rakahUnit.
  ?rakahUnit rdf:type :Rakah .  
  ?rakahUnit :containsPosture ?posture . 
  ?posture :hasPostureType ?postureName .  
}
ORDER BY ?rakahUnit  

```
### Competency Question 5:
**Question:** Which postures are performed multiple times in a single rakah?

**SPARQL Query:**
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>

SELECT ?rakahUnit ?postureName (COUNT(?posture) AS ?postureCount)
WHERE {
  :FZ_2_Fajar_C :containsRakah  ?rakahUnit.
  ?rakahUnit rdf:type :Rakah .  # Retrieves all Rakah units
  ?rakahUnit :containsPosture ?posture .  # Relates each Rakah to its postures
  ?posture :hasPostureType ?postureName .  # Retrieves the posture type
}
GROUP BY ?rakahUnit ?postureName  # Groups results by Rakah and posture name
HAVING (COUNT(?posture) > 1)  # Filters postures that occur more than once in a Rakah
ORDER BY ?rakahUnit ?postureName
```
<!-- ### Competency Question 6:
**Question:** What actions or conditions constitute an incomplete Salah?

**SPARQL Query:**
```
```
-->

### Competency Question 6:
**Question:** How does the duration of each Salah posture vary?

**SPARQL Query:**
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?rakah ?postureName ?startTime ?endTime
       ((xsd:integer(SUBSTR(STRAFTER(STR(?endTime), "_"), 1, 2)) * 3600 + 
         xsd:integer(SUBSTR(STRAFTER(STR(?endTime), "_"), 4, 2)) * 60 + 
         xsd:integer(SUBSTR(STRAFTER(STR(?endTime), "_"), 7, 2))) - 
        (xsd:integer(SUBSTR(STRAFTER(STR(?startTime), "_"), 1, 2)) * 3600 + 
         xsd:integer(SUBSTR(STRAFTER(STR(?startTime), "_"), 4, 2)) * 60 + 
         xsd:integer(SUBSTR(STRAFTER(STR(?startTime), "_"), 7, 2))) AS ?durationInSeconds)
WHERE {
  :S10_FZ_Salah :containsRakah  ?rakah.
  ?rakah :containsPosture ?posture .
  ?posture :hasPostureType ?postureName .
  ?posture :postureStartsAtTime ?startTime .
  ?posture :postureEndsAtTime ?endTime .
}
ORDER BY ?rakah ?postureName

```
### Competency Question 7:
**Question:** Is Salah completed within the prescribed time?

**SPARQL Query:**
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticsalah.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

Ask  
WHERE {
  :S10 rdf:type :Salah .  # Retrieves all Salah instances
  ?salah :hasSalahType ?salahType .  # Relates the Salah to its type (e.g., Fajr, Dhuhr)
  ?salah :isStartedAtTime ?startTime .  # Start time of Salah
  ?salah :isCompletedAtTime ?endTime .  # End time of Salah
  ?salah  :hasPrescribedWindow ?timeliness .  # Relates the Salah to its timeliness constraints
  ?timeliness :hasWindowStartTime ?prescribedStart .  # Prescribed start time for this Salah type
  ?timeliness :hasWindowEndTime ?prescribedEnd .  # Prescribed end time for this Salah type

  # Extract the time (hours and minutes) from the startTime and endTime
  BIND(SUBSTR(STR(?startTime), 12, 5) AS ?startHourMin)  # Extracts hh:mm from '2021-11-19_09:49:54:279'
  BIND(SUBSTR(STR(?endTime), 12, 5) AS ?endHourMin)      # Extracts hh:mm

  # Standardize the prescribed time format to match
  BIND(SUBSTR(STR(?prescribedStart), 1, 5) AS ?prescribedStartTime)  # Extracts hh:mm from '11:53 (PKT)'
  BIND(SUBSTR(STR(?prescribedEnd), 1, 5) AS ?prescribedEndTime)      # Extracts hh:mm

  # Filter to check if Salah is within the prescribed time
  FILTER (?startHourMin >= ?prescribedStartTime && ?endHourMin <= ?prescribedEndTime)
}
```
