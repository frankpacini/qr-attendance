<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="6">
        <Home>
        </Home>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { post } from "../requests"
import Home from '../components/Home'

export default {

    components: {
      Home
    },
    
    data() {
        return {
            //routes: this.$router.options.routes,
        }
    },

    methods: {
        submit(){
            if(this.email != "" && this.password != "") {
                post('/auth/login', {
                    email: this.email,
                    password: this.password
                })
                .then(res => {
                    console.log("Logged In ")
                    console.log(res)
                })
            }
        }
    },
}
</script>