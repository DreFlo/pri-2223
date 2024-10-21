<template>
    <div class="card mb-2">
        <div class="card-body p-4">
            <h1 class="card-title"><a :href="'https://www.imdb.com/title/' + title.imdb_id"  class="text-decoration-none">{{title.title}}</a></h1>
            <p class="card-text text-align-justify">{{title.description}}</p>
            <div v-if="credits.length">
                <button class="btn btn-primary mb-2" type="button" @click="toggleCollapseCredits">{{showingCredits ? 'Hide Credits' : 'Show Credits'}}</button>
                <div class="collapse" :id="title.id + '_credits'" :ref="title.id + '_credits'">
                    <credit-card :credit="credit" v-for="credit in credits" />
                </div>
            </div>
            <div v-else>
                <button class="btn btn-secondary mb-2" disabled type="button">Credits</button>
                <p class="card-text">There are no credits for this title</p>
            </div>
        </div>
        <div class="card-footer">
            <small class="text-muted">{{title.release_year}}</small>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import axios from 'axios'

import type { Title } from '../@types/title'
import type { Credit } from '../@types/credit'
import type { Response } from '../@types/response'
import type { PropType } from 'vue';

import CreditCard from './CreditCard.vue'

export default defineComponent({
    name: 'TitleCard',
    props: {
        title: {
            type: Object as PropType<Title>,
            required: true
        }
    },
    components : {
        CreditCard
    },
    data() {
        return {
            credits: [] as Credit[],
            showingCredits: false
        }
    },
    created() {
        axios.get(
            'http://localhost:8983/solr/titles/query?q=%7B!child%20of%3D\'content_type:parentDocument\'%7Did:%22' + 
            this.title.id +
            '%22&q.op=AND&indent=true&rows=100').then((response) => {
            let queryResponse = response.data.response as Response
            console.log(`Credits for ${this.title.title} received: `, queryResponse);
            queryResponse.docs.forEach((doc) => {
                if (!((doc as Title).content_type == 'parentDocument')) {
                    this.credits.push(doc as Credit)
                }
            })
        })
    },
    methods : {
        toggleCollapseCredits() {
            let creditsCollapse = this.$refs[this.title.id + '_credits'] as HTMLElement
            this.showingCredits = !this.showingCredits
            if (creditsCollapse.classList.contains('collapse')) {
                creditsCollapse.classList.remove('collapse')
            } else {
                creditsCollapse.classList.add('collapse')
            }
        }
    }
})
</script>