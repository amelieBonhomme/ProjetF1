import Chart from "chart.js/auto"

export async function renderSexeChart(canvasId) {
  const res = await fetch("http://localhost:8000/api/stats/sexe/")
  const data = await res.json()

  const hommes = data.H || 0
  const femmes = data.F || 0
  const autres = data.X || 0

  const ctx = document.getElementById(canvasId)

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Hommes", "Femmes", "Autres"],
      datasets: [{
        data: [hommes, femmes, autres],
        backgroundColor: ["#3498db", "#e74c3c", "#9b59b6"]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "bottom" }
      }
    }
  })
}
