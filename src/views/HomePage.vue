<template>
    <v-container>
        <v-card @click="createNewMeeting"> 
            <v-card-actions>
                Create New Meeting
            </v-card-actions>
        </v-card>
        <v-card>
            <v-card-actions>
                View Past Meetings
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: "HomePage",

    methods: {
        createNewMeeting(){
            this.$router.push("/meeting/createMeeting")
        }
    }
}
</script>