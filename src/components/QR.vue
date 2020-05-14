<template>
  <v-container>
    <v-container v-if="this.validMeeting == 1">
      <v-card>
        <v-card-title >
            <v-row justify="center">
                <qrcode-vue :value="value" :size="size" level="H"></qrcode-vue>
            </v-row>
        </v-card-title>
        <v-card-actions>
          <v-row justify="center">
          <v-btn tile color="blue" v-on:click="newQR" width="95%" type="submit">Make New QR</v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container v-if="this.validMeeting == 2">
      <h1>Not a meeting</h1>
    </v-container>
  </v-container>
</template>

<script>
import QrcodeVue from 'qrcode.vue'
import api from "../api.js";
//import Vue from 'vue';

const QR = {
  components: {
    QrcodeVue,
  },

  data() {
    return {
      size: 300,
      id: "",
      validMeeting: 0, //0 means loading, 1 means valid 2 means not valid
      meetingName: "",
      meetingActive: true, //if meeting is still open or not
    };
  },

  computed: {
    value: function () {
      return 'http://localhost:8080/attendance/' + this.id
    }
  },

  created() {
    this.id = this.$route.params.id
    console.log("Created")
    //method to check that it is actually a meeting id
    api.checkMeeting(this.id).then(res => {
      console.log("Valid meeting id" + res)
      this.validMeeting = 1
      console.log(res)
      this.meetingName = res.data.name
      this.id = res.data.meetingID
      this.meetingActive = res.data.active
    }).catch(err => {
      this.validMeeting = 2
      console.log("Not a valid meeting" + err)
    })
  },


  methods: {
        newQR(){
        }
    },
  
};
export default QR;
</script>