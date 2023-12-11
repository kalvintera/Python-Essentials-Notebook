from typing import List


class DataProcessor:
    """
    Die Klasse DataProcessor ist dafür zuständig, Datenlisten zu verarbeiten.
    Sie bietet Funktionen, um bestimmte Merkmale (Features) aus den Daten zu extrahieren
    und spezielle Aufbereitungen wie die Verarbeitung von Bewertungen durchzuführen.
    """

    def __init__(self, features_list: List):
        """
        Initialisiert eine neue Instanz von DataProcessor.
        :param features_list: Eine Liste von Merkmalen, die aus den Daten extrahiert werden sollen.
        """
        self.features_list = features_list

    def list_from_selected_features(
        self,
        movie_data_list: List,
    ) -> List:
        """
        Erzeugt eine Liste von Filmen, die nur ausgewählte Features enthalten.

        :param movie_data_list: Eine Liste von Filmen, wobei jeder Film als Dictionary repräsentiert wird.
        :return: Eine Liste von Dictionaries, die nur die ausgewählten Features enthalten.
        """

        # Initialisieren der Liste, die die gefilterten Filme aufnimmt
        movies_with_selected_features_list = []

        # Überprüfen, ob die Feature-Liste vorhanden ist
        if self.features_list:
            # Durchgehen jedes Films in der Liste
            for movie_dict in movie_data_list:
                # Das Dictionary 'filtered_movie_dict' sollte
                # für jeden Film zurückgesetzt werden, um Duplikate zu vermeiden.
                # Aktuell behält es die Daten vom vorherigen Film.
                filtered_movie_dict = {}
                for feature in self.features_list:
                    if feature in movie_dict.keys():
                        filtered_movie_dict[feature] = movie_dict[feature]

                movies_with_selected_features_list.append(filtered_movie_dict)
            return movies_with_selected_features_list
        else:
            print("Features list is empty.")

    # List comprehension Beispiel
    def list_comprehension_from_select_features(
        self,
        movie_data_list: List,
    ) -> List:
        """
        Erzeugt eine Liste von Filmen mit ausgewählten Features, nutzt dafür List Comprehension.

        :param movie_data_list: Eine Liste von Filmen, wobei jeder Film als Dictionary repräsentiert wird.
        :return: Eine Liste von Dictionaries, die nur die ausgewählten Features enthalten.
        """
        # Initialisieren der Liste, die die gefilterten Filme aufnimmt
        movies_with_selected_features_list = []

        # Überprüfen, ob die Feature-Liste vorhanden ist
        if self.features_list:
            # Durchgehen jedes Films in der Liste
            for movie_dict in movie_data_list:
                filtered_movie_dict = {
                    key: value
                    for key, value in movie_dict.items()
                    if key in self.features_list
                }

                movies_with_selected_features_list.append(filtered_movie_dict)
            return movies_with_selected_features_list
        else:
            print("Features list is empty.")

    @staticmethod
    def process_ratings(movie_list: List):
        """
        Verarbeitet die Bewertungen in einer Liste von Filmen.

        :param movie_list: Eine Liste von Filmen.
        :return: Die Liste von Filmen, wobei die Bewertungen in einem speziellen Format aufgenommen sind.
        """

        for movie in movie_list:
            ratings_dict = {}
            if "Ratings" in movie.keys() and type(movie_list) == list:
                for rating in movie["Ratings"]:
                    ratings_dict[str(rating["Source"]) + " Rating"] = rating["Value"]
                    movie.update(ratings_dict)
                del movie["Ratings"]

        return movie_list

    @staticmethod
    def process_ratings_list_comprehension(movie_list: List):
        """
        Verarbeitet die Bewertungen in einer Liste von Filmen, nutzt dafür List Comprehension.

        :param movie_list: Eine Liste von Filmen.
        :return: Die Liste von Filmen, wobei die Bewertungen in einem speziellen Format aufgenommen sind.
        """

        for movie in movie_list:
            if "Ratings" in movie.keys() and type(movie_list) == list:
                movie.update(
                    {str(key) + " Rating": value for key, value in movie.items()}
                )
                del movie["Ratings"]
        return movie_list
