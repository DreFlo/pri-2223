<template>
    <div class="col">
        <div>
            <h1>RecFlix</h1>
        </div>
        <div class="input-group mb-2">
            <label class="m-1">
                Search by Participant 
                <input type="checkbox" class="mr-2" v-model="searchByParticipant" id="participantSearchCheckbox"/>
            </label>
            <label class="m-1">
                Release Year 
                <input type="number" min="1900" max="2099" step="1" v-model="startYear" placeholder="from"/>
                <input type="number" min="1900" max="2099" step="1" v-model="endYear" placeholder="to"/>
            </label>
            <label class="m-1">
                IMDb Score
                <input type="number" min="0" max="10" step="0.1" v-model="minScore" placeholder="from"/>
                <input type="number" min="0" max="10" step="0.1" v-model="maxScore" placeholder="to"/>
            </label>
        </div>
        <div class="input-group mb-2">
            <input
                type="text" 
                id="form1" 
                class="form-control" 
                aria-label="Search field" 
                aria-describedby="basic-addon2" 
                v-model="searchInput" 
                v-on:keydown.enter="search"
                :placeholder="!searchByParticipant ? 'Title or Description' : 'Participant name'"
                />
            <button class="btn btn-primary" type="button" @click="search">Search</button>
        </div>
        <div class="row">
            <div style="flex:1;" class="dropdown" v-if="response.docs.length">
                <label for="sort-button">{{sortingBy}}</label>
                <button class="btn btn-primary dropdown-toggle bg-white border-white shadow-none" id="sort-button"
                    aria-expanded="false" data-bs-toggle="dropdown" type="button"
                    style="color: #0C2340;background: var(--bs-border-color-translucent);border-color: var(--bs-border-color-translucent);--bs-secondary-rgb: 108,117,125;opacity: 1;">
                            Sort
                </button>
                <div class="dropdown-menu dropdown-menu-end">
                    <a class="dropdown-item" @click="sortByDate(true)">Release year ascending</a>
                    <a class="dropdown-item" @click="sortByDate(false)">Release year descending</a>
                    <a class="dropdown-item" @click="sortByIMDbScore(true)">IMDb score ascending</a>
                    <a class="dropdown-item" @click="sortByIMDbScore(false)">IMDb score descending</a>
                    <a class="dropdown-item" @click="sortByTitle(true)">Title ascending</a>
                    <a class="dropdown-item" @click="sortByTitle(false)">Title descending</a>
                    <a class="dropdown-item" @click="sortByNumVotes(true)">Number of votes ascending</a>
                    <a class="dropdown-item" @click="sortByNumVotes(false)">Number of votes descending</a>
                    <a class="dropdown-item" @click="sortByTMDbScore(true)">TMDb score ascending</a>
                    <a class="dropdown-item" @click="sortByTMDbScore(false)">TMDb score descending</a>
                </div>
            </div>
        </div>
    </div>
    <search-result-list :response="response"/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import SearchResultList from '../components/SearchResultList.vue';
import type { Response } from '../@types/Response';
import type { Title } from '../@types/Title';

import axios from 'axios';

export default defineComponent({
    name: 'SearchView',
    components: {
        SearchResultList
    },
    data() {
        return {
            searchInput: '',
            response: {
                numFound: 0,
                start: 0,
                docs: [],
                numFoundExact: false
            } as Response,
            searchByParticipant: false,
            startYear: '',
            endYear: '',
            minScore: '',
            maxScore: '',
            sortingBy: ''
        };
    },
    methods : {
        search() {
            this.response = {
                numFound: 0,
                start: 0,
                docs: [],
                numFoundExact: false
            } as Response;

            // Search by Movie URL
            let searchByMovieQuery = 
                'http://localhost:8983/solr/titles/query?q=' +
                this.searchInput +
                '&q.op=OR&defType=edismax&indent=true&qf=title%5E3%20description%20genres' +
                this.getIMDbScoreRange() +
                this.getReleaseYearRange()

            console.log('Search by Movie URL: ', searchByMovieQuery);            

            // Search by Actor URL
            let searchByActorQuery = 
                'http://localhost:8983/solr/titles/query?q=%7B!parent%20which%3D\'content_type:parentDocument\'%7Dname:%22' +
                this.searchInput +
                '%22&q.op=AND&indent=true' +
                this.getIMDbScoreRange() + 
                this.getReleaseYearRange()

            console.log('Search by Actor URL: ', searchByActorQuery);

            // Use query according to checkbox
            axios.get(this.searchByParticipant ? searchByActorQuery : searchByMovieQuery).then((response) => {
                let queryResponse = response.data.response as Response;
                console.log('Query response', queryResponse);
                this.response.docs = queryResponse.docs
                this.response.numFound = queryResponse.numFound;
                this.response.numFoundExact = queryResponse.numFoundExact;
                this.response.start = queryResponse.start;
            });
        },
        getIMDbScoreRange() {
            return '&fq=imdb_score:%20%5B' + (this.minScore == '' ? '*' : this.minScore) + '%20TO%20' + (this.maxScore == '' ? '*' : this.maxScore)  + '%5D'
        },
        getReleaseYearRange() {
            return '&fq=release_year:%20%5B' + (this.startYear == '' ? '*' : this.startYear) + '%20TO%20' + (this.endYear == '' ? '*' : this.endYear) + '%5D'
        },
        sortByDate(ascending: boolean) {
            this.response.docs.sort((a, b) => {
                if (ascending) {
                    this.sortingBy = 'Release year ascending';
                    return (a as Title).release_year - (b as Title).release_year;
                } else {
                    this.sortingBy = 'Release year descending';
                    return (b as Title).release_year - (a as Title).release_year;
                }
            });
        },
        sortByIMDbScore(ascending: boolean) {
            this.response.docs.sort((a, b) => {
                if (ascending) {
                    this.sortingBy = 'IMDb score ascending';
                    return (a as Title).imdb_score! - (b as Title).imdb_score!;
                } else {
                    this.sortingBy = 'IMDb score descending';
                    return (b as Title).imdb_score! - (a as Title).imdb_score!;
                }
            });
        },
        sortByTMDbScore(ascending: boolean) {
            this.response.docs.sort((a, b) => {
                if (ascending) {
                    this.sortingBy = 'TMDb score ascending';
                    return (a as Title).tmdb_score! - (b as Title).tmdb_score!;
                } else {
                    this.sortingBy = 'TMDb score descending';
                    return (b as Title).tmdb_score! - (a as Title).tmdb_score!;
                }
            });
        },
        sortByTitle(ascending: boolean) {
            this.response.docs.sort((a, b) => {
                if (ascending) {
                    this.sortingBy = 'Title ascending';
                    return (a as Title).title.localeCompare((b as Title).title);
                } else {
                    this.sortingBy = 'Title descending';
                    return (b as Title).title.localeCompare((a as Title).title);
                }
            });
        },
        sortByNumVotes(ascending: boolean) {
            this.response.docs.sort((a, b) => {
                if (ascending) {
                    this.sortingBy = 'Number of votes ascending';
                    return (a as Title).tmdb_popularity! - (b as Title).tmdb_popularity!;
                } else {
                    this.sortingBy = 'Number of votes descending';
                    return (b as Title).tmdb_popularity! - (a as Title).tmdb_popularity!;
                }
            });
        }
    },
    watch : {
        searchByParticipant(newValue, _) {
            console.log('Search by Actor set to: ', newValue);            
        },
        startYear(newvalue, _) {
            console.log('Start Year set to: ', newvalue);            
        }
    }
})
</script>
