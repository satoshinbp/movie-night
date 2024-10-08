import { useEffect, useState } from 'react'
import { Container, SelectChangeEvent, Typography } from '@mui/material'
import { fetchWatchlist, fetchRegions, removeFromWatchlist } from '../apis/movies'
import MovieList from '../components/MovieList'
import RegionSelect from '../components/RegionSelect'
import { Movie } from '../types/movies'

const defaultRegions = ['CA', 'JP']

export default function Watchlist() {
  const [loading, setLoading] = useState(false)
  const [movies, setMovies] = useState<Movie[]>([])
  const [regions, setRegions] = useState<string[]>([])
  const [selectedRegions, setSelectedRegions] = useState<string[]>(defaultRegions)

  const compareMovies = (regions: string[]) => (a: Movie, b: Movie) => {
    const aOnNetflix = regions.some((r) => a.netflix_regions.includes(r))
    const bOnNetflix = regions.some((r) => b.netflix_regions.includes(r))
    if (aOnNetflix && !bOnNetflix) {
      return -1
    } else if (!aOnNetflix && bOnNetflix) {
      return 1
    } else {
      return a.title.localeCompare(b.title)
    }
  }

  const onRegionChange = (event: SelectChangeEvent<typeof selectedRegions>) => {
    const {
      target: { value },
    } = event
    const regions = typeof value === 'string' ? value.split(',') : value
    setSelectedRegions(regions)
    const sortedMovies = [...movies].sort(compareMovies(regions))
    setMovies(sortedMovies)
  }

  useEffect(() => {
    const refreshWatchlistMovies = async () => {
      try {
        setLoading(true)
        const [regions, movies] = await Promise.all([fetchRegions(), fetchWatchlist()])
        setRegions(regions.map((r) => r.iso_3166_1))
        setMovies(movies)
      } catch (error) {
        console.error('Error fetching watchlist movies:', error)
      } finally {
        setLoading(false)
      }
    }

    refreshWatchlistMovies()
  }, [])

  const handleRemove = async (movieId: number) => {
    try {
      await removeFromWatchlist(movieId)
      setMovies(movies.filter((m) => m.id !== movieId))
    } catch {
      console.error('Failed to remove movie from watchlist')
    }
  }

  if (loading) return <div>loading...</div>
  return (
    <Container>
      <Typography variant="h4" component="h1" mt={2} mb={2}>
        Watchlist
      </Typography>
      <RegionSelect regions={regions} selectedRegions={selectedRegions} onRegionChange={onRegionChange} />
      {movies.length > 0 && (
        <MovieList
          movies={movies.sort(compareMovies(selectedRegions))}
          regions={selectedRegions}
          onRemove={handleRemove}
        />
      )}
    </Container>
  )
}
