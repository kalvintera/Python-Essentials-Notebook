from typing import List
from api.get_data import OmdbApiHandler
from processor.process_data import DataProcessor


def pretty_print(data_list: List) -> None:
    """
    Druckt Elemente einer Liste in einem formatierten Format aus.

    Args:
        data_list (List): Eine Liste von Daten, die gedruckt werden sollen.
    """
    for data in data_list:
        print(data, "\n")


def run():
    """
    Hauptfunktion, die den Prozess des Abrufens und Verarbeitens von Filmdaten steuert.
    """
    # Instanziere die Klassen zur Interaktion mit der API und zur Datenverarbeitung
    movie_api = OmdbApiHandler()
    processor = DataProcessor(
        features_list=[
            "Title",
            "Year",
            "Released",
            "Runtime",
            "Genre",
            "Plot",
            "Country",
            "Awards",
            "Ratings",
            "BoxOffice",
        ]
    )

    # Abrufen von Filmdaten
    movie_info_all_list = movie_api.get_movie_data_from_list(
        movie_list=["Barbie", "Oppenheimer", "Shinning", "Mission Impossible"]
    )

    # Verarbeite die Daten, um ausgewählte Features zu erhalten: nested loops Beispiel
    movies_with_selected_features_list = processor.list_from_selected_features(
        movie_data_list=movie_info_all_list
    )
    # list comprehension Variante
    movies_with_selected_features_list = (
        processor.list_comprehension_from_select_features(
            movie_data_list=movie_info_all_list
        )
    )
    # usage: pretty_print(data_list=movies_with_selected_features_list)
    # filter Daten based on a list
    movie_list_with_processed_ratings = processor.process_ratings(
        movie_list=movies_with_selected_features_list
    )
    # list comprehension Variante von process_ratings Funktion
    movie_list_with_processed_ratings = processor.process_ratings_list_comprehension(
        movie_list=movies_with_selected_features_list
    )
    # Zeige die verarbeiteten Daten
    pretty_print(data_list=movies_with_selected_features_list)


if __name__ == "__main__":
    run()
