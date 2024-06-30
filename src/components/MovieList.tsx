import { Card, CardActionArea, CardContent, CardMedia, Grid, Typography } from '@mui/material'
import { Movie } from '../apis/movies'

export interface MovieWithProvider extends Movie {
  netflixRegions: string[]
}

export default function MovieList({ movies }: { movies: MovieWithProvider[] }) {
  return (
    <Grid container spacing={2}>
      {movies.map((movie) => (
        <Grid item key={movie.id} xs={12} sm={6} md={4} lg={3}>
          <Card sx={{ backgroundColor: movie.netflixRegions.length > 0 ? 'inherit' : 'grey' }}>
            <CardActionArea
              href={movie.netflixRegions.length > 0 ? 'https://www.netflix.com/search?q=' + movie.title : ''}
              target="_blank"
            >
              <CardMedia
                sx={{ height: 140 }}
                image={`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`}
                title={movie.title}
              />
              <CardContent>
                <Typography variant="h6" component="div">
                  {movie.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Release Date: {movie.release_date}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Rate: {movie.vote_average} ({movie.vote_count})
                </Typography>
                {movie.netflixRegions.length > 0 && (
                  <Typography variant="body2" color="text.secondary">
                    Streaming on Netflix ({movie.netflixRegions.join(', ')})
                  </Typography>
                )}
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>
      ))}
    </Grid>
  )
}
