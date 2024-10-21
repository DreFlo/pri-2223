<template>
    <div v-if="(doc as Title).content_type == 'parentDocument'">
        <title-card :title="(doc as Title)"/>
    </div>
    <div v-else>
        <credit-card :credit="(doc as Credit)"/>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import type { Title } from '../@types/title';
import type { Credit } from '../@types/credit';
import type { PropType } from 'vue';

import TitleCard from './TitleCard.vue';
import CreditCard from './CreditCard.vue';

export default defineComponent({
    name: 'SearchResult',
    components: {
        TitleCard,
        CreditCard
    },
    props: {
        doc: {
            type: Object as PropType<Title | Credit>,
            required: true
        }
    }
})
</script>