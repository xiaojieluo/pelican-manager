<template lang="html">
    <div class="container">
        <Options
            :options="options"
        />
    </div>
</template>

<script>
import Options from '@/components/options/_options'

export default {
    name: "optionsPublished",
    components: {
        'Options': Options
    },
    data () {
        return {
            options: [
                { title: '每页显示几条', key: 'default_pagination', placeholder: '标题', type: 'int'},
            ],
        }
    }
}
</script>

<style lang="css">
</style>
