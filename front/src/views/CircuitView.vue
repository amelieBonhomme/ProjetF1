<template>
  <div class="generalLayout">
    <main id="accueil">
    <h2 class="circuit-title">Les circuit en Europe : </h2>
    <br>

      <div v-for="c in circuit" :key="c.id_circuit" class="circuit-card">

        <!-- Nom du circuit -->
        <h2 class="circuit-title">{{ c.nom_circuit }}</h2>

        <!-- Logo + Description -->
        <div class="circuit-content">
          <img :src="c.image_circuit" alt="logo circuit" class="circuit-logo" />

          <p class="circuit-description">
            {{ c.description_circuit }}
          </p>
        </div>

        <!-- Lien vers le site -->
        <a :href="c.lien_site" target="_blank" class="circuit-link">
          Voir le site officiel
        </a>

      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { getCircuit } from "@/services/api.js"

const circuit = ref([])

onMounted(async () => {
  circuit.value = await getCircuit()
})
</script>