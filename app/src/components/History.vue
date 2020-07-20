<template>
  <v-container fluid>
    <v-card v-for="(meeting, i) in meetings"
      :key="i">
      <v-card-title class="headline">
        <h2 style="color:#1976d2">{{"\u0022" + meeting['name'] + "\u0022"}}</h2>
      </v-card-title>
      <v-card-actions>
        <v-expansion-panels
          :multiple="true"
          :hover="true"
        >
          <v-expansion-panel>
            <v-expansion-panel-header>Attendees</v-expansion-panel-header>
            <v-expansion-panel-content>
              Hi
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-card-actions>
    </v-card> 
  </v-container>
</template>

<script>
import api from "../api.js";
//import Vue from 'vue';

const History = {
  components: {
  },

  data() {
    return {
      meetings: {},
      meeting_ids: [],
      attendees: [],
      attendee_ids: []
    };
  },

  created() {
    console.log("Created")
    api.getAllMeetings().then(res => {
      this.meeting_ids = res.data.ids
      this.meetings = res.data.dict
      //this.getMeetings()
    }).catch(err => {
      console.log("Could not retrieve ids: " + err)
    })
  },

  mounted() {
    // window.setInterval(() => {
    //     console.log(this.meeting_ids)
    //     this.getMeetings()
    //   }, 5000)
  },


  methods: {
        getMeetings() {
          for(let id in this.meetings_ids) {
            api.checkMeeting(this.meeting_ids[id]).then(res => {
              //console.log(res.data)
              if(this.meetings.length == id)
                this.meetings.push(res.data)
              else
                this.meetings[id] = res.data
            }).catch(err => {
              console.log("No such meeting " + err)
            })
          }
        },
        close(id) {
          api.closeMeeting(id).catch(err => {
            console.log("Close failed " + err)
          })
        }
    },
  
};
export default History;
</script>