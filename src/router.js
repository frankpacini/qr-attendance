import Vue from "vue";
import Router from "vue-router";
import store from "./store"; // TODO: How do we import the store globally ?
import api from "./api";

Vue.use(Router);

const redirectIfLoggedIn = function(next) {
  if (store.getters.isLoggedIn == true) {
    next("browse");
  } else if (store.getters.isLoggedIn == "unset") {
    api.verifyLogin();
  } else {
    next();
  }
};


const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      // component: () => import("./views/Landing.vue"),
      beforeEnter: (to, from, next) => redirectIfLoggedIn(next)
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/LoginPage.vue"),

    }
   
  
  ]
});


export default router;
