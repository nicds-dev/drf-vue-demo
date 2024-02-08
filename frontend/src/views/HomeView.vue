<template>
  <Navigation @getCatId="catId" />
  <div v-if="catReceived">
    <h3>{{ catReceived }} Products</h3>
  </div>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="product in products" :key="product.id" class="col">
        <div class="card text-center">
          <img :src="product.image" class="card-img-top" alt="image of {{ product.name }}">
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <h6 class="card-subtitle mb-2 text-body-secondary">{{ product.category_name }}</h6>
            <p class="card-text">{{ product.description }}</p>
          </div>
          <div class="card-footer text-danger">
            PRICE: {{ product.price }} USD
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import Navigation from '@/components/Navigation.vue'

export default {
  name: 'HomeView',
  components: {
    Navigation,
  },
  data() {
    return {
      products: [],
      catReceived: null
    }
  },
  methods: {
    catId(catId, catName) {
      this.catReceived = catName
      if (catId) {
        axios.get(`http://127.0.0.1:8000/api/products/?category=${catId}`)
        .then((response) => {
          this.products = response.data
        })
        .catch((error) => {
          console.log(error);
        })
      } else {
        axios.get('http://127.0.0.1:8000/api/products/')
        .then((response) => {
          this.products = response.data
        })
        .catch((error) => {
          console.log(error);
        })
      }
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/products/')
    .then((response) => {
      this.products = response.data
    })
    .catch((error) => {
      console.log(error);
    })
  }
}
</script>

<style scoped>

</style>
