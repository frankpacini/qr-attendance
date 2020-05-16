<template>
    <v-container fluid>
        <v-container  v-if="this.valid == 1">
            <v-container style="width:50%" v-if="this.name == ''">
                <Name v-bind:userID="this.userID" @input="(newName) => {name = newName}" @createdAttendee="(newUserID) => {userID = newUserID}"  />
            </v-container>

            <v-container v-if="this.name != ''">
                <v-card>
                    <v-card-title>
                        Congratulations. You are signed in as {{ this.name }}. 
                    </v-card-title>
                    <v-card-subtitle @click="reset">
                        <v-btn>  Not You? </v-btn>
                    </v-card-subtitle>
                </v-card>
            </v-container>
        </v-container>
        <v-container v-if="this.valid == 2">
            <h1>Not a valid attendance link</h1>
        </v-container>
        <v-container v-if="this.valid == 3">
            <h1>Link is no longer active</h1>
        </v-container>
    </v-container>
</template>

<script>

import Name from '../components/Name.vue'
import api from "../api.js";
import {getCookie, deleteCookie} from "../js/authentication.js";

export default {

    components: {
        Name
    },
    
    created() {
        this.id = this.$route.params.id
        console.log("Cookie: " + getCookie("name") + " " + getCookie("userID"))
        api.checkMeeting(this.id).then(res => {
        console.log("Valid meeting id" + res)
        if (res.data["active"]) {
            this.valid = 1
            console.log("Active meeting")
            if(this.name != "") {
                api.setName(this.id, this.name, this.userID).catch(err => {
                    console.log(err)
                })
            }
        }
        else {
            this.valid = 3
            console.log("Inactive meeting")
        }
        console.log(res)
        }).catch(err => {
        this.valid = 2
        console.log("Not a valid meeting" + err)
        })
    },

    data() {
        return {
            name: getCookie("name") ? getCookie("name") : "",
            id: "",
            userID: getCookie("userID") ? getCookie("userID") : "",
            valid: 0 //0 is loading, 1 is valid, 2 is invalid
        }
    },

    methods:
    {
        reset(){
            console.log("This was pressed")
            this.name = ""
            deleteCookie("name")
        }
    }
}
</script>