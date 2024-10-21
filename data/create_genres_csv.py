import csv
import sys
import ast

header = ['id']
genres_list = []

with open(sys.argv[1], 'r') as titles:
    csv_reader = csv.reader(titles)
    next(csv_reader)
    genres_set = set()

    # find all genres
    for row in csv_reader:
        genres_set = genres_set.union(set(ast.literal_eval(row[7])))

    genres_list = list(genres_set)
    header += genres_list

csv_list = [header]

with open(sys.argv[1], 'r') as titles:
    csvreader = csv.reader(titles)
    next(csvreader)

    # create csv line for each title
    for row in csvreader:
        title_list = [row[0]]
        title_genres = ast.literal_eval(row[7])

        for genre in genres_list:
            if (genre in title_genres):
                title_list.append(1)
            else:
                title_list.append(0)
        
        csv_list.append(title_list)

with open('genres.csv', 'w', newline='') as genres:
    csv_writer = csv.writer(genres)
    csv_writer.writerows(csv_list)
