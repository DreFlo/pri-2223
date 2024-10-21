<template>
    <div class="card">
        <a :href="'https://www.justwatch.com/us/search?q=' + credit.name + '&person_id=' + credit.person_id"  class="text-decoration-none">{{credit.name}}</a>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import type { Credit } from '../@types/credit';
import type { PropType } from 'vue';

export default defineComponent({
    name: 'CreditCard',
    props: {
        credit: {
            type: Object as PropType<Credit>,
            required: true
        }
    },
})
</script>