# PRI Turma 2 Grupo 6

## Objetivo

Recomendação baseada em:
 - género e descrição
 - ano produção
 - atores
 - produtor
 - local de produção

## Análise dados

### Ficheiros Titles - 5850 linhas

Id - todos os id´s são únicos

Title - existem alguns títulos repetidos mas a maior parte trata-se de filmes diferentes

Type - todos os registos pertencem às classes existentes (MOVIE e SHOW)

Description - 6 registos iguais:

* **A Lion in the House trata-se do mesmo filme e por isso remove-se duplicado [Eliminar 11216 e 11217 de credits, e filme]**

* Out of my league são 2 filmes diferentes mas um dá seguimento ao outro, nada a alterar

* Elite Short Stories também são 2 filmes diferentes, nada a alterar

* **18 registos sem descrição, eliminar**

Release_year - anos entre 1945 e 2022

**Age_certification - 2619 sem valor, substituir por 'unrated'**

**Runtime - 14 registos com 0 (não especificado), substituir por 'null'**

**Genre - lista de géneros, dividir e criar nova tabela (cada género é uma coluna)**

Production_countries - lista de países, manter assim

Seasons - todas as séries (SHOWs) têm um número inteiro de temporadas, todos os filmes (MOVIEs) não têm informação sobre temporadas

**Imdb_id - 403 registos sem valor**

**Imdb_score - 79 registos com imbd_id mas sem imbd_score e sem imdb_votes, ir buscar valores ao site**

**Imdb_votes - 16 registos com imbd_id e imbd_score mas sem imdb_votes, ir buscar valor ao site**

**Tmdb_popularity - 91 registos sem valor e sem tmbd_score, ir buscar valores ao site ??**

**Tmdb_score - 220 registos sem valor, ir buscar valor ao site ??**

### Ficheiro Credits - 77801 linhas

Person_id - id´s iguais para a mesma pessoa

**Title_id - verificar se existem no outro ficheiro**

Name - Existem nomes iguais, será natural

Character - 5222 registos de atores (ACTOR) sem nome da personagem (deixar estar), diretores não têm personagem

Role - todos os registos pertencem às classes existentes (ACTOR e DIRECTOR)



