import requests
from typing import List, Dict

from config import Config


class OmdbApiHandler:
    """
    Diese Klasse dient als Handler für die Interaktion mit der OMDB API.
    Sie ermöglicht das Abrufen von Filmdaten durch die API.
    """

    def __init__(self):
        """
        Der Konstruktor initialisiert die Instanz mit Konfigurationsdaten.
        """
        # Laden der Konfigurationsdaten, die API-Schlüssel und URL enthalten.
        self.config = Config()

    def get_movie_data_single(self, movie_title: str) -> Dict:
        """
        Ruft Daten für einen einzelnen Film anhand seines Titels ab.

        :param movie_title: Der Titel des Films, dessen Daten abgerufen werden sollen.
        :return: Ein Dictionary mit den Daten des Films oder None, falls ein Fehler auftritt.
        """
        # Parameter für die API-Anfrage vorbereiten, einschließlich des Filmtitels und des API-Schlüssels.
        parameters = {"t": movie_title, "apikey": self.config.api_key}

        # Anfrage an die OMDB API senden.
        response = requests.get(self.config.api_url, params=parameters)

        # Überprüfen des Antwortstatus und Verarbeiten der Daten.
        if response.status_code == 200:
            # Bei erfolgreicher Antwort, JSON-Daten extrahieren.
            movie_data = response.json()
        else:
            # Im Fehlerfall eine Nachricht ausgeben und 'None' zurückgeben.
            print("Something went wrong")
            movie_data = None

        return movie_data

    def get_movie_data_from_list(self, movie_list: List[str]) -> List[Dict]:
        """
        Ruft Filmdaten für eine Liste von Filmtiteln ab.

        :param movie_list: Eine Liste von Filmtiteln.
        :return: Eine Liste von Dictionaries, die jeweils die Daten eines Films enthalten.
        """
        # Liste zur Speicherung der Filmdaten.
        movie_info_list = []

        # Durchlaufen der Filmliste und Abrufen der Daten für jeden Film.
        for movie in movie_list:
            movie_info_list.append(self.get_movie_data_single(movie_title=movie))

        return movie_info_list
