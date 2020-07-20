<template>
    <v-container style="color:#a8dadc">
        <v-row align="center" justify="center">
                    <h1 style="color:#000000">Meetings</h1>
                </v-row>
            <v-row dense>
                <v-col cols="12">
                    <v-card
                        color="#E63946"
                        dark
                        @click="createNewMeeting"
                    >
                        <v-card-title class="headline">Create New Meeting</v-card-title>
                    </v-card>
                </v-col>
            </v-row>
            <v-row dense>
                <v-col cols="12">
                    <v-card
                        color="#457b9d"
                        dark
                        @click="viewPastMeetings"
                    >
                        <v-card-title class="headline">View Past Meetings</v-card-title>
                    </v-card>
                </v-col>
            </v-row>
    </v-container>
</template>

<script>
export default {
    name: "HomePage",

    methods: {
        createNewMeeting(){
            this.$router.push("/meeting/createMeeting")
        },
        viewPastMeetings() {
            this.$router.push("/meeting/pastMeetings")
        }
    }
}
</script>