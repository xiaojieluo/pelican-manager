<template lang="html">
    <div class="container">
        <span v-for="item in options">
            <SettingComponents
                :title="item.title"
                :key_="item.key"
                :type="item.type"
                v-model="serv_options[item.key]"
            />
            <br>
        </span>
        <Row>
            <Col span="2"><Button @click="save">Save</Button></Col>
            <Col span="6"><Button @click="reset">Reset</Button></Col>
        </Row>
    </div>
</template>

<script>
import SettingComponents from '@/components/SettingComponents'

export default {
    name: 'OptionsComponent',
    props: ['options'],
    computed:{
        count(){
            return this.$store.state.options_general.options
        },
        serv_options: {
            // 返回从服务器获取的数据， 填充表单
            // this.$store.dispatch('get_options')
            get () {
                return this.$store.state.options_general.options
            },
            set (value) {
                this.$store.commit('update_options', value)
                console.log("set")
                console.log(value)
            }
        }
    },
    mounted: function(){
        console.log("mounted")
        console.log(this.options)
        // console.log(this.$store.commit)
        let keys = this.get_keys()
        this.$store.dispatch('get_options', {keys: keys})
    },
    components: {
        'SettingComponents': SettingComponents
    },
    methods: {
        /**
         * 获取所有 key
         * @return {[type]} [description]
         */
        get_keys: function(){
            let keys = []
            for (var i = 0; i < this.options.length; i++) {
                keys.push(this.options[i].key)
            }
            return keys
        },
        /**
         * 将修改的数据保存到服务器
         * @return {[type]} [description]
         */
        save: function(){
            console.log("save")
            console.log(this.serv_options.author)
            this.$store.dispatch('save', {data: this.serv_options}).then(response => {
                console.log("Success!")
                console.log(response)
                this.$Message.success("保存成功！")
            }, error => {
                console.error(error)
                this.$Message.error("保存错误！")
            })

        },
        /**
         * 放弃修改， 从服务器重新请求数据
         * @return {[type]} [description]
         */
        reset: function(){
            console.log("reset")
            let keys = this.get_keys()
            this.$store.dispatch('get_options', {keys: keys})
                .then(res => {
                    console.log("reset succesful!")
                    this.$Message.success('恢复成功！')
                }, error => {
                    this.$Message.error("失败")
                })

        }
    }
}
</script>

<style lang="css">
.settingspan {
    margin-bottom: 100px;
}
</style>
