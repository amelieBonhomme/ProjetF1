<template>
  <div class="generalLayout">

    <main id="accueil">
      <h1 class="titre">Les 10 écuries engagées en Formule 1</h1>
      <p class="intro-f1">
        Le Championnat du Monde de Formule 1 réunit chaque saison <strong>10 écuries</strong>, 
        un nombre fixé par la FIA afin de garantir un niveau de compétition élevé, 
        une stabilité financière et une gestion optimale du plateau.  
        Chaque écurie engage <strong>deux pilotes</strong>, soit un total de 20 concurrents 
        qui s’affrontent sur les circuits du monde entier : Europe, Asie, Amériques, Moyen‑Orient.
      </p>
      <br>

      <p class="intro-f1">
        Ces 10 équipes représentent l’élite du sport automobile. Elles conçoivent leurs propres 
        monoplaces, développent leurs moteurs ou collaborent avec des motoristes partenaires, 
        et disposent d’infrastructures technologiques parmi les plus avancées au monde.
      </p>
      <br>

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
      <h1 class="titre">Une 11ᵉ équipe bientôt ?</h1>
      <p>
        Ces dernières années, <strong>Andretti Cadillac</strong> a tenté d’entrer en Formule 1.
        La <strong>FIA</strong> a validé leur candidature, mais la <strong>F1</strong> a refusé leur arrivée
        pour le moment.  
      </p>
      <p>
        Si la situation évolue, le plateau pourrait passer à <strong>11 écuries</strong> dans le futur,
        mais ce n’est pas le cas aujourd’hui.
      </p>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { getEquipes } from "@/services/api.js"

const equipes = ref([])

onMounted(async () => {
  equipes.value = await getEquipes()
})
</script>

