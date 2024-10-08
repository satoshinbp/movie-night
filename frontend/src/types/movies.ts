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

export interface Region {
  iso_3166_1: string
  english_name: string
  native_name: string
}
