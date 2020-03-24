<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="6">
        <Login/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { post } from "../requests"
import Login from '../components/Login'

export default {

    components: { 
      Login
    },
    
    data() {
        return {
            email: "",
            password: "",
            visibibilty: false
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