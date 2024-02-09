<template>
  <div class="container">
    <NavBar v-if="$route.path != '/'" />
    <Navigation v-if="$route.path === '/about'" />
    <router-view/>
    <Footer />
  </div>
</template>

<script setup>
  import NavBar from '@/components/NavBar.vue';
  import Navigation from './components/Navigation.vue';
  import Footer from '@/components/Footer.vue';
</script>
