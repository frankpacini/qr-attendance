import Vue from "vue";
import Router from "vue-router";
import store from "./store"; // TODO: How do we import the store globally ?
import api from "./api";
import QR from "./components/Home.vue"

Vue.use(Router);

const redirectIfLoggedIn = function(next) {
  if (store.getters.isLoggedIn == true) {
    next("home");
  } else if (store.getters.isLoggedIn == "unset") {
    api.verifyLogin();
  } else {
    next();
  }
}; 
let x = QR.data()['value'].slice('http://localhost:8080'.length);
console.log("x: " + x)
// const setX = function(q) {
//   x = q;
//   console.log("x: " + x)
// }

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      beforeEnter: (to, from, next) => redirectIfLoggedIn(next),
      // redirect: {
      //   name: "login",
      // }
      // component: () => import("./views/Landing.vue"),
    },
    {
      path: "/login",
      name: "login",
      //beforeEnter: (to, from, next) => redirectIfLoggedIn(next),
      component: () => import("./views/LoginPage.vue"),
    },
    {
      path: "/home",
      name: "home",
      component: () => import("./views/HomePage.vue"),
    }, 
    {
      path: x,
      name: "atten",
      component: () => import("./views/LoginPage.vue"),
    }
  ]
});
console.log("x: " + x)

export default router;

