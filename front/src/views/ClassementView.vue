<template>
  <div class="generalLayout">
    <main id="classement">

      <h1>Classement Pilotes</h1>
      <br>
      <p class="update-date">Dernière mise à jour : Saison {{ pilotesSeason }} — Manche {{ pilotesRound }}</p>
      <table class="classement-table">
        <thead>
          <tr>
            <th>Position</th>
            <th>Pilote</th>
            <th>Écurie</th>
            <th>Points</th>
            <th>Favori</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in pilotes" :key="p.Driver.driverId">
            <td>{{ p.position }}</td>
            <td>{{ p.Driver.givenName }} {{ p.Driver.familyName }}</td>
            <td>{{ p.Constructors[0].name }}</td>
            <td>{{ p.points }}</td>
            <td>
              <span v-if="favoris.includes(mapConstructors[p.Constructors[0].constructorId])">❤️</span>
              <span v-else>🤍</span>
            </td>
          </tr>
        </tbody>
      </table>

      <h1>Classement Constructeurs</h1>
      <br>
      <p class="update-date">Dernière mise à jour : Saison {{ constructeursSeason }} — Manche {{ constructeursRound }}</p>
      <table class="classement-table">
        <thead>
          <tr>
            <th>Position</th>
            <th>Écurie</th>
            <th>Points</th>
            <th>Favori</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="c in constructeurs" :key="c.Constructor.constructorId">
            <td>{{ c.position }}</td>
            <td>{{ c.Constructor.name }}</td>
            <td>{{ c.points }}</td>
            <td>
              <span v-if="favoris.includes(mapConstructors[c.Constructor.constructorId])">❤️</span>
              <span v-else>🤍</span>
            </td>
          </tr>
        </tbody>
      </table>
      <h1>Commentaires :</h1>
      <div class="commentaires">
        <div v-for="c in commentaires" :key="c.id" class="comment">
          <p class="auteur">{{ c.user.login }} — {{ c.date }}</p>
          <p>{{ c.texte }}</p>
        </div>
      </div>

      <div v-if="user" class="add-comment">
        <textarea v-model="newComment" placeholder="Écrire un commentaire..."></textarea>
        <button @click="submitComment">Envoyer</button>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { getClassementPilotes, getClassementConstructeurs } from "@/services/classementApi.js"
import { getFavoris } from "@/services/favorisApi.js"
import { getCommentaires, addCommentaire } from "@/services/commentairesApi.js"

const pilotes = ref([])
const pilotesSeason = ref("")
const pilotesRound = ref("")

const constructeurs = ref([])
const constructeursSeason = ref("")
const constructeursRound = ref("")
  
const favoris = ref([])
const user = JSON.parse(localStorage.getItem("user"))

const commentaires = ref([])
const newComment = ref("")

const mapConstructors = {
  alpine: "ALPINE",
  aston_martin: "ASTON",
  audi: "Audi / Kick Sauber", 
  ferrari: "FERRARI",
  haas: "HAAS",
  mclaren: "MCLAREN",
  mercedes: "MERCEDES",
  rb: "RB",
  red_bull: "REDBULL",
  williams: "WILLIAMS",
  cadillac: "CADILLAC"
}


onMounted(async () => {
  const p = await getClassementPilotes()
  pilotes.value = p.standings
  pilotesSeason.value = p.season
  pilotesRound.value = p.round

  const c = await getClassementConstructeurs()
  constructeurs.value = c.standings
  constructeursSeason.value = c.season
  constructeursRound.value = c.round

  favoris.value = await getFavoris(user.id_user)

  commentaires.value = await getCommentaires()

})

const submitComment = async () => {
  if (!newComment.value.trim()) return

  await addCommentaire(newComment.value, user.id_user)
  newComment.value = ""

  // Rafraîchir la liste
  commentaires.value = await getCommentaires()
}
</script>


