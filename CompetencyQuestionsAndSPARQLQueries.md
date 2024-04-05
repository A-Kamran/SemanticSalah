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
SELECT (COUNT(?rakah) AS ?rakahCount)
WHERE {
  ?prayer rdf:type :Salah;
          :hasSalahUnit ?unit.
  ?unit :hasSalahUnitType ?rakah.
}
```
### Competency Question 3:
**Question:** Which postures precede or follow each other in Salah?

**SPARQL Query:**
```

```
### Competency Question 4:
**Question:** What is the correct sequence of Salah postures?

**SPARQL Query:**
```

```
### Competency Question 5:
**Question:** Which postures are performed multiple times in a single rakah?

**SPARQL Query:**
```

```
### Competency Question 6:
**Question:** What actions or conditions constitute an incomplete Salah?

**SPARQL Query:**
```

```
### Competency Question 7:
**Question:** How does the duration of each Salah posture vary?

**SPARQL Query:**
```
```
### Competency Question 8:
**Question:** Is Salah completed within the prescribed time?

**SPARQL Query:**

```
