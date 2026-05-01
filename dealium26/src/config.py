from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    app_name: str = "Dealium26"
    supported_languages: tuple[str, ...] = ("en", "hi", "te")
    default_language: str = os.getenv("DEFAULT_LANGUAGE", "en")


CONFIG = AppConfig()
