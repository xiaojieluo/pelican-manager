<template>
    <div class="container">
        <!-- Article Meta -->
        <Collapse v-model="value">
            <Panel name="meta">
                    Article meta
                    <span slot="content">
                        <Row slot="content" class="meta" v-for="key in Object.keys(article.meta)">
                            <Col span="5">{{ key }}:</Col>
                            <Col span="8">
                                <Select v-model="article.meta[key]" v-if="key == 'status'" style="width:200px;margin-bottom: 40px">
                                    <Option value="published" key="published">published</Option>
                                    <Option value="draft" key="draft">draft</Option>
                                </Select>
                                <Input v-model="article.meta[key]" v-else></Input>
                            </Col>
                        </Row>
                    </span>
            </Panel>

            <Panel name="text">
                Text
                <Row slot="content" class="text">
                    <Input type="textarea" :autosize="true" v-model="article.text"></Input>
                </Row>
            </Panel>
        </Collapse>

        <Button type="primary" :loading="loading" icon="checkmark-round" @click="update">
            <span v-if="!loading">Save</span>
            <span v-else>updating...</span>
        </Button>
    </div>

</template>

<script>
export default {
    data(){
        return {
            msg: 'Helo',
            article: {'meta': '', 'text': ''},
            value: "meta",
            loading: false
        }
    },
    created: function(){
        this.make_input()
        this.get_article()
    },
    methods: {
        update: function(){
            console.log("update.")
            this.loading = true
            let url = 'http://127.0.0.1:5000/api/articles/'+ this.$route.query.path
            this.$ajax.put(url, {
                'meta': this.article.meta,
                'text': this.article.text
            }).then((res) => {
                    console.log(res)
                    this.loading = false
                    this.$Notice.success({
                        title: '更新成功！',
                        desc: this.article.path + ' 更新成功！'
                    })
            })
        },
        make_input: function(){
        },
        get_article: function (){
            let url = 'http://127.0.0.1:5000/api/articles/'+ this.$route.query.path
            this.$ajax.get(url)
                .then((res) => {
                    let data = res.data
                    console.log(data.status)
                    if (data.meta.status === undefined){
                        data.meta.status = 'published'
                    }
                    console.log(data)
                    this.article = data
                    console.log(this.article.meta.title)
                }).catch((res) => {
                    console.log(res)
                })
        }
    }
}
</script>

<style lang="css">
.meta{
    margin-bottom: 3px;
}
</style>
