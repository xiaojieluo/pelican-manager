<template lang="html">
    <div class="container">
        {{ title }}
        <input type="text" name="" :value="value" @input="$emit('balabala', $event.target.value)">
    </div>
</template>

<script>
export default {
    name: 'InputText',
    props: {
        type: { type: String, default: ''},
        value: {},
        title: {},
    },
    model: {
        event: 'balabala'
    },
    data () {
        return {
            msg: 'Hello, components'
        }
    },
}
</script>

<style lang="css">
</style>
