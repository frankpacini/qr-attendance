<template>
        <v-card>
            <v-card-title >
                <v-row justify="center">
                    <h2 style="color:#1976d2">Login</h2>
                </v-row>
            </v-card-title>
          <v-card-text>
            <v-form class="form-signin">
                <div class="form-label-group">
                    <v-text-field
                        id="email"
                        label="Email"
                        autofocus
                        v-model="email"
                    > </v-text-field>
                    <v-text-field
                        id="password"
                        label="Password"
                        autofocus
                        v-model="password"
                        :append-icon="visibility ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="() => (visibility = !visibility)"
                        :type="visibility ? 'text' : 'password'"
                    > </v-text-field>
                </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
              <v-row justify="center">
              <v-btn tile color="success" v-on:click="submit" width="95%" type="submit">Login</v-btn>
              </v-row>
          </v-card-actions>
            <div class="text-center ma-2">
            <v-snackbar v-model="snackbar">
                {{ text }}
            <v-btn
                color= state.color
                text
                on:click="closeSnackbar"
            >
            Close
            </v-btn>
            </v-snackbar>
            </div>
        </v-card>
</template>

<script>
import api from "../api.js";
import state from "../store.js";
import { colors } from "../utilities/branding";
// import { post } from "../requests"
import store from "../store.js";
export default {
    components: {
      //state,
    },
    
    data() {
        return {
            email: "",
            password: "",
            visibility: false,
            snackbar: state.show,
            text: state.message,
            state: state
        }
    },  



    methods: {
        submit(){
            if(this.email != "" && this.password != "") {
                api.getSessionID(this.email, this.password)
                // post('/auth/login', {
                //     email: this.email,
                //     password: this.password
                // })
                // .then(res => {
                //     console.log("Logged In")
                //     console.log(res)
                //     store.commit('setLoggedInTrue')
                //     this.$router.push('/home')
                // }).catch(err => {
                //     console.log(err)
                // })
            }
        },
        closeSnackbar() {
            store.commit("setSnackbar", { message: "", show: false, color: colors.white})
        }
    },
}
</script>