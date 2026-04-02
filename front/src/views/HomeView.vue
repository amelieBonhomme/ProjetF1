<template>
  <div class="layout">
    <header class="topbar">
      <span class="logo">NFL</span>
      <span class="year">EST. 1920</span>
    </header>

    <main class="hero">
      <h1 class="title">
        FOOTBALL<br />
        <span>WITHOUT</span><br />
        MERCY
      </h1>

      <div class="image-zone">
        <img src="../assets/nfl_ac.png" alt="NFL" />
      </div>

      <div class="info">
        <p>Un sport brutal, stratégique et spectaculaire. Ici, chaque mètre se gagne.</p>

        <div class="actions">
          <router-link to="/rules" class="btn"> Rules </router-link>
          <router-link to="/gallery" class="btn ghost"> Gallery </router-link>
        </div>
      </div>
    </main>

    <!-- OVERLAY -->
    <div v-if="!isLogged" class="overlay">
      <div class="login-box">

        <!-- FORMULAIRE DE CONNEXION -->
        <div v-if="!isRegistering">
          <h2>Connexion</h2>

          <form @submit.prevent="handleLogin">
            <input type="text" placeholder="Login" v-model="login" required />
            <input type="password" placeholder="Mot de passe" v-model="mdp" required />
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
              <label>
                <input type="radio" value="H" v-model="regSexe" />
                Homme
              </label>

              <label>
                <input type="radio" value="F" v-model="regSexe" />
                Femme
              </label>

              <label>
                <input type="radio" value="X" v-model="regSexe" />
                Autre
              </label>
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
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const isLogged = ref(false);
const isRegistering = ref(false);

const login = ref("");
const mdp = ref("");
const error = ref("");

const regLogin = ref("");
const regMdp = ref("");
const regNom = ref("");
const regPrenom = ref("");
const regSexe = ref("");
const regDate = ref("");
const regMail = ref("");

onMounted(() => {
  const user = localStorage.getItem("user");
  isLogged.value = !!user;
});

const handleLogin = async () => {
  const response = await fetch("http://localhost:8000/api/login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ login: login.value, mdp: mdp.value }),
  });

  const data = await response.json();

  if (!response.ok) {
    error.value = data.error;
  } else {
    localStorage.setItem("user", JSON.stringify(data));
    isLogged.value = true;
  }
};

const handleRegister = async () => {
  const response = await fetch("http://localhost:8000/api/register/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      login: regLogin.value,
      mdp: regMdp.value,
      nom: regNom.value,
      prenom: regPrenom.value,
      sexe: regSexe.value,
      date_naissance: regDate.value,
      mail: regMail.value,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    error.value = data.error;
  } else {
    // Auto-login après inscription
    localStorage.setItem("user", JSON.stringify(data));
    isLogged.value = true;
  }
};
</script>

<style>
/* GLOBAL */
.layout {
  background-color: rgba(0, 0, 0, 0.849);
  min-height: 100vh;
  color: white;
  font-family: 'Inter', system-ui, sans-serif;
  padding: 2rem;
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);
  position: relative;
}

/* TOPBAR */
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
  letter-spacing: 2px;
  opacity: 0.8;
}

/* HERO */
.hero {
  margin-top: 4rem;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  grid-template-rows: auto auto;
  gap: 3rem;
}

/* TITRE */
.title {
  grid-column: 1 / 2;
  font-size: clamp(4rem, 8vw, 8rem);
  font-weight: 900;
  line-height: 0.95;
  text-transform: uppercase;
}

.title span {
  color: #c8102e;
}

/* IMAGE */
.image-zone {
  grid-column: 2 / 3;
  grid-row: 1 / 3;
  position: relative;
}

.image-zone img {
  width: 100%;
  object-fit: cover;
  filter: grayscale(100%) contrast(120%);
  mix-blend-mode: lighten;
  border-radius: 20rem;
}

/* TEXTE */
.info {
  max-width: 420px;
}

.info p {
  font-size: 1.1rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.75);
}

/* ACTIONS */
.actions {
  display: flex;
  gap: 1.5rem;
  margin-top: 2rem;
}

/* BOUTONS */
.btn {
  padding: 0.8rem 2rem;
  background: white;
  color: black;
  font-weight: 700;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: transform 0.2s ease;
}

.btn:hover {
  transform: translateY(-3px);
}

.btn.ghost {
  background: transparent;
  color: white;
  border: 1px solid white;
}

/* OVERLAY */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(4px);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* FORMULAIRE */
.login-box {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 12px;
  width: 320px;
  text-align: center;
  backdrop-filter: blur(6px);
}

.login-box h2 {
  margin-bottom: 1rem;
  color: white;
}

.login-box input {
  width: 100%;
  padding: 0.8rem;
  margin-bottom: 1rem;
  border: none;
  border-radius: 6px;
}

.login-box button {
  width: 100%;
  padding: 0.8rem;
  background: #c8102e;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(200, 16, 46, 0.4);
}

.login-box button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(200, 16, 46, 0.6);
}

.login-box button:active {
  transform: scale(0.95);
  box-shadow: 0 2px 8px rgba(200, 16, 46, 0.3);
}

.switch {
  margin-top: 1rem;
  cursor: pointer;
  color: #ddd;
}

.switch span {
  color: #c8102e;
  font-weight: bold;
}

.error {
  margin-top: 1rem;
  color: #ff6b6b;
}
.sexe-group {
  display: flex;
}
</style>
