import axios from 'axios'

const BASE_URL = 'https://api.themoviedb.org/3/watch/providers/'
const ACCESS_TOKEN = process.env.REACT_APP_TMDB_ACCESS_TOKEN

export interface MovieProvider {
  display_priorities: any
  display_priority: number
  logo_path: string
  provider_name: string
  provider_id: number
}
export const fetchMovieProviders = async (region: string): Promise<MovieProvider> => {
  const url = BASE_URL + 'movie'
  const response = await axios.get(url, {
    params: { language: 'en-US', watch_region: region },
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
  })
  return response.data.results
}

export interface Region {
  iso_3166_1: string
  english_name: string
  native_name: string
}
export const fetchMovieProviderRegions = async (): Promise<Region[]> => {
  const url = BASE_URL + 'regions'
  const response = await axios.get(url, {
    params: { language: 'en-US' },
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
  })
  return response.data.results
}
