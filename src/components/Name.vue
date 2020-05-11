<template>
        <v-card>
            <v-card-title >
                <v-row justify="center">
                    <h2 style="color:#1976d2">Enter Name</h2>
                </v-row>
            </v-card-title>
          <v-card-text>
            <v-form class="form-enterName" @submit.prevent="submit">
                <div class="form-label-group">
                    <v-text-field
                        id="name"
                        label="Name"
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
            <div class="text-center ma-2">
            <v-snackbar v-model="snackbar">
                {{ text }}
            <v-btn
                color= state.color
                text
                on:click="closeSnackbar"
            >
            Close
            </v-btn>
            </v-snackbar>
            </div>
        </v-card>
</template>

<script>
export default {
    
    data() {
        return {
            name: "",
        }
    },

    methods: {
        submit() {
            this.$emit('input', this.name);
        }
    }
}
</script>