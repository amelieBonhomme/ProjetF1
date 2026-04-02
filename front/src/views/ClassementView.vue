<script setup>
import { classementFrance } from "@/data/classementFrance";
</script>

<template>
  <section class="classement-page">
    <div class="classement-header">
      <h1>Classement D1 Élite France</h1>
      <p>Championnat français de football américain</p>
    </div>

    <div class="table-wrapper">
      <table class="classement-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Équipe</th>
            <th>Ville</th>
            <th>J</th>
            <th>Pts</th>
            <th>G</th>
            <th>N</th>
            <th>P</th>
            <th>PTS+</th>
            <th>PTS-</th>
            <th>Diff</th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="team in classementFrance"
            :key="team.rang"
            :class="{
              first: team.rang === 1,
              second: team.rang === 2,
              third: team.rang === 3
            }"
          >
            <td>{{ team.rang }}</td>
            <td>{{ team.equipe }}</td>
            <td>{{ team.ville }}</td>
            <td>{{ team.matchs }}</td>
            <td>{{ team.points }}</td>
            <td>{{ team.gagne }}</td>
            <td>{{ team.nul }}</td>
            <td>{{ team.perdu }}</td>
            <td>{{ team.ptsPlus }}</td>
            <td>{{ team.ptsMoins }}</td>
            <td :class="team.diff >= 0 ? 'positive' : 'negative'">
              {{ team.diff >= 0 ? `+${team.diff}` : team.diff }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<style scoped>
.classement-page {
  min-height: 100vh;
  padding: 40px 24px;
  background: linear-gradient(180deg, #0b1020 0%, #11182d 100%);
  color: white;
}

.classement-header {
  margin-bottom: 24px;
}

.classement-header h1 {
  margin: 0 0 8px;
  font-size: 2rem;
  font-weight: 800;
}

.classement-header p {
  margin: 0;
  color: #b8c1d9;
}

.table-wrapper {
  overflow-x: auto;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.04);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.classement-table {
  width: 100%;
  border-collapse: collapse;
}

.classement-table th,
.classement-table td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.classement-table th {
  background: rgba(255, 255, 255, 0.06);
  font-weight: 700;
}

.classement-table tr:hover {
  background: rgba(255, 255, 255, 0.05);
}

.first {
  background: rgba(255, 215, 0, 0.08);
}

.second {
  background: rgba(192, 192, 192, 0.08);
}

.third {
  background: rgba(205, 127, 50, 0.08);
}

.positive {
  color: #4ade80;
  font-weight: 700;
}

.negative {
  color: #f87171;
  font-weight: 700;
}
</style>