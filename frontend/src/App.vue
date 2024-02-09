<template>
  <NavBar v-if="$route.path != '/'" />
  <Navigation v-if="$route.path === '/about'" />
  <router-view/>
  <Footer />
</template>

<script setup>
  import NavBar from '@/components/NavBar.vue';
  import Navigation from './components/Navigation.vue';
  import Footer from '@/components/Footer.vue';
</script>
