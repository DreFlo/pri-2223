export type Title = {
    id: string;
    title: string;
    type: string;
    release_year: number;
    age_cretification: string;
    description: string;
    runtime: number;
    seasons: number | null;
    genres: string[];
    imdb_id: string | null;
    imdb_score: number | null;
    imdb_votes: number | null;
    tmdb_popularity: number | null;
    tmdb_score: number | null;
    content_type: string;
}