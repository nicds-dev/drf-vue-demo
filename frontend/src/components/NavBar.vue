<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container fw-semibold">
            <button
                class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                aria-expanded="false" aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link to="/" :class="`nav-link ${$route.path === '/' ? 'active' : ''}`">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/about" :class="`nav-link ${$route.path === '/about' ? 'active' : ''}`">About</router-link>
                    </li>
                </ul>
                <form class="d-flex" role="search" @submit.prevent="submitForm" v-if="$route.path === '/'">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="searchText">
                    <button class="btn btn-outline-primary" type="submit" @click="getSearch" >Search</button>
                </form>
            </div>
        </div>
    </nav>
</template>

<script setup>
    import { ref, defineEmits } from 'vue'

    const searchText = ref('')
    const emmitSearch = defineEmits(['getSearchText'])

    const getSearch = () => {
        emmitSearch('getSearchText', searchText.value)
    }

</script>

<style scoped>
  .active {
    color: #0d6efd !important;
  }
</style>