import axios from "axios"

const API = "https://api.jolpi.ca/ergast/f1/current"

export async function getClassementPilotes() {
  const res = await axios.get(`${API}/driverStandings.json`)
  const data = res.data.MRData.StandingsTable.StandingsLists[0]

  return {
    season: data.season,
    round: data.round,
    standings: data.DriverStandings
  }
}

export async function getClassementConstructeurs() {
  const res = await axios.get(`${API}/constructorStandings.json`)
  const data = res.data.MRData.StandingsTable.StandingsLists[0]

  return {
    season: data.season,
    round: data.round,
    standings: data.ConstructorStandings
  }
}
