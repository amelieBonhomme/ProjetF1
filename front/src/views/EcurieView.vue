<template>
  <div class="generalLayout">

    <main id="accueil">
      <h1 class="titre">Les 10 écuries engagées en Formule 1</h1>

      <div class="bloc_club">
        <div 
          class="flip-card" 
          v-for="equipe in equipes" 
          :key="equipe.id_equipe"
        >
          <div class="flip-card-inner">

            <!-- FACE AVANT -->
            <div class="flip-card-front">
              <img :src="equipe.logo" alt="Logo">
              <h4 class="titre">{{ equipe.nom }}</h4>
            </div>

            <!-- FACE ARRIÈRE -->
            <div class="flip-card-back back-layout">

              <!-- ❤️ BOUTON FAVORI -->
              <button class="heart-btn" @click.stop="toggleFavoriEquipe(equipe.id_equipe)">
                <span v-if="favoris.includes(equipe.id_equipe)">❤️</span>
                <span v-else>🤍</span>
              </button>

              <div class="back-text">
                <p>{{ equipe.description }}</p>
              </div>

              <div class="back-image">
                <strong>Pilote principal :</strong> {{ equipe.pilote_principal }}
                <img :src="equipe.image_pilote" alt="Pilote">
                <br>
                <strong>Pilote Second :</strong> {{ equipe.pilote_second }}
                <img :src="equipe.image_pilote2" alt="Pilote">
              </div>

            </div>

          </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { getEquipes } from "@/services/api.js"
import { getFavoris, toggleFavori } from "@/services/favorisApi.js"

const equipes = ref([])
const favoris = ref([])

const user = JSON.parse(localStorage.getItem("user"))

onMounted(async () => {
  equipes.value = await getEquipes()
  favoris.value = await getFavoris(user.id_user)
})

async function toggleFavoriEquipe(id_equipe) {
  console.log("CLICK sur équipe :", id_equipe)

  const res = await toggleFavori(user.id_user, id_equipe)
  console.log("Réponse API toggle :", res)

  favoris.value = await getFavoris(user.id_user)
  console.log("Favoris mis à jour :", favoris.value)
}
</script>
