<template lang="html">
    <div class="container">
        <span v-for="item in general_options">
            <SettingComponents
                :title="item.title"
                :key_="item.key"
                :type="item.type"
                v-model="options[item.key]"
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
    name: 'optionsGeneral',
    data() {
        return {
            msg: 'Hello',
            st: this.$store.state.count,
            general_options: [
                { title: '站点名称', key: 'sitename', placeholder: '标题' },
                { title: '站点url', key: 'siteurl', placeholder: '站点 URL' },
                { title: '默认作者', key: 'author', placeholder: '默认作者' },
                { title: '时区', key: 'timezone', placeholder: '时区' },
                { title: '日期格式', key: 'default_date_format', placeholder: '默认日期格式' },
            ],
        }
    },
    computed:{
        count(){
            return this.$store.state.options_general.options
        },
        options: {
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
        console.log("State")
        console.log(this.$store.commit)
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
            for (var i = 0; i < this.general_options.length; i++) {
                keys.push(this.general_options[i].key)
            }
            return keys
        },
        /**
         * 将修改的数据保存到服务器
         * @return {[type]} [description]
         */
        save: function(){
            console.log("save")
            console.log(this.options.author)
            this.$store.dispatch('save', {data: this.options}).then(response => {
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
