import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

import options_general from './modules/options/general'

export default new Vuex.Store({
    modules:{
        options_general
    }
})
