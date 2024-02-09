<template>
  <NavBar @getSearchText="search" />
  <Navigation @getCatId="catId" />
  <section id="products">
    <div class="container">
      <div v-if="catReceived" class="text-center mb-3">
        <h3 class="mb-3">{{ catReceived }} Products</h3>
      </div>
      <div v-if="products.length === 0" class="alert alert-warning text-center" role="alert">
        <span v-if="textSearchRule">No products found with the name '<strong>{{ textSearchRule }}</strong>'.</span>
        <span v-else>No products available.</span>
      </div>
      <div class="row row-cols-1 row-cols-md-4 g-4">
        <div v-for="product in products" :key="product.id" class="col">
          <div class="card text-start">
            <img :src="product.image" class="card-img-top" alt="image of {{ product.name }}">
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <h6 class="card-subtitle mb-2 text-body-secondary">{{ product.category_name }}</h6>
              <span class="fs-5 fw-bold text-primary">${{ product.price }} USD</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
  import axios from 'axios'
  import Navigation from '@/components/Navigation.vue'
  import NavBar from '@/components/NavBar.vue'
  import { ref, onMounted } from 'vue'

  const products = ref([])
  const catReceived = ref(null)
  const textSearchRule = ref(null)

  const fetchData = (url) => {
    axios.get(url)
      .then((response) => {
        products.value = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const search = (textSearch) => {
    catReceived.value = null
    textSearchRule.value = textSearch;
    const url = textSearch ? `http://127.0.0.1:8000/api/products/?search=${textSearch}` : 'http://127.0.0.1:8000/api/products/';
    fetchData(url);
  };

  const catId = (catId, catName) => {
    textSearchRule.value = null
    catReceived.value = catName;
    const url = catId ? `http://127.0.0.1:8000/api/products/?category=${catId}` : 'http://127.0.0.1:8000/api/products/';
    fetchData(url);
  };

  onMounted(() => {
    fetchData('http://127.0.0.1:8000/api/products/');
  });
</script>

