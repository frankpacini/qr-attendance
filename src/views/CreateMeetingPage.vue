<template>
    <v-container>
        <v-card>
            <v-card-title >
                <v-row justify="center">
                    <h2 style="color:#1976d2">Enter Name of Meeting</h2>
                </v-row>
            </v-card-title>
          <v-card-text>
            <v-form class="form-enterName" @submit.prevent="submit">
                <div class="form-label-group">
                    <v-text-field
                        id="name"
                        label="Name of Meeting"
                        autofocus
                        v-model="name"
                    > </v-text-field>
                </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
              <v-row justify="center">
              <v-btn tile color="success" v-on:click="submit" width="95%" type="submit">Submit</v-btn>
              </v-row>
          </v-card-actions>
        </v-card>
    </v-container>
</template>


<script>

import api from "../api";
import router from "../router"
export default {
    
    


    data() {
        return{
            name: ""
        }
    },

    methods: {
        submit(){
            console.log("This runs")
            //post function that creates a meeting
            api.createMeeting(this.name).then(res => {
                    console.log("Created Meeting")
                    var meetingID = res.data["meetingID"]
                    router.push(meetingID)
                })

            
            //should return meeting id  
            
        }
    }
}
</script>