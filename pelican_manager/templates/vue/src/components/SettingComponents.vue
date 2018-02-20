<template lang="html">
    <div class="container">
        <Row>
            <Col span="4"><b>{{ title }}</b> </Col>
            <Col span="8">
                <!-- 数字类型 -->
                <InputNumber v-if="type == 'int'" :value="value" @input="change" />
                <!-- 字符串类型 -->
                <Input
                    v-else
                    :value="value"
                    @input="change"
                >
                </Input>
            </Col>
        </Row>
    </div>
</template>

<script>
/**
 * 设置子组件
 * 通过此组件实例化 iview 的 Input 组件
 * props:
 *      type: 指定 Input 类型，默认 '',  支持的值： textarea
 *      value: v-model 绑定的数据， 无需传入
 *      title: Input 要显示的标题
 *      placeholder: placeholder， 默认为空
 *
 */
export default {
    name: 'SettingComponents',
    props: {
        type: '',
        title: {},
        key_: '',
        value: ''
    },
    data () {
        return {
            msg: 'Hello, components'
        }
    },
    methods: {
        /**
         * 将 key 与 value 通过 action 更新 vuex 状态
         * @param  {[type]} value [description]
         * @return {[type]}       [description]
         */
        change: function(value){
            var name = this.key_

            console.log("changess")
            console.log(this.key_)
            console.log(value)
            this.$store.commit('update_options', { name : this.key_, value: value})
            // this.$state.dispatch('update_options', {name})
        }
    }
}
</script>

<style lang="css">
</style>
