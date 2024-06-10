
import json

netflix = []
with open('netflix_titles.tsv', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        netflix.append(line.split("\t"))

header = netflix[0]
new_netflix = netflix[1:]

title_index = header.index('PRIMARYTITLE')
director_index = header.index('DIRECTOR')
cast_index = header.index('CAST')
genre_index = header.index('GENRES')
start_year_index = header.index('STARTYEAR')

hw02_output = []


for line in new_netflix:
    start_year = line[start_year_index]
    decade = (int(start_year) // 10) * 10 

    new_dictionary = {
        "title": line[title_index],
        "directors": line[director_index].split(",") if line[director_index] else [],
        "cast": line[cast_index].split(",") if line[cast_index] else [],
        "genres": line[genre_index].split(",") if line[genre_index] else [],
        "decade": decade
    }    
    hw02_output.append(new_dictionary)

with open("hw02_output.json", mode="w", encoding="utf-8") as output_file:   
    json.dump(hw02_output, output_file, ensure_ascii=False, indent=4)