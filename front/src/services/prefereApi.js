import axios from "axios"

const API = "http://127.0.0.1:8000/api"

export async function getPrefere(id_user) {
  const res = await axios.get(`${API}/prefere/${id_user}/`)
  return res.data   // renvoie une LISTE d'id_circuit
}

export async function togglePrefere(id_user, id_circuit) {
  const res = await axios.post(`${API}/prefere/toggle/`, {
    user_id: id_user,
    circuit_id: id_circuit
  })
  return res.data
}