import { getCookie, deleteCookie } from "./js/authentication";
import router from "./router";
import { post, get, _delete } from "./requests";
import store from "./store"; //might be a circular import
import notify from "./utilities/notify";
import { colors } from "./utilities/branding";

const api = {
  logout() {
    post("/auth/logout", { sessionId: getCookie("SID") })
      .then(() => {
        deleteCookie("SID");
        store.commit("setLoggedInFalse");
        router.push("/");
        notify("User logged out", colors.green);
      })
      .catch(() => {
        notify("Unable to logout. Please try again later. ", colors.red);
      });
  },
  getSessionID(username, password) {
    post("/auth/login", { email: username, password: password })
      .then(() => {
        /*
        if (response.data.admin == true) {
          store.commit("setIsAdmin");
        }
        */
        store.commit("setUser", username);
        store.commit("setLoggedInTrue");
        router.push("/browse");
        notify("Successfully logged in", colors.green);
      })
      .catch(() => {
        notify("Incorrect username or password. Please try again", colors.red);
      });
  },
  verifyLogin() {
    const sessionId = getCookie("SID");
    if (!sessionId) {
      store.commit("setLoggedInFalse");
      router.push("/");
      return false;
    }
    return post("/auth/verifySession", { sessionId: sessionId })
      .then(() => {
        store.commit("setLoggedInTrue");
        router.push("/browse");
        return true;
      })
      .catch((error) => {
        deleteCookie("SID");
        store.commit("setLoggedInFalse");
        router.push("/login");
        notify(error.response.data.message, colors.red);
        return false;
      })
  },
};

export default api;
