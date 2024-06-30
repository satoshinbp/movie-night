import { useEffect, useState } from 'react'
import { Container, Pagination, Stack, Typography } from '@mui/material'
import { fetchWatchlistMoviesWithProviders } from '../apis/movies'
import MovieList, { MovieWithProvider } from '../components/MovieList'
import RegionSelect from '../components/RegionSelect'
import { fetchMovieProviderRegions } from '../apis/providers'

const ACCOUNT_ID = process.env.REACT_APP_TMDB_ACCOUNT_ID
const defaultRegions = ['CA', 'JP']

export default function Watchlist() {
  const [movies, setMovies] = useState<MovieWithProvider[]>([])
  const [page, setPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const [regions, setRegions] = useState<string[]>([])
  const [selectedRegions, setSelectedRegions] = useState<string[]>([])

  useEffect(() => {
    const refreshRegions = async () => {
      const regions = await fetchMovieProviderRegions()
      setRegions(regions.map((r) => r.iso_3166_1))
      setSelectedRegions(regions.map((r) => r.iso_3166_1).filter((r) => defaultRegions.includes(r)))
    }
    refreshRegions()
  }, [])

  useEffect(() => {
    const refreshWatchlistMovies = async () => {
      if (!ACCOUNT_ID) {
        console.error('TMDB Account ID is not set')
        return
      }

      try {
        const { movies, totalPages } = await fetchWatchlistMoviesWithProviders(parseInt(ACCOUNT_ID), selectedRegions)
        setPage(1)
        setMovies(movies)
        setTotalPages(totalPages)
      } catch (error) {
        console.error('Error fetching watchlist movies:', error)
      }
    }
    refreshWatchlistMovies()
  }, [selectedRegions])

  const handlePageChange = async (_: React.ChangeEvent<unknown>, value: number) => {
    if (!ACCOUNT_ID) {
      console.error('TMDB Account ID is not set')
      return
    }

    const { movies, totalPages } = await fetchWatchlistMoviesWithProviders(parseInt(ACCOUNT_ID), selectedRegions, value)
    setPage(value)
    setMovies(movies)
    setMovies(movies)
    setTotalPages(totalPages)
  }

  return (
    <Container>
      <Typography variant="h4" component="h1" mt={2} mb={2}>
        Watchlist
      </Typography>
      <Stack spacing={2} mt={2} mb={2}>
        <RegionSelect regions={regions} selectedRegions={selectedRegions} setSelectedRegions={setSelectedRegions} />
        {movies.length > 0 && (
          <>
            <Pagination count={totalPages} page={page} onChange={handlePageChange} />
            <MovieList movies={movies} />
            <Pagination count={totalPages} page={page} onChange={handlePageChange} />
          </>
        )}
      </Stack>
    </Container>
  )
}
