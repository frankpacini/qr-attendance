<template>
        <v-card>
            <v-card-title>
                <v-row justify="center">
                    <h2 style="color:#1d3557">Enter Name</h2>
                </v-row>
            </v-card-title>
          <v-card-text>
            <v-form class="form-enterName" @submit.prevent="submit">
                <div class="form-label-group">
                    <v-text-field
                        id="name"
                        label="Please enter your full name"
                        autofocus
                        v-model="name"
                    > </v-text-field>
                </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
              <v-row justify="center">
              <v-btn tile color="#e63946" v-on:click="submit" width="95%" type="submit">Submit</v-btn>
              </v-row>
          </v-card-actions>
        </v-card>
</template>

<script>

import api from "../api.js";
import {setCookie} from "../js/authentication.js";
export default {

    props: {
        userID: String
    },

    data() {
        return {
            name: "",
            meetingID: "",
        }
    },

    created(){
        this.meetingID = this.$route.params.id
    },

    methods: {
        submit() {
            var userIDresult;
            api.setName(this.meetingID, this.name, this.userID).then(res => {
                console.log("Signed in" + res)
                userIDresult = res.data.userID
                console.log(res)
                this.$emit('input', this.name);
                this.$emit('createdAttendee', userIDresult)
                setCookie("name", this.name, 60);
                setCookie("userID", userIDresult, 60);
                }).catch(err => {
                console.log(err)
            })
            
        }
    }
}
</script>