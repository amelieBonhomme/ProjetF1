<template>
  <div class="clubs-page">
    <div class="clubs-layout">
      <router-link to="/" class="back-btn">← Retour</router-link>

      <header class="clubs-header card">
        <p class="eyebrow">Clubs français</p>
        <h1>Infos clubs</h1>
        <p class="subtitle">
          Découvre les principales équipes françaises de football américain,
          leur identité et leur histoire.
        </p>
      </header>

      <section class="card section">
        <h2 class="section-title">Conférence A</h2>

        <div class="bloc_club">
          <div class="flip-card" v-for="club in conferenceA" :key="club.nom">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <img :src="club.logo" :alt="club.nom" />
                <h4 class="card-title">{{ club.nom }}</h4>
              </div>
              <div class="flip-card-back">
                <p>{{ club.date }}</p>
                <p>{{ club.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="card section">
        <h2 class="section-title">Conférence B</h2>

        <div class="bloc_club">
          <div class="flip-card" v-for="club in conferenceB" :key="club.nom">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <img :src="club.logo" :alt="club.nom" />
                <h4 class="card-title">{{ club.nom }}</h4>
              </div>
              <div class="flip-card-back">
                <p>{{ club.date }}</p>
                <p>{{ club.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
const conferenceA = [
  {
    nom: "Asnières-sur-Seine Molosses",
    logo: "https://molossesfootball.com/wp-content/uploads/2025/06/Logo-principal.png",
    date: "Créés en 1992",
    description: "Un des clubs franciliens les plus réguliers, reconnu pour sa formation et son identité locale forte."
  },
  {
    nom: "Saint-Ouen-l’Aumône Cougars",
    logo: "https://lescougars.fr/wp-content/uploads/2023/01/Logo_Cougars_Football_rmvd_bckg.png",
    date: "Fondés en 1989",
    description: "Un des clubs les plus titrés de France, marqué par une vraie culture de performance."
  },
  {
    nom: "Amiens Spartiates",
    logo: "https://upload.wikimedia.org/wikipedia/commons/6/68/Logo_des_Spartiates_d%27Amiens.png",
    date: "Créés en 1987",
    description: "Une référence dans le Nord, connue pour son identité forte et son attachement à la ville d’Amiens."
  },
  {
    nom: "Villeneuve-d’Ascq Vikings",
    logo: "https://upload.wikimedia.org/wikipedia/fr/f/fd/Logo_Vikings_Ascq.png",
    date: "Créés en 1984",
    description: "Un club historique du Nord, pilier du développement du football américain autour de Lille."
  },
  {
    nom: "La Courneuve Flash",
    logo: "https://upload.wikimedia.org/wikipedia/fr/e/ed/Logo_Flash_La_Courneuve.png",
    date: "Créés en 1984",
    description: "Le club le plus titré de France, référence absolue du football américain français."
  },
  {
    nom: "Thonon Black Panthers",
    logo: "https://www.les-black-panthers.org/FootUS/wp-content/uploads/2024/01/Blason-Black-Panthers.png",
    date: "Fondés en 1987",
    description: "Un club prestigieux, reconnu pour son professionnalisme et ses performances européennes."
  }
];

const conferenceB = [
  {
    nom: "Toulouse Ours",
    logo: "https://upload.wikimedia.org/wikipedia/en/e/e1/Ours_de_Toulouse_logo.png",
    date: "Créés en 1986",
    description: "Un des clubs majeurs du Sud, important dans le développement du sport en Occitanie."
  },
  {
    nom: "Grizzlys Catalans",
    logo: "https://upload.wikimedia.org/wikipedia/fr/a/a4/LOGO_des_GRIZZLYS_CATALANS.png",
    date: "Fondés en 2013",
    description: "Un club jeune, ambitieux et en forte progression dans le paysage national."
  },
  {
    nom: "Montpellier Hurricanes",
    logo: "https://montpellier-hurricanes.com/wp-content/uploads/2024/10/02.png",
    date: "Créés en 1993",
    description: "Un club historique du Sud, reconnu pour son dynamisme et sa formation de jeunes."
  },
  {
    nom: "Marseille Blue Stars",
    logo: "https://upload.wikimedia.org/wikipedia/fr/2/2a/Blue_Stars_Marseille.png",
    date: "Fondés en 1986",
    description: "Une équipe majeure de ces dernières années, avec plusieurs finales et une montée en puissance nette."
  },
  {
    nom: "Aix-en-Provence Argonautes",
    logo: "https://upload.wikimedia.org/wikipedia/fr/2/20/Logo_Argonautes_Aix.png",
    date: "Créés en 1986",
    description: "Une légende du football américain français, avec une des histoires les plus riches du pays."
  },
  {
    nom: "Grenoble Centaures",
    logo: "https://centaures-grenoble.com/wp-content/uploads/2021/06/cropped-Logo-tisse-textile-4-1.png",
    date: "Fondés en 1985",
    description: "Un club stable et solide, très impliqué dans la formation et la durée."
  }
];
</script>

<style scoped>
.clubs-page {
  min-height: 100vh;
  color: white;
}

.clubs-layout {
  max-width: 1300px;
  margin: 0 auto;
  padding: 2rem;
}

.card {
  background: rgba(12, 12, 12, 0.62);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 24px;
  backdrop-filter: blur(10px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.22);
}

.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.72);
  font-size: 0.92rem;
  font-weight: 600;
}

.back-btn:hover {
  color: white;
}

.clubs-header {
  padding: 2.5rem;
  margin-bottom: 2rem;
}

.eyebrow {
  margin: 0 0 0.8rem;
  color: #ff5b74;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 0.8rem;
  font-weight: 700;
}

.clubs-header h1 {
  margin: 0;
  font-size: clamp(2.6rem, 6vw, 5rem);
  font-weight: 900;
  text-transform: uppercase;
  line-height: 0.95;
}

.subtitle {
  max-width: 700px;
  margin-top: 1rem;
  color: rgba(255, 255, 255, 0.72);
  line-height: 1.8;
  font-size: 1.05rem;
}

.section {
  padding: 2rem;
  margin-bottom: 2rem;
}

.section-title {
  margin: 0 0 1.5rem;
  font-size: 2rem;
  text-transform: uppercase;
}

.bloc_club {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 1.5rem;
}

.flip-card {
  width: 100%;
  min-height: 280px;
  perspective: 1000px;
}

.flip-card-inner {
  width: 100%;
  height: 100%;
  min-height: 280px;
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

@media (max-width: 640px) {
  .clubs-layout {
    padding: 1rem;
  }

  .clubs-header,
  .section {
    padding: 1.25rem;
  }
}
</style>