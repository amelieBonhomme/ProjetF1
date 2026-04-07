<template>
  <div class="generalLayout">
    <main id="accueil">
      <h2 class="circuit-title">Les circuits en Europe :</h2>
      <br>

      <div v-for="c in circuitsTries" :key="c.id_circuit" class="circuit-card">

        <h2 class="circuit-title">{{ c.nom_circuit }}</h2>

        <!-- Bouton like -->
        <button class="heart-btn" @click.stop="togglePrefereCircut(c.id_circuit)">
          <span v-if="prefere.includes(c.id_circuit)">❤️</span>
          <span v-else>🤍</span>
        </button>

        <div class="circuit-content">
          <img :src="c.image_circuit" alt="logo circuit" class="circuit-logo" />
          <p class="circuit-description">{{ c.description_circuit }}</p>
        </div>

        <a :href="c.lien_site" target="_blank" class="circuit-link">
          Voir le site officiel
        </a>

      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { getCircuit } from "@/services/api.js"
import { getPrefere, togglePrefere } from "@/services/prefereApi.js"

const circuit = ref([])
const prefere = ref([])

const user = JSON.parse(localStorage.getItem("user"))

onMounted(async () => {
  circuit.value = await getCircuit()
  prefere.value = await getPrefere(user.id_user)   // renvoie une LISTE
})

async function togglePrefereCircut(id_circuit) {
  await togglePrefere(user.id_user, id_circuit)
  prefere.value = await getPrefere(user.id_user)
}

const circuitsTries = computed(() => {
  if (!prefere.value || prefere.value.length === 0) return circuit.value

  return [
    ...circuit.value.filter(c => prefere.value.includes(c.id_circuit)),
    ...circuit.value.filter(c => !prefere.value.includes(c.id_circuit))
  ]
})
</script>
