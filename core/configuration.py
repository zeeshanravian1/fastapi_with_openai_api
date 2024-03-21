"""
Core Configuration Module

Description:
- This module is responsible for core configuration and read values from
environment file.

"""

from pydantic_settings import BaseSettings


class CoreConfiguration(BaseSettings):
    """
    Core Settings Class

    Description:
    - This class is used to load core configurations from .env file.

    """

    CORS_ALLOW_ORIGINS: str
    CORS_ALLOW_METHODS: str
    CORS_ALLOW_HEADERS: str

    OPENAI_API_KEY: str

    PROJECT_TITLE: str = "Product Blog Project"
    PROJECT_DESCRIPTION: str = "Product Blog Project Documentation"

    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    class Config:
        """
        Config Class

        Description:
        - This class is used to configure environment variables.

        """

        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


core_configuration = CoreConfiguration()
