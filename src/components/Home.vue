<template>
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
</template>

<script>
import QrcodeVue from 'qrcode.vue'
//import Vue from 'vue';
let x = Math.ceil(Math.random()*10**16)

const QR = {
  components: {
    QrcodeVue,
  },

  data() {
    return {
      value: 'http://localhost:8080/attendance/'+x,
      size: 300,
    };
  },

  methods: {
        newQR(){
            x = Math.ceil(Math.random()*10**16);
            this.value = 'http://localhost:8080/'+x 
            console.log("x1: " + x)
        }
    },
  
};
export default QR;
</script>