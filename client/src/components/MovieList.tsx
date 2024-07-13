import { Card, CardActionArea, CardContent, CardMedia, Chip, Grid, Stack, Typography } from '@mui/material'
import { Movie } from '../apis/tmdb'

export default function MovieList({ movies, regions }: { movies: Movie[]; regions: string[] }) {
  return (
    <Grid container spacing={1}>
      {movies.map((movie) => {
        const matchedRegions = movie.netflix_regions.filter((r) => regions.includes(r))
        return (
          <Grid item key={movie.id} xs={6} sm={4} md={3} lg={2}>
            <Card
              sx={{
                height: '100%',
                backgroundColor: matchedRegions.length > 0 ? 'inherit' : 'grey',
              }}
            >
              <CardActionArea
                href={movie.netflix_regions.length > 0 ? 'https://www.netflix.com/search?q=' + movie.title : ''}
                target="_blank"
              >
                <CardMedia
                  sx={{ height: 300 }}
                  image={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`}
                  title={movie.title}
                />
              </CardActionArea>
              <CardContent>
                <Stack spacing={1}>
                  <Typography>{movie.title + ' (' + movie.runtime + ' mins)'}</Typography>
                  {matchedRegions.length > 0 && (
                    <Stack direction="row" spacing={1}>
                      {matchedRegions.map((r) => (
                        <Chip key={r} label={r} />
                      ))}
                    </Stack>
                  )}
                </Stack>
              </CardContent>
            </Card>
          </Grid>
        )
      })}
    </Grid>
  )
}
