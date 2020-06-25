<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="6">
        <QR>
        </QR>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { post } from "../requests"
import QR from '../components/QR'

export default {

    components: {
      QR
    },
    
    data() {
        return {
            //routes: this.$router.options.routes,
        }
    },

    

  /*  computed: {
      meetingID: this.$route.params.id
    }, */

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