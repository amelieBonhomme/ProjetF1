<script setup>
  import { RouterView, useRouter } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import fondVideo from "@/assets/fond1.mp4"


  const router = useRouter()
  const isLogged = ref(false)

  onMounted(() => {
    isLogged.value = !!localStorage.getItem("user")
  })

  const logout = () => {
    localStorage.removeItem("user")
    isLogged.value = false
    router.push("/")   // retour à l'accueil
    window.location.reload() // recharge pour réactiver l’overlay
  }
</script>


<template>
  <nav class="navbar">
    <ul>
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/regles">Règles</router-link></li>
      <li><router-link to="/ecurie">Ecurie</router-link></li>
      <li><router-link to="/circuit">Circuit</router-link></li>
      <li><router-link to="/classement">Classement</router-link></li>
    </ul>
  </nav>


  <video autoplay muted loop id="background-video">
    <source :src="fondVideo" type="video/mp4">
  </video>
  <!-- BOUTON DÉCONNEXION -->
  <button 
    v-if="isLogged" 
    class="logout-btn"
    @click="logout"
  >
    Déconnexion
  </button>
  <RouterView />
</template>
