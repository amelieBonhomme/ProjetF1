<script setup>
import { RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

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

    <!-- BOUTON DÉCONNEXION -->
    <button 
      v-if="isLogged" 
      class="logout-btn"
      @click="logout"
    >
      Déconnexion
    </button>

    <ul>
      <li><a href="/"><img src="@/assets/nfl_logo.png" alt="Logo" /></a></li>
      <li><a href="accueil">Accueil</a></li>
      <li><a href="rules">Règles</a></li>
      <li><a href="">Stratégie</a></li>
      <li><a href="">Info club</a></li>
      <li><a href="">Classement</a></li>
    </ul>   
  </nav>

  <video autoplay muted loop id="background-video">
    <source src="@/assets/fond1.mp4" type="video/mp4">
    Votre navigateur ne supporte pas la vidéo HTML5.
  </video>

  <RouterView />
</template>

<style>
.navbar {
  position: fixed;
  max-width: 60%;
  background-color: #5a3a33;
  opacity: 0.9;
  color: rgb(255, 255, 255);
  top: 0;
  left: 0;
  width: 100%;
  padding: 1% 0;
  text-align: center;
  border-radius: 30px;
  margin-left: 20%;
  margin-top: 1%;
  z-index: 10;
}

.navbar ul {
  display: flex;
  justify-content: center;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 9%;
}

.navbar li {
  display: flex;
  align-items: center;
  font-weight: bold;
  font-size: 20px;
}

.navbar li a img {
  width: 60px;
}

.navbar li a:hover {
  text-decoration: underline;
}

/* BOUTON DÉCONNEXION */
.logout-btn {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  background: #c8102e;
  color: white;
  border: none;
  padding: 8px 14px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.2s ease;
}

.logout-btn:hover {
  background: #a00d24;
  transform: translateY(-50%) scale(1.05);
}

#background-video {
  position: fixed;
  top: 0;
  left: 0;
  width: 99vw;
  height: 100vh;
  object-fit: cover;
  z-index: -1;
}
</style>
