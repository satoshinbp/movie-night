import { Card, CardActionArea, CardContent, CardMedia, Chip, Stack, Typography } from '@mui/material'
import { Movie } from '../apis/tmdb'

export default function MovieList({ movies, regions }: { movies: Movie[]; regions: string[] }) {
  return (
    <Stack spacing={{ xs: 1, sm: 2 }} direction="row" useFlexGap flexWrap="wrap">
      {movies.map((movie) => {
        const matchedRegions = movie.netflix_regions.filter((r) => regions.includes(r))
        return (
          <Card
            sx={{
              width: 130,
              backgroundColor: matchedRegions.length > 0 ? 'inherit' : 'grey',
            }}
          >
            <CardActionArea
              href={movie.netflix_regions.length > 0 ? 'https://www.netflix.com/search?q=' + movie.title : ''}
              target="_blank"
            >
              <CardMedia
                sx={{ height: 216 }}
                image={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`}
                title={movie.title}
              />
            </CardActionArea>
            <CardContent>
              <Stack spacing={1}>
                <Typography variant="body2" noWrap>
                  {movie.title}
                </Typography>
                <Typography variant="body2">{'(' + movie.runtime + ' mins)'}</Typography>
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
        )
      })}
    </Stack>
  )
}
