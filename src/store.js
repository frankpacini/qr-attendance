import Vue from "vue";
import Vuex from "vuex";
import api from "./api";
import { colors } from "./utilities/branding";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    //Initial state
    
    loggedIn: "unset",
    

    message: "",
    show: false,
    color: colors.white,
  },
  mutations: {
    setLoggedInFalse(state) {
      state.loggedIn = false;
    },
    setLoggedInTrue(state) {
      state.loggedIn = true;
      console.log('state: logged in')
    },
    setUser(state, email) {
      state.user = email;
      state.loggedIn = true;
    },
    setSnackbar(state, message, show, color) {
      state.message = message;
      state.show = show;
      state.color = color;
    },
  },
  getters: {
    isLoggedIn: state => {
      return state.loggedIn;
    },
  },
  actions: {
    logout() {
      api.logout();
    }
  }
});

export default store;
