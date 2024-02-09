<template>
    <section class="mt-5 text-center mx-auto">
        <h1>Welcome to our store</h1>
        <img class="img-fluid" :src="require('@/assets/img/header.jpg')" alt="">
        <div v-if="$route.path !== '/about'" class="d-flex flex-wrap gap-4 justify-content-center mt-3">
            <button v-for="category in categories" :key="category.id" type="button" class="btn btn-dark" @click="getCatId(category.id, category.name)">
                {{ category.name }}
            </button>
            <button type="button" class="btn btn-dark" @click="getCatId(null, null)">All</button>
            <hr class="col-12">
        </div>
    </section>
</template>

<script setup>
    import axios from 'axios'
    import { ref, defineEmits, onMounted } from 'vue'

    const categories = ref([])

    const emit = defineEmits(['getCatId'])

    const getCatId = (catId, catName) => {
        emit('getCatId', catId, catName)
    }
    
    onMounted(() => {
        axios.get('http://127.0.0.1:8000/api/categories/')
        .then((response) => {
            categories.value = response.data
        })
        .catch((error) => {
            console.log(error);
        })
    })
</script>