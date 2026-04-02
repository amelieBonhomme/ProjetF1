<template>
  <div class="page">
    <div class="background-image"></div>
    <div class="background-overlay"></div>

    <div class="layout">
      <header class="topbar">
        <div class="brand">
          <span class="logo">NFL</span>
          <span class="year">EST. 1920</span>
        </div>


        <div class="nav-right">
          <template v-if="isLogged">
            <span class="user-badge">Connecté</span>
            <button class="logout-btn" @click="handleLogout">Déconnexion</button>
          </template>

          <template v-else>
            <button class="login-btn" @click="isRegistering = false">Connexion</button>
          </template>
        </div>
      </header>

      <main class="hero">
        <div class="hero-left">
          <h1 class="title">
            FOOTBALL<br />
            <span>WITHOUT</span><br />
            MERCY
          </h1>

          <div class="info">
            <p>
              Un sport brutal, stratégique et spectaculaire.
              Ici, chaque mètre se gagne.
            </p>

            <div class="actions">
              <router-link to="/rules" class="btn">Rules</router-link>
              <router-link to="/gallery" class="btn ghost">Gallery</router-link>
            </div>
          </div>
        </div>

        <div class="image-zone">
          <img src="@/assets/nfl_ac.png" alt="NFL" />
        </div>
      </main>

      <section class="intro-card">
        <h2>Bienvenue sur l’univers du football américain</h2>
        <p>
          Découvre les règles, les équipes, les galeries et le classement
          dans une interface immersive inspirée de l’univers NFL.
        </p>
      </section>

      <div v-if="!isLogged" class="overlay">
        <div class="login-box">
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
  error.value = "";

  const response = await fetch("http://localhost:8000/api/login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      login: login.value,
      mdp: mdp.value,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    error.value = data.error || "Erreur de connexion";
  } else {
    localStorage.setItem("user", JSON.stringify(data));
    isLogged.value = true;
  }
};

const handleRegister = async () => {
  error.value = "";

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
    error.value = data.error || "Erreur d'inscription";
  } else {
    localStorage.setItem("user", JSON.stringify(data));
    isLogged.value = true;
  }
};

const handleLogout = () => {
  localStorage.removeItem("user");
  isLogged.value = false;
};
</script>

<style scoped>
.page {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  color: white;
  font-family: "Inter", system-ui, sans-serif;
}

.background-image {
  position: fixed;
  inset: 0;
  background: url("@/assets/fond1.jpg") center center / cover no-repeat;
  z-index: -2;
}

.background-overlay {
  position: fixed;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(0, 0, 0, 0.45) 0%, rgba(0, 0, 0, 0.75) 100%);
  z-index: -1;
}

.layout {
  min-height: 100vh;
  padding: 2rem;
}

/* NAVBAR */
.topbar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding: 1rem 1.5rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  background: rgba(10, 10, 10, 0.55);
  backdrop-filter: blur(14px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  min-width: 160px;
}

.logo {
  font-size: 1.3rem;
  font-weight: 900;
  letter-spacing: 0.18em;
  color: white;
}

.year {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.55);
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
  justify-content: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.78);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 600;
  padding: 0.55rem 0.9rem;
  border-radius: 999px;
  transition: all 0.25s ease;
}

.nav-link:hover {
  color: white;
  background: rgba(255, 255, 255, 0.08);
}

.nav-link.router-link-exact-active {
  color: white;
  background: rgba(200, 16, 46, 0.18);
  box-shadow: inset 0 0 0 1px rgba(200, 16, 46, 0.35);
}

.nav-right {
  min-width: 160px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 0.75rem;
}

.user-badge {
  padding: 0.45rem 0.85rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: white;
  font-size: 0.85rem;
  font-weight: 600;
}

.login-btn,
.logout-btn {
  border: none;
  border-radius: 999px;
  padding: 0.7rem 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}

.login-btn {
  background: white;
  color: black;
}

.login-btn:hover,
.logout-btn:hover {
  transform: translateY(-2px);
}

.logout-btn {
  background: #c8102e;
  color: white;
  box-shadow: 0 8px 20px rgba(200, 16, 46, 0.25);
}

.logout-btn:hover {
  box-shadow: 0 10px 24px rgba(200, 16, 46, 0.35);
}

/* HERO */
.hero {
  min-height: calc(100vh - 150px);
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 3rem;
}

.hero-left {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.title {
  margin: 0;
  font-size: clamp(3.5rem, 8vw, 8rem);
  font-weight: 900;
  line-height: 0.92;
  letter-spacing: -0.04em;
  text-transform: uppercase;
}

.title span {
  color: #c8102e;
}

.info {
  max-width: 480px;
}

.info p {
  margin: 0;
  font-size: 1.12rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.8);
}

.actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn {
  padding: 0.9rem 1.8rem;
  border-radius: 999px;
  background: white;
  color: black;
  text-decoration: none;
  font-weight: 700;
  letter-spacing: 0.04em;
  transition: all 0.2s ease;
}

.btn:hover {
  transform: translateY(-3px);
}

.btn.ghost {
  background: transparent;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.4);
}

.image-zone {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-zone img {
  width: min(100%, 520px);
  max-height: 78vh;
  object-fit: contain;
  filter: drop-shadow(0 25px 50px rgba(0, 0, 0, 0.45));
}

/* INTRO CARD */
.intro-card {
  max-width: 720px;
  margin-top: -2rem;
  padding: 1.5rem;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.intro-card h2 {
  margin: 0 0 0.8rem;
  font-size: 1.5rem;
}

.intro-card p {
  margin: 0;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.82);
}

/* OVERLAY */
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.68);
  backdrop-filter: blur(5px);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.login-box {
  width: 100%;
  max-width: 360px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 2rem;
  border-radius: 20px;
  text-align: center;
  backdrop-filter: blur(10px);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.35);
}

.login-box h2 {
  margin-bottom: 1.2rem;
  color: white;
}

.login-box form {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}

.login-box input {
  width: 100%;
  padding: 0.9rem 1rem;
  border: none;
  border-radius: 10px;
  outline: none;
  background: rgba(255, 255, 255, 0.92);
}

.login-box button[type="submit"] {
  width: 100%;
  padding: 0.9rem;
  background: #c8102e;
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(200, 16, 46, 0.4);
}

.login-box button[type="submit"]:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(200, 16, 46, 0.55);
}

.switch {
  margin-top: 1rem;
  cursor: pointer;
  color: #ddd;
}

.switch span {
  color: #ff5b74;
  font-weight: 700;
}

.error {
  margin-top: 1rem;
  color: #ff7d7d;
}

.sexe-group {
  display: flex;
  justify-content: space-between;
  gap: 0.8rem;
  flex-wrap: wrap;
  text-align: left;
  font-size: 0.95rem;
}

.sexe-group label {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: white;
}

@media (max-width: 900px) {
  .topbar {
    flex-direction: column;
    align-items: stretch;
  }

  .brand,
  .nav-right {
    min-width: unset;
    justify-content: center;
  }

  .nav-links {
    flex-wrap: wrap;
  }

  .hero {
    grid-template-columns: 1fr;
    text-align: center;
    padding-top: 1rem;
  }

  .hero-left {
    align-items: center;
  }

  .info {
    max-width: 100%;
  }

  .actions {
    justify-content: center;
    flex-wrap: wrap;
  }

  .image-zone img {
    max-height: 50vh;
  }

  .layout {
    padding: 1rem;
  }
}
</style>