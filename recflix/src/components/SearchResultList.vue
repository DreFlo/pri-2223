<template>
    <div>
        <search-result :doc="doc" v-for="doc in $props.response.docs" :key="doc.id"/>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import type { Response } from '../@types/Response';
import type { PropType } from 'vue';

import SearchResult from './SearchResult.vue';

export default defineComponent({
    name: 'SearchResultList',
    components: {
        SearchResult
    },
    props: {
        response: {
            type: Object as PropType<Response>,
            required: true
        }
    }
})
</script>