import axios from 'axios'

const BASE_URL = 'http://localhost:8000'
const ACCOUNT_ID = process.env.REACT_APP_TMDB_ACCOUNT_ID

export interface Movie {
  adult: boolean
  backdrop_path: string
  genre_ids: number[]
  id: number
  original_language: string
  overview: string
  popularity: number
  poster_path: string
  release_date: string
  title: string
  video: boolean
  vote_average: number
  vote_count: number
  netflix_regions: string[]
  runtime: number
}
export const fetchWatchlist = async (): Promise<Movie[]> => {
  if (!ACCOUNT_ID) {
    throw Error('TMDB Account ID is not set')
  }
  const url = `${BASE_URL}/accounts/${parseInt(ACCOUNT_ID)}/watchlist`
  const res = await axios.get(url)
  return res.data
}

export interface Region {
  iso_3166_1: string
  english_name: string
  native_name: string
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
  const res = await axios.get(url)
  return res.data
}
