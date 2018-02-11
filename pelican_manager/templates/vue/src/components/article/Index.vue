<template id="">
    <div class="container" style="width: 100%">
        <Table
            border
            ref="selection"
            :loading=loading
            size="small"
            :columns="columns"
            :data="datas"
            @on-row-click="click_select"
        >
        </Table>
        <div style="margin: 10px;overflow: hidden">
            <div style="float: right;">
                <Page
                    :total=total
                    :current=current
                    :page-size=page_size
                    @on-change="changePage"
                >
                </Page>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
export default {
    name: "ArticleIndex",
    data() {
        return {
            columns: [
                { type: 'selection', width: 60, align: 'center' },
                { type: 'index' },
                // { key: 'path',  title: '路径' },
                { key: 'title', title: '标题' },
                { key: 'author', title: '作者', align: 'center'},
                { key: 'date', title: '时间', align: 'center' },
                { key: 'modified', title: '修改时间', align: 'center' },
                { key: 'category', title: '分类', align: 'center' },
                { key: 'status', title: '状态', align: 'center' },
                { key: 'action', title: '操作', fixed: 'right', render: (h, params) => {
                    return h('div', [
                        h('Button', {
                            props: { type: "primary", size: "small"},
                            style: { marginRight: '5px' },
                            on: { click: () => {
                                this.show(params)
                            }}
                        }, 'View'),
                        h('Button', {
                            props: { type: "error", size: "small"},
                            on: { click: () => {
                                this.remove(params)
                            }}
                        }, 'Delete')
                    ])
                }},
            ],
            total: 0,
            page_size: 10,
            current: 1,
            datas: [],
            all: null,
            loading: true,
            select: [], // 选择的行
        }
    },
    mounted: function(){
        // this.table_columns()
        this.tableData()
    },
    methods: {
        /**
         * 单击选择
         * @return {[type]} [description]
         */
        click_select: function(param, index){
            console.log(param)
            console.log(index)
            if (this.select.length == 0){
                this.select.push(param)
            }else {
                for (var i = 0; i < this.select.length; i++) {
                    let select = this.select[i]
                    let res;
                    if (select.path == param.path) {
                        console.log("==")
                        break;
                    } else {
                        this.select.push(param)
                        break;
                    }
                }
            }
            console.log(this.select)
        },
        show(param){
            console.log("Show")
            this.$router.push({path: '/articles/edit', query: { 'path': param.row.path }})
        },
        remove(index){
            console.log("Remove")
            console.log(index)
        },
        // table_columns: function(){
        //     // 获取页面的 columns
        //     console.log()
        // },
        tableData: function () {
            let datas = [];
            console.log("开始请求")
            this.$ajax.get('http://127.0.0.1:5000/api/articles/')
                .then((res) => {
                    if (res.status == 200) {
                        for (var i = 0; i < res.data.results.length; i++) {
                            let result = res.data.results[i]
                            let data = result.meta
                            data['path'] = result.path
                            // 给文章设置 status 背景色
                            let cellClassName = {'status': 'table-status-published'};
                            if (data.hasOwnProperty('status') && data['status'] == 'draft') {
                                cellClassName['status'] = 'table-status-draft'
                            }else {
                                data['status'] = 'published'
                            }
                            data['cellClassName'] = cellClassName

                            // 添加 edit 操作
                            datas.push(data)
                        }
                        this.total = res.data.total
                        this.datas = this.pagination(this.current, this.page_size, datas)
                        this.loading = false
                    }
                })
                .catch(function(data){
                    console.log(data)
                    datas = []
                    this.total = 0
                })
        },

        pagination: function(pageNo = 1, pageSize = 10, data){
            var offset = (pageNo - 1) * pageSize;
			let result = (offset + pageSize >= data.length) ? data.slice(offset, data.length) : data.slice(offset, offset + pageSize);
			return result
        },

        changePage: function(page){
            this.current = page
            this.loading = true
            this.tableData()
        }
    },
}

</script>


<style>
.ivu-table .table-status-published {
    background-color: #19be6b;
    color: #fff;
}
.ivu-table .table-status-draft {
    background-color: #ff9900;
    color: #fff;
}
</style>
