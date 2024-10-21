import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.ticker import MaxNLocator


class Movie:
    def __init__(self, id, year, rating_imdb, number_of_votes, rating_tmdb, number_of_words_title, number_of_words_description):
        self.id = id
        self.year = year
        self.rating_imdb = rating_imdb
        self.number_of_votes = number_of_votes
        self.rating_tmdb = rating_tmdb
        self.genres = []
        self.number_of_words_title = number_of_words_title
        self.number_of_words_description = number_of_words_description
    def add_genre(self, genre):
        self.genres.append(genre)
    



class Show:
    def __init__(self, id, year, rating_imdb, number_of_votes, rating_tmdb, number_of_words_title, number_of_words_description):
        self.id = id
        self.year = year
        self.rating_imdb = rating_imdb
        self.number_of_votes = number_of_votes
        self.rating_tmdb = rating_tmdb
        self.genres = []
        self.number_of_words_title = number_of_words_title
        self.number_of_words_description = number_of_words_description
    def add_genre(self, genre):
        self.genres.append(genre)

movies = {}
shows = {}
genres = []

with open('data_netflix/titles.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        is_movie = True
        if (row[0][1] == 's'):
            is_movie = False

        if is_movie:
            movies[row[0]] = Movie(row[0], int(row[4]) if row[4] != '' else 0,
            float(row[11]) if row[11] != '' else 0, 
            float(row[12]) if row[12] != '' else 0,
            float(row[14]) if row[14] != '' else 0,
            len(row[1].split()), len(row[3].split()))
        else:
            shows[row[0]] = Show(row[0], int(row[4]) if row[4] != '' else 0, 
            float(row[11]) if row[11] != '' else 0, 
            float(row[12]) if row[12] != '' else 0,
             float(row[14]) if row[14] != '' else 0,
            len(row[1].split()), len(row[3].split()))

with open('data_netflix/genres.csv', 'r') as f:
    reader = csv.reader(f)
    genres = next(reader)[1:]
    for row in reader:
        is_movie = True
        if (row[0][1] == 's'):
            is_movie = False
        row_without_id = row[1:]
        for (i, genre) in enumerate(row_without_id):
            if genre == '1':
                if is_movie and row[0] in movies:
                    movies[row[0]].add_genre(genres[i])
                elif not is_movie and row[0] in shows:
                    shows[row[0]].add_genre(genres[i])

#dictionaries with number of movies and shows per genre
number_movies_per_genre = {}
number_shows_per_genre = {}
#dictionaries with number of movies and shows per year
number_movies_per_year = {}
number_shows_per_year = {}
#dictionaries with average rating of movies and shows per year
average_rating_movies_per_year = {}
average_rating_shows_per_year = {}
#dictionaries with average rating of movies and shows per genre
average_rating_movies_per_genre = {}
average_rating_shows_per_genre = {}
#dictionaries with number of votes of movies and shows per genre
number_votes_movies_per_genre = {}
number_votes_shows_per_genre = {}
#dictionaries with number of votes of movies and shows per year
number_votes_movies_per_year = {}
number_votes_shows_per_year = {}
#dictionaries with average rating of movies and shows per genre (tmdb)
average_rating_movies_per_genre_tmdb = {}
average_rating_shows_per_genre_tmdb = {}

for movie in movies.values():
    for genre in movie.genres:
        if genre not in number_movies_per_genre:
            number_movies_per_genre[genre] = 0
        number_movies_per_genre[genre] += 1
        if genre not in average_rating_movies_per_genre:
            average_rating_movies_per_genre[genre] = 0
        average_rating_movies_per_genre[genre] += movie.rating_imdb
        if genre not in number_votes_movies_per_genre:
            number_votes_movies_per_genre[genre] = 0
        number_votes_movies_per_genre[genre] += movie.number_of_votes
        if genre not in average_rating_movies_per_genre_tmdb:
            average_rating_movies_per_genre_tmdb[genre] = 0
        average_rating_movies_per_genre_tmdb[genre] += movie.rating_tmdb
    if movie.year not in number_movies_per_year and movie.year >= 2000:
        number_movies_per_year[movie.year] = 1
    elif movie.year in number_movies_per_year:
        number_movies_per_year[movie.year] += 1
    if movie.year not in average_rating_movies_per_year and movie.year >= 2000:
        average_rating_movies_per_year[movie.year] = movie.rating_imdb
    elif movie.year in average_rating_movies_per_year:
        average_rating_movies_per_year[movie.year] += movie.rating_imdb
    if movie.year not in number_votes_movies_per_year and movie.year >= 2000:
        number_votes_movies_per_year[movie.year] = movie.number_of_votes
    elif movie.year in number_votes_movies_per_year:
        number_votes_movies_per_year[movie.year] += movie.number_of_votes


for show in shows.values():
    for genre in show.genres:
        if genre not in number_shows_per_genre:
            number_shows_per_genre[genre] = 0
        number_shows_per_genre[genre] += 1
        if genre not in average_rating_shows_per_genre:
            average_rating_shows_per_genre[genre] = 0
        average_rating_shows_per_genre[genre] += show.rating_imdb
        if genre not in number_votes_shows_per_genre:
            number_votes_shows_per_genre[genre] = 0
        number_votes_shows_per_genre[genre] += show.number_of_votes
        if genre not in average_rating_shows_per_genre_tmdb:
            average_rating_shows_per_genre_tmdb[genre] = 0
        average_rating_shows_per_genre_tmdb[genre] += show.rating_tmdb
    if show.year not in number_shows_per_year and show.year >= 2000:
        number_shows_per_year[show.year] = 1
    elif show.year in number_shows_per_year:
        number_shows_per_year[show.year] += 1
    if show.year not in average_rating_shows_per_year and show.year >= 2000:
        average_rating_shows_per_year[show.year] = show.rating_imdb
    elif show.year in average_rating_shows_per_year:
        average_rating_shows_per_year[show.year] += show.rating_imdb
    if show.year not in number_votes_shows_per_year and show.year >= 2000:
        number_votes_shows_per_year[show.year] = show.number_of_votes
    elif show.year in number_votes_shows_per_year:
        number_votes_shows_per_year[show.year] += show.number_of_votes

for year in average_rating_movies_per_year:
    average_rating_movies_per_year[year] /= number_movies_per_year[year]

for year in average_rating_shows_per_year:
    average_rating_shows_per_year[year] /= number_shows_per_year[year]

for genre in average_rating_movies_per_genre:
    average_rating_movies_per_genre[genre] /= number_movies_per_genre[genre]

for genre in average_rating_shows_per_genre:
    average_rating_shows_per_genre[genre] /= number_shows_per_genre[genre]

for genre in number_votes_movies_per_genre:
    number_votes_movies_per_genre[genre] /= number_movies_per_genre[genre]

for genre in number_votes_shows_per_genre:
    number_votes_shows_per_genre[genre] /= number_shows_per_genre[genre]

for year in number_votes_movies_per_year:
    number_votes_movies_per_year[year] /= number_movies_per_year[year]

for year in number_votes_shows_per_year:
    number_votes_shows_per_year[year] /= number_shows_per_year[year]

for genre in average_rating_movies_per_genre_tmdb:
    average_rating_movies_per_genre_tmdb[genre] /= number_movies_per_genre[genre]

for genre in average_rating_shows_per_genre_tmdb:
    average_rating_shows_per_genre_tmdb[genre] /= number_shows_per_genre[genre]

#add 0 to years with no movies or shows
for year in range(2000, 2023):
    if year not in number_movies_per_year:
        number_movies_per_year[year] = 0
    if year not in number_shows_per_year:
        number_shows_per_year[year] = 0
    if year not in average_rating_movies_per_year:
        average_rating_movies_per_year[year] = 0
    if year not in average_rating_shows_per_year:
        average_rating_shows_per_year[year] = 0
    if year not in number_votes_movies_per_year:
        number_votes_movies_per_year[year] = 0
    if year not in number_votes_shows_per_year:
        number_votes_shows_per_year[year] = 0
    
'''
# Plot histogram of genres for movies and shows
X_axis = np.arange(len(genres))
genre_array_movie = np.array([number_movies_per_genre[key] for key in sorted(genres)])
genre_array_show = np.array([number_shows_per_genre[key] for key in sorted(genres)])
plt.bar(X_axis - 0.2, genre_array_movie, 0.4, label = 'Movies', hatch = '////', color = 'red', edgecolor = 'black')
plt.bar(X_axis + 0.2, genre_array_show, 0.4, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(genres), rotation = 90)
plt.legend()
plt.title('Netflix - Number of movies and TV shows per genre')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_ylim(0, 2000)

#save plot to file
plt.savefig('imgs/genre_histogram_netflix.png')
plt.show()

# Plot histogram of years for movies
X_axis = np.arange(len(number_movies_per_year))
years_array_movie = np.array([number_movies_per_year[key] for key in sorted(number_movies_per_year.keys())])
plt.bar(X_axis, years_array_movie, label = 'Movies', color = 'red', edgecolor = 'black')
plt.xticks(X_axis, sorted(number_movies_per_year.keys()))
plt.legend()
plt.title('Netflix - Number of movies per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(number_movies_per_year.keys())[::5])
plt.gca().set_ylim(0, 700)
plt.savefig('imgs/year_movie_histogram_netflix.png')
plt.show()

# Plot histogram of years for shows
X_axis = np.arange(len(number_shows_per_year))
years_array_show = np.array([number_shows_per_year[key] for key in sorted(number_shows_per_year.keys())])
plt.bar(X_axis, years_array_show, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(number_shows_per_year.keys()))
plt.legend()
plt.title('Netflix - Number of TV shows per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(number_shows_per_year.keys())[::5])
plt.gca().set_ylim(0, 700)
plt.savefig('imgs/year_show_histogram_netflix.png')
plt.show()

# Plot histogram of average rating for movies
X_axis = np.arange(len(average_rating_movies_per_year))
average_rating_array_movie = np.array([average_rating_movies_per_year[key] for key in sorted(average_rating_movies_per_year.keys())])
plt.bar(X_axis, average_rating_array_movie, label = 'Movies', color = 'red', edgecolor = 'black')
plt.xticks(X_axis, sorted(average_rating_movies_per_year.keys()))
plt.legend()
plt.title('Netflix - Average rating of movies per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(average_rating_movies_per_year.keys())[::5])
plt.gca().set_ylim(4, 8)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('imgs/rating_movie_histogram_netflix.png')
plt.show()

# Plot histogram of average rating for shows
X_axis = np.arange(len(average_rating_shows_per_year))
average_rating_array_show = np.array([average_rating_shows_per_year[key] for key in sorted(average_rating_shows_per_year.keys())])
plt.bar(X_axis, average_rating_array_show, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(average_rating_shows_per_year.keys()))
plt.legend()
plt.title('Netflix - Average rating of TV shows per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(average_rating_shows_per_year.keys())[::5])
plt.gca().set_ylim(4, 8)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('imgs/rating_show_histogram_netflix.png')
plt.show()

# Plot histogram of average rating for movies and shows per genre
X_axis = np.arange(len(genres))
average_rating_array_movie = np.array([average_rating_movies_per_genre[key] for key in sorted(genres)])
average_rating_array_show = np.array([average_rating_shows_per_genre[key] for key in sorted(genres)])
plt.bar(X_axis - 0.2, average_rating_array_movie, 0.4, label = 'Movies', hatch = '////', color = 'red', edgecolor = 'black')
plt.bar(X_axis + 0.2, average_rating_array_show, 0.4, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(genres), rotation = 90)
plt.legend()
plt.title('Netflix - Average rating of movies and TV shows per genre')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_ylim(4, 8)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('imgs/rating_genre_histogram_netflix.png')
plt.show()


# Plot histogram of number of votes for movies and shows per genre
X_axis = np.arange(len(genres))
number_votes_array_movie = np.array([number_votes_movies_per_genre[key] for key in sorted(genres)])
number_votes_array_show = np.array([number_votes_shows_per_genre[key] for key in sorted(genres)])
plt.bar(X_axis - 0.2, number_votes_array_movie, 0.4, label = 'Movies', hatch = '////', color = 'red', edgecolor = 'black')
plt.bar(X_axis + 0.2, number_votes_array_show, 0.4, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(genres), rotation = 90)
plt.legend()
plt.title('Netflix - Number of votes per movies and TV shows per genre')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_ylim(0, 125000)
plt.savefig('imgs/votes_genre_histogram_netflix.png')
plt.show()

# Plot histogram of number of votes for movies per year
X_axis = np.arange(len(number_votes_movies_per_year))
number_votes_array_movie = np.array([number_votes_movies_per_year[key] for key in sorted(number_votes_movies_per_year.keys())])
plt.bar(X_axis, number_votes_array_movie, label = 'Movies', color = 'red', edgecolor = 'black')
plt.xticks(X_axis, sorted(number_votes_movies_per_year.keys()))
plt.legend()
plt.title('Netflix - Number of votes per movies per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(number_votes_movies_per_year.keys())[::5])
plt.gca().set_ylim(0, 225000)
plt.savefig('imgs/votes_movie_histogram_netflix.png')
plt.show()

# Plot histogram of number of votes for shows per year
X_axis = np.arange(len(number_votes_shows_per_year))
number_votes_array_show = np.array([number_votes_shows_per_year[key] for key in sorted(number_votes_shows_per_year.keys())])
plt.bar(X_axis, number_votes_array_show, label = 'TV Shows', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(number_votes_shows_per_year.keys()))
plt.legend()
plt.title('Netflix - Number of votes per TV shows per year since 2000')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks(X_axis[::5])
plt.gca().set_xticklabels(sorted(number_votes_shows_per_year.keys())[::5])
plt.gca().set_ylim(0, 225000)
plt.savefig('imgs/votes_show_histogram_netflix.png')
plt.show()

# Plot histogram of average rating for movies between imdb and tmdb per genre
X_axis = np.arange(len(genres))
average_rating_array_movie_imdb = np.array([average_rating_movies_per_genre[key] for key in sorted(genres)])
average_rating_array_movie_tmdb = np.array([average_rating_movies_per_genre_tmdb[key] for key in sorted(genres)])
plt.bar(X_axis - 0.2, average_rating_array_movie_imdb, 0.4, label = 'IMDB', hatch = '////', color = 'red', edgecolor = 'black')
plt.bar(X_axis + 0.2, average_rating_array_movie_tmdb, 0.4, label = 'TMDB', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(genres), rotation = 90)
plt.legend()
plt.title('Netflix - Average rating of movies per genre between IMDB and TMDB')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_ylim(4, 8)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('imgs/rating_movie_imdb_tmdb_histogram_netflix.png')
plt.show()

# Plot histogram of average rating for shows between imdb and tmdb per genre
X_axis = np.arange(len(genres))
average_rating_array_show_imdb = np.array([average_rating_shows_per_genre[key] for key in sorted(genres)])
average_rating_array_show_tmdb = np.array([average_rating_shows_per_genre_tmdb[key] for key in sorted(genres)])
plt.bar(X_axis - 0.2, average_rating_array_show_imdb, 0.4, label = 'IMDB', hatch = '////', color = 'red', edgecolor = 'black')
plt.bar(X_axis + 0.2, average_rating_array_show_tmdb, 0.4, label = 'TMDB', color = 'blue', edgecolor = 'black')
plt.xticks(X_axis, sorted(genres), rotation = 90)
plt.legend()
plt.title('Netflix - Average rating of TV shows per genre between IMDB and TMDB')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_ylim(4, 8)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('imgs/rating_show_imdb_tmdb_histogram_netflix.png')
plt.show()
'''

# box plot with number of words on title and on description for movies

number_of_words_title_movies=[]
number_of_words_description_movies = []
number_of_words_title_shows=[]
number_of_words_description_shows = []

for key in movies.keys():
    number_of_words_title_movies.append(movies[key].number_of_words_title)
    number_of_words_description_movies.append(movies[key].number_of_words_description)

for key in shows.keys():
    number_of_words_title_shows.append(shows[key].number_of_words_title)
    number_of_words_description_shows.append(shows[key].number_of_words_description)

# box plot with number of words on title for movies and shows
plt.boxplot([number_of_words_title_movies, number_of_words_title_shows], labels = ['Movies', 'TV Shows'])
plt.title('Netflix - Number of words on title for movies and TV shows')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.savefig('imgs/number_of_words_title_boxplot_netflix.png')
plt.show()

# box plot with number of words on description for movies and shows
plt.boxplot([number_of_words_description_movies, number_of_words_description_shows], labels = ['Movies', 'TV Shows'])
plt.title('Netflix - Number of words on description for movies and TV shows')
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.savefig('imgs/number_of_words_description_boxplot_netflix.png')
plt.show()
