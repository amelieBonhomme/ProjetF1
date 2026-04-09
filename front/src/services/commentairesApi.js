export async function getCommentaires() {
  const res = await fetch("http://localhost:8000/api/commentaires/")
  return await res.json()
}

export async function addCommentaire(texte, id_user) {
  const res = await fetch("http://localhost:8000/api/commentaires/add/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texte, id_user })
  })
  return await res.json()
}
