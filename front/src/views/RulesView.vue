<template>
  <router-link to="/" class="back-btn"> ← Return </router-link>

  <div class="rules-layout">
    <header class="rules-header">
      <h1>Rules & Positions</h1>
      <p>Comprendre le football américain, poste par poste.</p>
    </header>

    <!-- OFFENSE -->
    <section class="section">
      <h2>Offense</h2>
      <div class="content">
        <div class="schema">
          <img src="../assets/offensive.png" alt="Offense positions" />
        </div>
        <ul class="positions">
          <li><strong>QB</strong> – Chef d’orchestre, lance ou distribue le ballon</li>
          <li><strong>RB</strong> – Puissance et explosivité au sol</li>
          <li><strong>WR</strong> – Vitesse, précision, réception</li>
          <li><strong>TE</strong> – Blocage et réception</li>
          <li><strong>OL</strong> – Protection du quarterback</li>
        </ul>
      </div>
    </section>

    <!-- DEFENSE -->
    <section class="section">
      <h2>Defense</h2>
      <div class="content reverse">
        <ul class="positions">
          <li><strong>DL</strong> – Pression sur la ligne</li>
          <li><strong>LB</strong> – Lecture du jeu, polyvalence</li>
          <li><strong>CB</strong> – Couverture des receveurs</li>
          <li><strong>S</strong> – Dernier rempart</li>
        </ul>
        <div class="schema">
          <img src="../assets/defensive.jpg" alt="Defense positions" />
        </div>
      </div>
    </section>

    <!-- RULES -->
    <section class="rules-core">
      <h2>Core Rules</h2>

      <div class="rules-grid">
        <div class="rule-card">
          <h3>4 Downs</h3>
          <p>4 tentatives pour gagner 10 yards.</p>
        </div>
        <div class="rule-card">
          <h3>Touchdown</h3>
          <p>6 points en entrant dans l’en-but.</p>
        </div>
        <div class="rule-card">
          <h3>Field Goal</h3>
          <p>3 points au pied.</p>
        </div>
        <div class="rule-card">
          <h3>Turnover</h3>
          <p>Perte de balle = changement de possession.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style>
.rules-layout {
  min-height: 100vh;
  background-color: rgba(0, 0, 0, 0.849);
  color: white;
  padding: 4rem 2rem;
  font-family: 'Inter', system-ui, sans-serif;
  box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);
}

.rules-header {
  max-width: 600px;
  margin-bottom: 6rem;
}

.rules-header h1 {
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 900;
  text-transform: uppercase;
}

.rules-header p {
  color: rgba(255, 255, 255, 0.6);
  margin-top: 1rem;
}

.section {
  margin-bottom: 6rem;
}

.section h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.content.reverse {
  grid-template-columns: 1fr 1fr;
}

.schema img {
  width: 100%;
  filter: grayscale(100%) contrast(120%);
}

.positions {
  list-style: none;
  padding: 0;
}

.positions li {
  margin-bottom: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.75);
}

.positions strong {
  color: #c8102e;
}

.rules-core {
  margin-top: 8rem;
}

.rules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
}

.rule-card {
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 2rem;
  border-radius: 1rem;
  transition: transform 0.2s ease;
}

.rule-card:hover {
  transform: translateY(-6px);
}

.rule-card h3 {
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.rule-card p {
  color: rgba(255, 255, 255, 0.6);
}

.back-btn {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  padding: 0;
  font-size: 0.9rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  position: relative;
  text-decoration: none;
  display: inline-block;
}

.back-btn::after {
  content: '';
  display: block;
  width: 0;
  height: 1px;
  background: white;
  transition: width 0.3s ease;
  margin-top: 6px;
}

.back-btn:hover {
  color: white;
}

.back-btn:hover::after {
  width: 100%;
}
</style>
