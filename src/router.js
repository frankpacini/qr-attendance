import Vue from "vue";
import Router from "vue-router";
import store from "./store"; // TODO: How do we import the store globally ?
import api from "./api";

Vue.use(Router);


const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      // component: () => import("./views/Landing.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/Login.vue"),
    }
   
  
  ]
});


export default router;
