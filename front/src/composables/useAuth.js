import { ref } from "vue"
import { loginUser, registerUser } from "@/services/auth.js"

const isLogged = ref(false)
const error = ref("")
const user = ref(null)

export function useAuth() {
  const login = async (loginValue, mdpValue) => {
    const data = await loginUser(loginValue, mdpValue)

    if (data.error) {
      error.value = data.error
      return false
    }

    user.value = data
    isLogged.value = true
    localStorage.setItem("user", JSON.stringify(data))
    return true
  }

  const register = async (payload) => {
    const data = await registerUser(payload)

    if (data.error) {
      error.value = data.error
      return false
    }

    user.value = data
    isLogged.value = true
    localStorage.setItem("user", JSON.stringify(data))
    return true
  }

  const loadUser = () => {
    const stored = localStorage.getItem("user")
    if (stored) {
      user.value = JSON.parse(stored)
      isLogged.value = true
    }
  }

  const logout = () => {
    localStorage.removeItem("user")
    user.value = null
    isLogged.value = false
  }

  // ⭐⭐ LA LIGNE QUI MANQUAIT ⭐⭐
  return { isLogged, user, error, login, register, loadUser, logout }
}
