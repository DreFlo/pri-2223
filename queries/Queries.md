# Queries

## Query 1

### Normal
I want to watch a title about cars with rating > 7.0.

```
q: car
qf: title description
fq: imdb_score: [7.0 TO *]
```

http://localhost:8983/solr/#/titles/query?q=car&q.op=OR&defType=edismax&indent=true&qf=title%20description&rows=20&fl=title,%20description,%20imdb_score&fq=imdb_score:%20%5B7.0%20TO%20*%5D

### Boosted
I want to watch a title about cars with rating > 7.0, description has more weight

```
q: car
qf: title^5 description 
fq: imdb_score: [7.0 TO *]
```

Aparecem primeiro os que têm mais ocorrências de car na description

http://localhost:8983/solr/#/titles/query?q=car&q.op=OR&defType=edismax&indent=true&qf=title%5E3%20description&rows=20&fl=title,%20description,%20imdb_score&fq=imdb_score:%20%5B7.0%20TO%20*%5D

## Query 2

### Normal
A title related to "family" and "christmas"

```
q: christmas family
qf: title description
```

http://localhost:8983/solr/#/titles/query?q=christmas%20family&q.op=OR&defType=edismax&indent=true&qf=title%20description&rows=100&fl=title,%20description

### Boosted
A title related to "family" and "christmas" (4 words between the two words)


```
q: christmas family
qf: title description
pf: title description
ps: 4 
```

http://localhost:8983/solr/#/titles/query?q=christmas%20family&q.op=OR&defType=edismax&indent=true&qf=title%20description&rows=100&ps=4&fl=title,%20description&pf=title%20description

## Query 3

### Normal
All movies since 2016 where Christina Hendricks is actor

```
q: "Christina Hendricks"
fq: release_year: [2016 TO *]
```

http://localhost:8983/solr/#/titles/query?q=%7B!parent%20which%3D'content_type:parentDocument'%7Dname:%22Christina%20Hendricks%22&q.op=AND&indent=true&fl=id,%20title,%20release_year&fq=release_year:%20%5B2016%20TO%20*%5D

### Fuzzy

```
q: "Christina~"
fq: release_year: [2016 TO *]
```

http://localhost:8983/solr/#/titles/query?q=%7B!parent%20which%3D'content_type:parentDocument'%7Dname:%22Christina~%22&q.op=AND&indent=true&fl=id,%20title,%20release_year&rows=100&fq=release_year:%20%5B2016%20TO%20*%5D

## Query 4

### Normal
Search for the title and description of another movie (Fast & Furious Spy Racers)

```
q: A government agency recruits teen driver Tony Toretto and his thrill-seeking friends to infiltrate a criminal street racing circuit as undercover spies
qf: description
```

http://localhost:8983/solr/#/titles/query?q=A%20government%20agency%20recruits%20teen%20driver%20Tony%20Toretto%20and%20his%20thrill-seeking%20friends%20to%20infiltrate%20a%20criminal%20street%20racing%20circuit%20as%20undercover%20spies&q.op=OR&defType=edismax&indent=true&qf=title%20description&rows=100&fl=title,%20description&stopwords=true

### Boosted
Search for the title and description of another movie (Fast & Furious Spy Racers) using term boost

```
q: A government agency recruits teen driver^2 Tony Toretto and his thrill-seeking friends^2 to infiltrate a criminal street racing^2 circuit as undercover spies
qf: description
```
http://localhost:8983/solr/#/titles/query?q=A%20government%20agency%20recruits%20teen%20driver%5E2%20Tony%20Toretto%20and%20his%20thrill-seeking%20friends%5E2%20to%20infiltrate%20a%20criminal%20street%20racing%5E2%20circuit%20as%20undercover%20spies&q.op=OR&defType=edismax&indent=true&qf=title%20description&rows=100&fl=title,%20description&stopwords=true

## Query 5

### Normal
Who participates in the movie 'Bonnie and Clyde'?

```
q: "Bonnie and Clyde"
qf: title
```

http://localhost:8983/solr/#/titles/query?q=%7B!child%20of%3D'content_type:parentDocument'%7Dtitle:%22Bonnie%20and%20Clyde%22&q.op=AND&indent=true&fl=name,%20role&rows=100