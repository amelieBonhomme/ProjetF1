<template>
  <div class="page">
    <div class="background-overlay"></div>

    <img class="carte" src="@/assets/nfl_carte.png" alt="Carte des équipes" />
    <p class="legende">Carte des équipes en France</p>

    <div class="layout">
      <header class="topbar">
        <div class="brand">
          <span class="logo">NFL</span>
          <span class="year">EST. 1920</span>
        </div>

        <nav class="nav-links">
          <router-link to="/" class="nav-link">Accueil</router-link>
          <router-link to="/classement" class="nav-link">Classement</router-link>
          <router-link to="/rules" class="nav-link">Règles</router-link>
          <router-link to="/gallery" class="nav-link">Galerie</router-link>
        </nav>

        <div class="nav-right">
          <router-link to="/login" class="login-btn">Connexion</router-link>
        </div>
      </header>

      <main id="accueil" class="content">
        <section class="section">
          <h1 class="titre">🏈 Qu’est-ce que le football américain ?</h1>

          <p class="texte">
            Le football américain est un sport collectif qui oppose deux équipes de 11 joueurs sur un
            terrain rectangulaire de 100 yards (environ 91 mètres) de long. Contrairement au football
            européen — où l’objectif est de faire circuler un ballon rond au pied pour marquer dans un but —
            le football américain vise à faire progresser un ballon ovale vers la zone d’en-but adverse
            pour marquer des points.
          </p>

          <p class="texte">Ces points peuvent être obtenus par :</p>

          <ul class="paragraphe">
            <li>Touchdowns (6 points), obtenus en franchissant la ligne d’en-but avec le ballon.</li>
            <li>Field goals (3 points), réalisés au pied à travers des poteaux verticaux.</li>
            <li>Safeties (2 points), obtenus en plaquant un adversaire dans sa propre zone.</li>
          </ul>
        </section>

        <section class="section">
          <h1 class="titre">Principes fondamentaux</h1>

          <ul class="paragraphe">
            <li>Le ballon ne se joue pas principalement au pied, mais à la main.</li>
            <li>Le jeu est divisé en phases appelées “downs” : chaque équipe a quatre tentatives pour avancer de 10 yards.</li>
            <li>Le match se joue en quatre quarts-temps de 15 minutes, avec de nombreuses interruptions.</li>
            <li>Chaque équipe est composée de trois escouades spécialisées : attaque, défense et équipes spéciales.</li>
            <li>Le contact physique est intense : les plaquages sont autorisés, avec casque et épaulières.</li>
          </ul>
        </section>

        <section class="section">
          <h1 class="titre">Histoire des clubs</h1>

          <p class="texte">
            La France est découpée en deux conférences dans le championnat de football américain afin de
            garantir un équilibre sportif, une organisation plus fluide et des déplacements raisonnables
            pour les clubs.
          </p>

          <p class="texte">
            Le pays étant vaste et les équipes réparties sur tout le territoire, diviser la compétition
            en Conférence A (Nord / Est) et Conférence B (Sud / Ouest) permet de réduire les trajets,
            de limiter les coûts logistiques et de préserver la condition physique des joueurs.
          </p>

          <p class="texte">
            Cette structure facilite également la gestion du calendrier et crée une dynamique compétitive
            plus cohérente : chaque conférence regroupe des équipes géographiquement proches, qui
            s’affrontent régulièrement avant de se retrouver lors des phases finales nationales.
          </p>
        </section>

        <section class="section">
          <h3 class="titre">Conférence A</h3>

          <div class="bloc_club">
            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://molossesfootball.com/wp-content/uploads/2025/06/Logo-principal.png" alt="Molosses" />
                  <h4 class="card-title">Asnières-sur-Seine Molosses</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1992</p>
                  <p>Un des clubs franciliens les plus réguliers, reconnu pour sa formation et son identité locale forte.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://lescougars.fr/wp-content/uploads/2023/01/Logo_Cougars_Football_rmvd_bckg.png" alt="Cougars" />
                  <h4 class="card-title">Saint-Ouen-l’Aumône Cougars</h4>
                </div>
                <div class="flip-card-back">
                  <p>Fondés en 1989</p>
                  <p>Un des clubs les plus titrés de France, marqué par une vraie culture de performance.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Logo_des_Spartiates_d%27Amiens.png" alt="Spartiates" />
                  <h4 class="card-title">Amiens Spartiates</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1987</p>
                  <p>Une référence dans le Nord, connue pour son identité forte et son attachement à la ville d’Amiens.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/fr/f/fd/Logo_Vikings_Ascq.png" alt="Vikings" />
                  <h4 class="card-title">Villeneuve-d’Ascq Vikings</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1984</p>
                  <p>Un club historique du Nord, pilier du développement du football américain autour de Lille.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/fr/e/ed/Logo_Flash_La_Courneuve.png" alt="Flash" />
                  <h4 class="card-title">La Courneuve Flash</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1984</p>
                  <p>Le club le plus titré de France, référence absolue du football américain français.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://www.les-black-panthers.org/FootUS/wp-content/uploads/2024/01/Blason-Black-Panthers.png" alt="Black Panthers" />
                  <h4 class="card-title">Thonon Black Panthers</h4>
                </div>
                <div class="flip-card-back">
                  <p>Fondés en 1987</p>
                  <p>Un club prestigieux, reconnu pour son professionnalisme et ses performances européennes.</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="section">
          <h3 class="titre">Conférence B</h3>

          <div class="bloc_club">
            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/en/e/e1/Ours_de_Toulouse_logo.png" alt="Ours" />
                  <h4 class="card-title">Toulouse Ours</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1986</p>
                  <p>Un des clubs majeurs du Sud, important dans le développement du sport en Occitanie.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/fr/a/a4/LOGO_des_GRIZZLYS_CATALANS.png" alt="Grizzlys" />
                  <h4 class="card-title">Grizzlys Catalans</h4>
                </div>
                <div class="flip-card-back">
                  <p>Fondés en 2013</p>
                  <p>Un club jeune, ambitieux et en forte progression dans le paysage national.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://montpellier-hurricanes.com/wp-content/uploads/2024/10/02.png" alt="Hurricanes" />
                  <h4 class="card-title">Montpellier Hurricanes</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1993</p>
                  <p>Un club historique du Sud, reconnu pour son dynamisme et sa formation de jeunes.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/fr/2/2a/Blue_Stars_Marseille.png" alt="Blue Stars" />
                  <h4 class="card-title">Marseille Blue Stars</h4>
                </div>
                <div class="flip-card-back">
                  <p>Fondés en 1986</p>
                  <p>Une équipe majeure de ces dernières années, avec plusieurs finales et une montée en puissance nette.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://upload.wikimedia.org/wikipedia/fr/2/20/Logo_Argonautes_Aix.png" alt="Argonautes" />
                  <h4 class="card-title">Aix-en-Provence Argonautes</h4>
                </div>
                <div class="flip-card-back">
                  <p>Créés en 1986</p>
                  <p>Une légende du football américain français, avec une des histoires les plus riches du pays.</p>
                </div>
              </div>
            </div>

            <div class="flip-card">
              <div class="flip-card-inner">
                <div class="flip-card-front">
                  <img src="https://centaures-grenoble.com/wp-content/uploads/2021/06/cropped-Logo-tisse-textile-4-1.png" alt="Centaures" />
                  <h4 class="card-title">Grenoble Centaures</h4>
                </div>
                <div class="flip-card-back">
                  <p>Fondés en 1985</p>
                  <p>Un club stable et solide, très impliqué dans la formation et la durée.</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="section">
          <h1 class="titre">Vidéo introductive</h1>

          <div class="video-container">
            <iframe
              src="https://www.youtube.com/embed/spWCMxp1JgA"
              title="Vidéo football américain"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerpolicy="strict-origin-when-cross-origin"
              allowfullscreen
            ></iframe>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.page {
  position: relative;
  min-height: 100vh;
  background: url("@/assets/fond1.jpg") center center / cover no-repeat fixed;
}

.background-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.58);
  z-index: 0;
}

.layout {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  color: white;
  font-family: "Inter", system-ui, sans-serif;
  padding: 2rem;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding: 1rem 1.5rem;
  margin-bottom: 2rem;
  border-radius: 20px;
  background: rgba(12, 12, 12, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.logo {
  font-size: 1.4rem;
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
  justify-content: center;
  gap: 0.75rem;
  flex: 1;
}

.nav-link {
  color: rgba(255, 255, 255, 0.78);
  text-decoration: none;
  font-weight: 600;
  padding: 0.65rem 1rem;
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
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.login-btn {
  text-decoration: none;
  background: #c8102e;
  color: white;
  font-weight: 700;
  padding: 0.75rem 1.15rem;
  border-radius: 999px;
  transition: all 0.2s ease;
  box-shadow: 0 8px 20px rgba(200, 16, 46, 0.25);
}

.login-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(200, 16, 46, 0.35);
}

.content {
  max-width: 1400px;
  margin: 0 auto;
}

.carte {
  position: relative;
  z-index: 1;
  display: block;
  margin: 2rem 0 0 auto;
  width: min(45%, 700px);
  background-color: rgba(240, 248, 255, 0.18);
  border-radius: 2rem;
  opacity: 0.95;
  padding: 0.4rem;
}

.legende {
  position: relative;
  z-index: 1;
  width: fit-content;
  margin: 0.8rem 0 2rem auto;
  font-style: italic;
  text-decoration: underline;
  color: rgba(255, 255, 255, 0.82);
}

.section {
  margin-bottom: 3rem;
  padding: 1.5rem;
  border-radius: 24px;
  background: rgba(7, 7, 7, 0.48);
  border: 1px solid rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(6px);
}

.titre {
  margin: 0 0 1.25rem;
  font-size: clamp(1.5rem, 2vw, 2.4rem);
}

.texte {
  margin-bottom: 1rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.88);
}

.paragraphe {
  margin-left: 1.2rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.9);
}

.paragraphe li {
  margin-bottom: 0.6rem;
}

.bloc_club {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.flip-card {
  width: 100%;
  min-height: 260px;
  perspective: 1000px;
}

.flip-card-inner {
  width: 100%;
  height: 100%;
  min-height: 260px;
  position: relative;
  transition: transform 0.7s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.9rem;
  text-align: center;
  padding: 1rem;
}

.flip-card-front {
  background: rgba(17, 12, 12, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.flip-card-front img {
  width: 100%;
  max-width: 120px;
  max-height: 120px;
  object-fit: contain;
}

.card-title {
  margin: 0;
  font-size: 1rem;
}

.flip-card-back {
  background: linear-gradient(180deg, #5a3a33 0%, #3f2722 100%);
  color: white;
  transform: rotateY(180deg);
}

.flip-card-back p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.5;
}

.video-container {
  position: relative;
  width: 100%;
  max-width: 900px;
  margin: 2rem auto 0;
  aspect-ratio: 16 / 9;
}

.video-container iframe {
  width: 100%;
  height: 100%;
  border-radius: 18px;
}

@media (max-width: 900px) {
  .topbar {
    flex-direction: column;
    align-items: stretch;
  }

  .nav-links {
    flex-wrap: wrap;
  }

  .brand,
  .nav-right {
    justify-content: center;
  }

  .carte {
    width: 100%;
    margin-top: 1rem;
  }

  .legende {
    margin-right: auto;
  }

  .layout {
    padding: 1rem;
  }
}
</style>