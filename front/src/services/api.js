// Faire accéder le code au la base de données pour afficher

const API_URL = "http://localhost:8000/api/"

export async function getEquipes() {
  const response = await fetch(API_URL + "equipes/")
  return await response.json()
}
export async function getCircuit() {
  const response = await fetch(API_URL + "circuit/")
  return await response.json()
}

export async function getUsers() {
  const response = await fetch(API_URL + "users/")
  return await response.json()
}

export async function getCommentaires() {
  const response = await fetch(API_URL + "commentaires/")
  return await response.json()
}

export async function getFavoris() {
  const response = await fetch(API_URL + "favoris/")
  return await response.json()
}

// pas encore utiliser mais je le met en cas
export async function getPrefere() {
  const response = await fetch(API_URL + "prefere/")
  return await response.json()
}
