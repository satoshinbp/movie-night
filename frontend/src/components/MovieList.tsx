import { Card, CardActionArea, CardContent, CardMedia, Chip, Fab, Stack, Typography } from '@mui/material'
import { Movie } from '../types/movies'
import DeleteIcon from '@mui/icons-material/Delete'

export default function MovieList({
  movies,
  regions,
  onRemove,
}: {
  movies: Movie[]
  regions: string[]
  onRemove: (movieId: number) => void
}) {
  return (
    <Stack spacing={{ xs: 1, sm: 2 }} direction="row" useFlexGap flexWrap="wrap">
      {movies.map((movie) => {
        const matchedRegions = movie.netflix_regions.filter((r) => regions.includes(r))
        return (
          <Card sx={{ position: 'relative', width: 276 }}>
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
                sx={{ height: 414 }}
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
