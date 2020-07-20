<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="6">
        <History>
        </History>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import History from "../components/History"

export default {

    components: {
        History,
    },
    data() {
        return{
            name: ""
        }
    },
}
</script>