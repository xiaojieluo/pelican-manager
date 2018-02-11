// var bootstratTable = {}
//
// bootstrapTable.install = function(Vue, options){
//     Vue.prototype.$http
// }

import Vue from 'vue'
import bootstrapTable from './bootstrap-table/src/bootstrap-table'

export default {
    install: function(val, name='$bootstratTable'){
        Object.defineProperty(Vue.prototype, '$http', { value: bootstrapTable })
    }
}
