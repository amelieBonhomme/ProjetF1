const API_URL = "http://localhost:8000/api/"

export async function loginUser(login, mdp) {
  const response = await fetch(API_URL + "login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ login, mdp }),
  })
  return await response.json()
}

export async function registerUser(payload) {
  const response = await fetch(API_URL + "register/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  })
  return await response.json()
}
