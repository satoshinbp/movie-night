import axios from 'axios'
import { Movie, Region } from '../types/movies'

const BASE_URL = 'http://localhost:8000'
const ACCOUNT_ID = process.env.REACT_APP_TMDB_ACCOUNT_ID

export const fetchWatchlist = async (): Promise<Movie[]> => {
  if (!ACCOUNT_ID) {
    throw Error('TMDB Account ID is not set')
  }
  const url = `${BASE_URL}/accounts/${parseInt(ACCOUNT_ID)}/watchlist`
  const res = await axios.get(url)
  return res.data
}

export const fetchRegions = async (): Promise<Region[]> => {
  const url = `${BASE_URL}/watch/regions`
  const res = await axios.get(url)
  return res.data
}

export const removeFromWatchlist = async (movieId: number): Promise<void> => {
  if (!ACCOUNT_ID) {
    throw Error('TMDB Account ID is not set')
  }
  const url = `${BASE_URL}/accounts/${parseInt(ACCOUNT_ID)}/watchlist/remove/${movieId}`
  const res = await axios.post(url)
  return res.data
}
