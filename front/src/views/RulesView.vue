<template>
  <div class="rules-page">
    <div class="rules-layout">
      <router-link to="/" class="back-btn">← Retour</router-link>

      <header class="rules-header card">
        <div class="header-text">
          <p class="eyebrow">Guide du jeu</p>
          <h1>Rules & Positions</h1>
          <p class="subtitle">
            Comprendre le football américain, poste par poste, avec les bases
            essentielles pour suivre un match.
          </p>
        </div>
      </header>

      <section class="section card">
        <div class="section-title">
          <h2>Offense</h2>
          <p>L’unité qui avance le ballon et construit le score.</p>
        </div>

        <div class="content">
          <div class="schema">
            <img src="@/assets/offensive.png" alt="Positions offensives" />
          </div>

          <ul class="positions">
            <li><strong>QB</strong> – Chef d’orchestre, lance ou distribue le ballon.</li>
            <li><strong>RB</strong> – Puissance et explosivité au sol.</li>
            <li><strong>WR</strong> – Vitesse, tracés précis et réception.</li>
            <li><strong>TE</strong> – Profil hybride entre blocage et réception.</li>
            <li><strong>OL</strong> – Protège le quarterback et ouvre des espaces.</li>
          </ul>
        </div>
      </section>

      <section class="section card">
        <div class="section-title">
          <h2>Defense</h2>
          <p>L’unité qui stoppe l’attaque adverse et provoque les erreurs.</p>
        </div>

        <div class="content reverse">
          <ul class="positions">
            <li><strong>DL</strong> – Met la pression dès la ligne de scrimmage.</li>
            <li><strong>LB</strong> – Lecture du jeu, impact physique et polyvalence.</li>
            <li><strong>CB</strong> – Suit les receveurs et défend la passe.</li>
            <li><strong>S</strong> – Dernier rempart, couverture profonde et aide défensive.</li>
          </ul>

          <div class="schema">
            <img src="@/assets/defensive.jpg" alt="Positions défensives" />
          </div>
        </div>
      </section>

      <section class="rules-core card">
        <div class="section-title">
          <h2>Core Rules</h2>
          <p>Les notions les plus importantes pour lire un match rapidement.</p>
        </div>

        <div class="rules-grid">
          <div class="rule-card">
            <span class="rule-number">01</span>
            <h3>4 Downs</h3>
            <p>Une équipe a 4 tentatives pour gagner 10 yards.</p>
          </div>

          <div class="rule-card">
            <span class="rule-number">02</span>
            <h3>Touchdown</h3>
            <p>6 points en entrant dans la zone d’en-but adverse.</p>
          </div>

          <div class="rule-card">
            <span class="rule-number">03</span>
            <h3>Field Goal</h3>
            <p>3 points grâce à un coup de pied entre les poteaux.</p>
          </div>

          <div class="rule-card">
            <span class="rule-number">04</span>
            <h3>Turnover</h3>
            <p>Une perte de balle donne immédiatement la possession à l’adversaire.</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.rules-page {
  min-height: 100vh;
  color: white;
}

.rules-layout {
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
  transition: all 0.2s ease;
}

.back-btn:hover {
  color: white;
  transform: translateX(-2px);
}

.rules-header {
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

.rules-header h1 {
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

.section,
.rules-core {
  padding: 2rem;
  margin-bottom: 2rem;
}

.section-title {
  margin-bottom: 1.5rem;
}

.section-title h2 {
  margin: 0 0 0.4rem;
  font-size: 2rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.section-title p {
  margin: 0;
  color: rgba(255, 255, 255, 0.64);
}

.content {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 2rem;
  align-items: center;
}

.content.reverse {
  grid-template-columns: 0.9fr 1.1fr;
}

.schema {
  padding: 1rem;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.03);
}

.schema img {
  width: 100%;
  display: block;
  border-radius: 16px;
  object-fit: cover;
}

.positions {
  list-style: none;
  padding: 0;
  margin: 0;
}

.positions li {
  margin-bottom: 1rem;
  padding: 1rem 1.1rem;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.04);
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.82);
}

.positions strong {
  color: #ff5b74;
}

.rules-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.2rem;
  margin-top: 1.5rem;
}

.rule-card {
  padding: 1.4rem;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.rule-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 91, 116, 0.35);
}

.rule-number {
  display: inline-block;
  margin-bottom: 0.8rem;
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #ff5b74;
}

.rule-card h3 {
  margin: 0 0 0.6rem;
  font-size: 1.1rem;
}

.rule-card p {
  margin: 0;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.68);
}

@media (max-width: 1024px) {
  .content,
  .content.reverse {
    grid-template-columns: 1fr;
  }

  .rules-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .rules-layout {
    padding: 1rem;
  }

  .rules-header,
  .section,
  .rules-core {
    padding: 1.25rem;
  }

  .rules-grid {
    grid-template-columns: 1fr;
  }

  .section-title h2 {
    font-size: 1.5rem;
  }
}
</style>