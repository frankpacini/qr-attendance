<template>
<v-container fluid>
    <v-container style="width:50%" v-if="this.name == ''">
        <Name  @input="(newName) => {name = newName}"  />
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
</template>

<script>

import Name from '../components/Name.vue'

export default {

    components: {
        Name
    },
    
    created() {
        console.log("This was created")
    },

    data() {
        return {
            name: ""
        }
    },

    methods:
    {
        reset(){
            console.log("This was pressed")
            this.name = ""
        }
    }
}
</script>