import Vue from "vue";
import Router from "vue-router";
import store from "./store"; // TODO: How do we import the store globally ?
import api from "./api";

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
      path: "/attendance/:id",
      name: "attendance",
      component: () => import("./views/AttendancePage.vue"),
    },
    {
      path: "/meeting/createMeeting",
      name: "createMeeting",
      component: () => import("./views/CreateMeetingPage.vue")
    },
    {
      path: "/meeting/pastMeetings",
      name: "pastMeeting",
      component: () => import("./views/PastMeetingPage.vue")
    },
    {
      path: "/meeting/:id",
      name: "meeting",
      component: () => import("./views/MeetingPage.vue")
    }
  ]
});

export default router;

