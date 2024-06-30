import axios from 'axios'
import { MovieProvider } from './providers'

const BASE_URL = 'https://api.themoviedb.org/3/'
const ACCESS_TOKEN = process.env.REACT_APP_TMDB_ACCESS_TOKEN

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
}

export const fetchMovies = async (
  page: number,
  regionCode: string,
  providerId: number
): Promise<{ movies: Movie[]; totalPages: number }> => {
  const url = BASE_URL + `discover/movie`
  const response = await axios.get(url, {
    params: {
      include_adult: true,
      include_video: true,
      language: 'en-US',
      page: page,
      sort_by: 'popularity.desc',
      watch_region: regionCode,
      with_watch_providers: providerId,
    },
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
  })

  const { results: movies, total_pages: totalPages } = response.data
  return { movies, totalPages }
}

export const fetchWatchlistMovies = async (
  accountId: number,
  page: number = 1
): Promise<{ movies: Movie[]; totalPages: number }> => {
  const url = BASE_URL + `account/${accountId}/watchlist/movies`
  const response = await axios.get(url, {
    params: {
      language: 'en-US',
      page: page,
    },
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
  })
  const { results: movies, total_pages: totalPages } = response.data
  return { movies, totalPages }
}

export const fetchMovieProviders = async (movieId: number) => {
  const url = BASE_URL + `movie/${movieId}/watch/providers`
  const response = await axios.get(url, {
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
  })
  return response.data.results
}

export const fetchWatchlistMoviesWithProviders = async (accountId: number, regions: string[], page: number = 1) => {
  const { movies, totalPages } = await fetchWatchlistMovies(accountId, page)
  const providers = await Promise.all(movies.map((movie: Movie) => fetchMovieProviders(movie.id)))
  const moviesWithProviders = movies.map((movie, i) => {
    const netflixRegions = regions.filter((region) =>
      providers[i][region]?.flatrate?.map((provider: MovieProvider) => provider.provider_name).includes('Netflix')
    )
    return { ...movie, netflixRegions }
  })
  return { movies: moviesWithProviders, totalPages }
}
