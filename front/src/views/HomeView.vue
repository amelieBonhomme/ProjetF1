<template>
  <img class ="carte"  src="https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-0.png" alt="carte" />
  <div class="layout">

    <main id="accueil">
      <h1 class="titre">🏎️ Qu’est-ce que la Formule 1 ?</h1>
      <p>
        <h4>
          La Formule 1 est la discipline reine du sport automobile mondial. Elle oppose des écuries
          internationales qui conçoivent des monoplaces ultra‑technologiques capables d’atteindre plus de
          350 km/h. Chaque course, appelée “Grand Prix”, se déroule sur des circuits mythiques à travers
          le monde. L’objectif est simple : terminer la saison avec le plus de points pour devenir
          Champion du Monde.
        </h4>
      </p>

      <div class="paragraphe">
        <li><h4>Les pilotes marquent des points selon leur position à l’arrivée (25 points pour le vainqueur).</h4></li>
        <li><h4>Un point supplémentaire est attribué au pilote réalisant le meilleur tour en course.</h4></li>
        <li><h4>Les écuries cumulent les points de leurs deux pilotes pour le Championnat Constructeurs.</h4></li>
      </div>

      <h1 class="titre">Principes fondamentaux :</h1>
      <div class="paragraphe">
        <li><h4>Chaque Grand Prix se déroule sur un week‑end : essais libres, qualifications, puis course.</h4></li>
        <li><h4>Les qualifications déterminent l’ordre de départ selon le meilleur temps au tour.</h4></li>
        <li><h4>Les monoplaces sont régies par un règlement technique strict défini par la FIA.</h4></li>
        <li><h4>Les arrêts aux stands (changement de pneus) sont essentiels pour la stratégie de course.</h4></li>
        <li><h4>La sécurité est une priorité absolue : halo, combinaisons ignifugées, crash-tests, etc.</h4></li>
      </div>

      <h1 class="titre">Organisation du championnat :</h1>
      <p>
        Le Championnat du Monde de Formule 1 est une compétition internationale organisée par la FIA.
        Il se compose d’une vingtaine de courses réparties sur plusieurs continents. Chaque écurie
        participe avec deux pilotes, et toutes affrontent les mêmes circuits, du Moyen‑Orient à l’Europe,
        en passant par l’Asie et les Amériques.
      </p>

      <p>
        Contrairement aux sports structurés en conférences ou divisions, la F1 fonctionne comme un
        championnat unique où toutes les équipes s’affrontent à chaque Grand Prix. La saison se conclut
        par la remise de deux titres prestigieux : le Champion du Monde Pilotes et le Champion du Monde
        Constructeurs.
      </p>
      <h1 class = "titre">Vidéo introductive :</h1>
      <div class="video-container">
        <iframe
          src="https://www.youtube.com/embed/tO0Zti6af0g"
          title="Vidéo football américain"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen>
        </iframe>
      </div>
      </main>
  </div>
  <!-- OVERLAY visible seulement si pas connecté -->
  <div v-if="!isLogged" class="overlay">
    <div class="login-box">

      <!-- FORMULAIRE DE CONNEXION -->
      <div v-if="!isRegistering">
        <h2>Connexion</h2>

        <form @submit.prevent="handleLogin">
          <input type="text" placeholder="Login" v-model="loginField" required />
          <input type="password" placeholder="Mot de passe" v-model="mdpField" required />
          <button type="submit">Se connecter</button>
        </form>

        <p v-if="error" class="error">{{ error }}</p>

        <p class="switch" @click="isRegistering = true">
          Pas de compte ? <span>Inscription</span>
        </p>
      </div>

      <!-- FORMULAIRE D'INSCRIPTION -->
      <div v-else>
        <h2>Inscription</h2>

        <form @submit.prevent="handleRegister">
          <input type="text" placeholder="Login" v-model="regLogin" required />
          <input type="password" placeholder="Mot de passe" v-model="regMdp" required />

          <input type="text" placeholder="Nom" v-model="regNom" required />
          <input type="text" placeholder="Prénom" v-model="regPrenom" required />

          <div class="sexe-group">
            <label><input type="radio" value="H" v-model="regSexe" /> Homme</label>
            <label><input type="radio" value="F" v-model="regSexe" /> Femme</label>
            <label><input type="radio" value="X" v-model="regSexe" /> Autre</label>
          </div>

          <input type="date" v-model="regDate" required />
          <input type="email" placeholder="Email" v-model="regMail" required />

          <button type="submit">Créer un compte</button>
        </form>

        <p v-if="error" class="error">{{ error }}</p>

        <p class="switch" @click="isRegistering = false">
          Déjà un compte ? <span>Connexion</span>
        </p>
      </div>

    </div>
  </div>

</template>

<script setup>
import { ref, onMounted } from "vue"
import { useAuth } from "@/composables/useAuth.js"

const {
  isLogged,
  error,
  login,
  register,
  loadUser
} = useAuth()

// Champs du formulaire
const loginField = ref("")
const mdpField = ref("")
const isRegistering = ref(false)

const regLogin = ref("")
const regMdp = ref("")
const regNom = ref("")
const regPrenom = ref("")
const regSexe = ref("")
const regDate = ref("")
const regMail = ref("")

onMounted(() => {
  loadUser()
})

const handleLogin = () => {
  login(loginField.value, mdpField.value)
}

const handleRegister = () => {
  register({
    login: regLogin.value,
    mdp: regMdp.value,
    nom: regNom.value,
    prenom: regPrenom.value,
    sexe: regSexe.value,
    date_naissance: regDate.value,
    mail: regMail.value,
  })
}
</script>
