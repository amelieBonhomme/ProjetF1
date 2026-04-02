<script setup>
import { RouterView, RouterLink, useRouter } from "vue-router";
import { ref, onMounted } from "vue";

const router = useRouter();
const isLogged = ref(false);
const currentUser = ref(null);

onMounted(() => {
  const user = localStorage.getItem("user");
  isLogged.value = !!user;
  currentUser.value = user ? JSON.parse(user) : null;
});

const logout = () => {
  localStorage.removeItem("user");
  isLogged.value = false;
  currentUser.value = null;
  router.push("/");
};
</script>

<template>
  <div class="app-shell">
    <div id="background-image"></div>
    <div class="background-overlay"></div>

    <nav class="navbar">
      <div class="nav-left">
        <RouterLink to="/" class="brand">
          <img src="@/assets/nfl_logo.png" alt="Logo NFL" class="brand-logo" />
          <div class="brand-text">
            <span class="brand-title">NFL FRANCE</span>
            <span class="brand-subtitle">EST. 1920</span>
          </div>
        </RouterLink>
      </div>

      <div class="nav-center">
        <RouterLink to="/" class="nav-link">Accueil</RouterLink>
        <RouterLink to="/rules" class="nav-link">Règles</RouterLink>
        <RouterLink to="/clubs" class="nav-link">Info club</RouterLink>
        <RouterLink to="/classement" class="nav-link">Classement</RouterLink>
      </div>

      <div class="nav-right">
        <template v-if="isLogged">
          <span class="user-badge">
            {{ currentUser?.login || "Connecté" }}
          </span>

          <button class="logout-btn" @click="logout">
            Déconnexion
          </button>
        </template>

        <template v-else>
          <RouterLink to="/" class="login-link">
            Connexion
          </RouterLink>
        </template>
      </div>
    </nav>

    <main class="page-content">
      <RouterView />
    </main>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

html,
body,
#app {
  margin: 0;
  min-height: 100%;
  font-family: "Inter", system-ui, sans-serif;
}

.app-shell {
  position: relative;
  min-height: 100vh;
  color: white;
}

#background-image {
  position: fixed;
  inset: 0;
  z-index: -2;
  background: url("@/assets/fffa.jpg") no-repeat center center;
  background-size: cover;
}

.background-overlay {
  position: fixed;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(
      180deg,
      rgba(0, 0, 0, 0.42) 0%,
      rgba(0, 0, 0, 0.72) 100%
    );
}

.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  width: min(1200px, calc(100% - 2rem));
  margin: 1rem auto 0;
  padding: 0.95rem 1.25rem;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 1rem;
  border-radius: 24px;
  background: rgba(16, 12, 12, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.28);
}

.nav-left {
  display: flex;
  align-items: center;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
  color: white;
}

.brand-logo {
  width: 52px;
  height: 52px;
  object-fit: contain;
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.1;
}

.brand-title {
  font-size: 0.98rem;
  font-weight: 800;
  letter-spacing: 0.12em;
}

.brand-subtitle {
  font-size: 0.72rem;
  color: rgba(255, 255, 255, 0.58);
  letter-spacing: 0.18em;
}

.nav-center {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.55rem;
  flex-wrap: wrap;
}

.nav-link {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.82);
  font-weight: 600;
  font-size: 0.96rem;
  padding: 0.7rem 1rem;
  border-radius: 999px;
  transition: all 0.2s ease;
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
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0.7rem;
}

.user-badge {
  padding: 0.5rem 0.9rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: white;
  font-size: 0.88rem;
  font-weight: 600;
}

.logout-btn,
.login-link {
  border: none;
  text-decoration: none;
  border-radius: 999px;
  padding: 0.75rem 1rem;
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.logout-btn {
  background: #c8102e;
  color: white;
  box-shadow: 0 8px 20px rgba(200, 16, 46, 0.25);
}

.logout-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(200, 16, 46, 0.35);
}

.login-link {
  background: white;
  color: black;
}

.login-link:hover {
  transform: translateY(-2px);
}

.page-content {
  position: relative;
  z-index: 1;
  padding-top: 1rem;
}

@media (max-width: 980px) {
  .navbar {
    grid-template-columns: 1fr;
    justify-items: center;
    text-align: center;
  }

  .nav-left,
  .nav-right {
    justify-content: center;
  }

  .nav-center {
    justify-content: center;
  }
}

@media (max-width: 600px) {
  .navbar {
    width: calc(100% - 1rem);
    padding: 0.9rem;
    margin-top: 0.5rem;
  }

  .brand {
    flex-direction: column;
    gap: 0.4rem;
  }

  .brand-text {
    align-items: center;
  }

  .nav-link {
    padding: 0.6rem 0.85rem;
    font-size: 0.92rem;
  }

  .nav-right {
    flex-direction: column;
  }
}
</style>