import { Card, CardActionArea, CardMedia, Chip, Fab, Stack, useTheme } from '@mui/material'
import { Movie } from '../types/movies'
import DeleteIcon from '@mui/icons-material/Delete'
import { useEffect, useRef, useState } from 'react'

export default function MovieList({
  movies,
  regions,
  onRemove,
  cols = 6,
}: {
  movies: Movie[]
  regions: string[]
  onRemove: (movieId: number) => void
  cols?: number
}) {
  const [width, setWidth] = useState(0)
  const gap = Number(useTheme().spacing(2).slice(0, -2))
  const elementRef = useRef<HTMLDivElement>(null)
  useEffect(() => {
    if (elementRef.current) {
      setWidth((elementRef.current.offsetWidth + gap) / cols - gap)
    }
  }, [cols, gap])

  return (
    <Stack spacing={{ xs: 1, sm: 2 }} direction="row" useFlexGap flexWrap="wrap" ref={elementRef}>
      {movies.map((movie) => {
        const matchedRegions = movie.netflix_regions.filter((r) => regions.includes(r))
        return (
          <Card sx={{ position: 'relative', width }}>
            <CardActionArea
              href={movie.netflix_regions.length > 0 ? 'https://www.netflix.com/search?q=' + movie.title : ''}
              target="_blank"
            >
              {matchedRegions.length === 0 && (
                <div
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: '100%',
                    backgroundColor: 'grey',
                    opacity: 0.5,
                  }}
                />
              )}
              <CardMedia
                sx={{ height: width * 1.5 }}
                image={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`}
                title={movie.title}
              />
              <Fab
                size="small"
                aria-label="remove"
                sx={{ position: 'absolute', top: 8, right: 8 }}
                onClick={() => onRemove(movie.id)}
              >
                <DeleteIcon />
              </Fab>
              {matchedRegions.length > 0 && (
                <Stack direction="row" spacing={1} sx={{ position: 'absolute', bottom: 8, left: 8 }}>
                  {matchedRegions.map((r) => (
                    <Chip key={r} label={r} color="primary" />
                  ))}
                </Stack>
              )}
              <Chip
                label={movie.runtime + ' mins'}
                sx={{ position: 'absolute', bottom: 8, right: 8 }}
                color="secondary"
              />
            </CardActionArea>
          </Card>
        )
      })}
    </Stack>
  )
}
