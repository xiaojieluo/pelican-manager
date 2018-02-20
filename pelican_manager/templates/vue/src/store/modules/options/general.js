import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.headers.post['Content-Type'] = 'application/json'

const state = {
    options: {}
}

const mutations = {
    /**
     * 更新 options 值
     * @param {[type]} state [description]
     * @param {[type]} data  [description]
     */
    set_options(state, data){
        state.options = data
    },
    /**
     * 更新 options 的值
     * data : object
     *      .name: 要更新的 key_
     *      .value: 要更新的值
     * @param  {[type]} state [description]
     * @param  {[type]} data  [description]
     * @return {[type]}       [description]
     */
    update_options(state, data){
        state.options[data.name] = data.value
    },
}

const actions = {
    get_options({commit}, payload){
        return new Promise((resolve, reject) => {
            var keys = payload.keys
            var url = '/api/settings/?key='+keys.toString()
            axios.get(url)
                .then((res) => {
                    if (res.status == 200) {
                        commit('set_options', res.data)
                        resolve(res)
                    }
                }).catch((res) => {
                    reject(res)
                })
        })
    },
    save: function ({commit}, payload){
        return new Promise((resolve, reject) => {
            console.log("Save.....")
            let data = JSON.stringify(payload.data)
            console.log(data)
            var url = '/api/settings/'
            axios.post(url, data)
                .then(response => {
                    resolve(response)
                }, error => {
                    reject(response)
                })
        })
    }
}

export default {
    state,
    mutations,
    actions
}
