<script setup>
import { RouterView, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import fondVideo from "@/assets/fond1.mp4"

import { useAuth } from "@/composables/useAuth.js"

const router = useRouter()

// ⭐ Une seule instance du composable
const { isLogged, loadUser, logout } = useAuth()

onMounted(() => {
  loadUser()
})

const logoutUser = () => {
  console.log("LOGOUT CLICKED")
  logout()
  router.push("/")
}
// Ajout pour le menu mobile
const isOpen = ref(false)
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}
</script>

<template>
  <nav class="navbar">
    <!-- <ul>
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/regles">Règles</router-link></li>
      <li><router-link to="/ecurie">Ecurie</router-link></li>
      <li><router-link to="/circuit">Circuit</router-link></li>
      <li><router-link to="/classement">Classement</router-link></li>
    </ul>
  </nav>
  <nav class="navbar"> -->

    <!-- Bouton hamburger (mobile uniquement) -->
    <button class="hamburger" @click="toggleMenu">
      ☰
    </button>

    <!-- Menu -->
    <ul :class="['nav-links', { open: isOpen }]">
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/regles">Règles</router-link></li>
      <li><router-link to="/ecurie">Ecurie</router-link></li>
      <li><router-link to="/circuit">Circuit</router-link></li>
      <li><router-link to="/classement">Classement</router-link></li>
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
    @click="logoutUser"
  >
    Déconnexion
  </button>

  <RouterView />
</template>
