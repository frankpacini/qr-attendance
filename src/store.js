import Vue from "vue";
import Vuex from "vuex";
import api from "./api";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    //Initial state
    
    loggedIn: "unset",
    
    user: "", //the email address of the user,
  },
  mutations: {
    
    setLoggedInFalse(state) {
      state.loggedIn = false;
    },
    setLoggedInTrue(state) {
      state.loggedIn = true;
    },
    setUser(state, email) {
      state.user = email;
      state.loggedIn = true;
    },
  },
  getters: {
    
    isLoggedIn: state => {
      return state.loggedIn;
    },
  },
  actions: {
    logout(state) {
      api.logout();
    }
  }
});

export default store;
