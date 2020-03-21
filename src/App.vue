<template>
  <v-app>
    <v-content>
      <router-view>
        <router-link to="/login">Go to Login</router-link>
      </router-view>
       
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data() {
    return {
      routes: this.$router.options.routes,
    };
  },
  
};
</script>
