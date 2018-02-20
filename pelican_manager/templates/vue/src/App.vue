<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo"></div>
                    <div class="layout-nav">
                        <MenuItem name="1">
                            <Icon type="ios-navigate"></Icon>
                            Item 1
                        </MenuItem>
                        <MenuItem name="2">
                            <Icon type="ios-keypad"></Icon>
                            Item 2
                        </MenuItem>
                        <MenuItem name="3">
                            <Icon type="ios-analytics"></Icon>
                            Item 3
                        </MenuItem>
                        <MenuItem name="4">
                            <Icon type="ios-paper"></Icon>
                            Item 4
                        </MenuItem>
                    </div>
                </Menu>
            </Header>
            <Layout>
                <Sider hide-trigger :style="{background: '#fff'}"
                    collapsible
                    breakpoint="md"
                    :collapsed-width="78"
                    >
                    <Menu
                        :active-name="active_name" theme="light" width="auto" :open-names="['articles']"
                        @on-select="sidemenu_select"
                        >
                        <Submenu name="dashboard">
                            <template slot="title">
                              <Icon type="ios-bookmarks"></Icon>
                              Dashboard
                            </template>
                            <MenuItem name="Home">Home</MenuItem>
                        </Submenu>
                        <Submenu name="article">
                            <template slot="title">
                                <Icon type="ios-bookmarks"></Icon>
                                文章
                            </template>
                            <MenuItem name="ArticleAll">所有文章</MenuItem>
                            <MenuItem name="articles_write">写文章</MenuItem>
                            <MenuItem name="1-2">分类目录</MenuItem>
                            <MenuItem name="1-3">标签</MenuItem>
                        </Submenu>
                        <Submenu name="options">
                            <template slot="title">
                                <Icon type="ios-keypad"></Icon>
                                设置
                            </template>
                            <MenuItem name="options_general">常规</MenuItem>
                            <MenuItem name="options_published">发布设置</MenuItem>
                        </Submenu>
                        <Submenu name="3">
                            <template slot="title">
                                <Icon type="ios-analytics"></Icon>
                                Item 3
                            </template>
                            <MenuItem name="3-1">Option 1</MenuItem>
                            <MenuItem name="3-2">Option 2</MenuItem>
                        </Submenu>
                    </Menu>
                </Sider>
                <Layout :style="{padding: '0 24px 24px'}">
                    <Breadcrumb :style="{margin: '24px 0'}">
                        <BreadcrumbItem to="/">Home</BreadcrumbItem>
                        <BreadcrumbItem to='/articles'>Articles</BreadcrumbItem>
                        <BreadcrumbItem>Layout</BreadcrumbItem>
                    </Breadcrumb>
                    <Content :style="{padding: '24px', minHeight: '280px', background: '#fff'}">
                        <router-view></router-view>
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>

<script>
export default {
  name: 'App',
  data () {
      return {
           active_name: 'Home'
      }
  },
  methods: {
      sidemenu_select: function(name){
          // 侧边栏点击事件
          console.log(name)
          this.active_name = name
          // if (name == 'articles_all') {
          //     this.$router.push({path: '/articles'})
          // }
          this.$router.push({ name: name })
      }
  }
}
</script>

<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
</style>
