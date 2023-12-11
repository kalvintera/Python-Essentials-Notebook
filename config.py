import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path


@dataclass
class Config:
    """
    Eine Konfigurationsklasse, die Einstellungen und Pfade für das Projekt definiert.

    Attributes:
        api_url (str): Die Basis-URL der OMDb API.
        project_path (Path): Der Pfad zum Wurzelverzeichnis des Projekts.
        input_path (Path): Der Pfad zum Verzeichnis, in dem Eingabedaten gespeichert sind.
        api_key (str): Der API-Schlüssel für die OMDb API, geladen aus einer .env-Datei.
    """

    api_url: str = "http://www.omdbapi.com/"
    project_path: Path = Path(__file__).resolve().parent
    input_path: Path = project_path.joinpath("input")
    load_dotenv(project_path.joinpath(".env"))
    api_key: str = os.getenv("API_KEY")
