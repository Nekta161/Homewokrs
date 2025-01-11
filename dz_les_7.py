from pprint import pprint

small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

search_term = input("Введите название фильма или его часть: ").lower().replace(" ", "")

found_movies = []
for movie, year in small_dict.items():
    if search_term in movie.lower():
        found_movies.append(movie)

if found_movies:
    pprint("Найденные фильмы:")
    for movie in found_movies:
        pprint(movie)
else:
    pprint("Фильмы не найдены.")

filtered_movies_list = []
filtered_movies_dict = {}
filtered_movies_list_of_dicts = []

for movie, year in small_dict.items():
    if year is not None and year > 2024:
        filtered_movies_list.append(movie)
        filtered_movies_dict[movie] = year
        filtered_movies_list_of_dicts.append({movie: year})

pprint("Названия фильмов, вышедших после 2024 года:")
for movie in filtered_movies_list:
    pprint(movie)

pprint("\nСписок названий фильмов:")
pprint(filtered_movies_list)

pprint("\nСловарь фильмов:")
pprint(filtered_movies_dict)

pprint("\nСписок словарей фильмов:")
pprint(filtered_movies_list_of_dicts)
