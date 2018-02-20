import axios from 'axios'
// import actions from './vuex/actions'

const state = {
    count: 0
}

const mutations = {
    add(state, n){
        state.count += n
    }
}

const actions = {
    increment(store) {
        console.log("Action")
    }
}

const options_general = {
    state: {
        options: {}
    },
    mutations: {
        get_options(state, options=['path']){
            console.log(options)
        }
    },
    actions: {
        get_options(context, options){
            console.log(options)
            // context.commit('get_options', options)
        }
    }

}


import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export default new Vuex.Store({
    state,
    mutations,
    actions
})
