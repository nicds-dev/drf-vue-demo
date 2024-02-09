<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
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
                        <router-link to="/" class="nav-link">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/about" class="nav-link">About</router-link>
                    </li>
                </ul>
                <form class="d-flex" role="search" @submit.prevent="submitForm">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="searchText">
                    <button class="btn btn-outline-success" type="submit" @click="getSearch" >Search</button>
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