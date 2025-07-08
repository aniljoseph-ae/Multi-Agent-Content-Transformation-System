"""
Configuration management with environment variables
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ultrasafe_api_key: str
    ultrasafe_base_url: str = "https://api.ultrasafe.com/v1"
    chroma_db_path: str = "./chroma_db"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    """Singleton settings instance"""
    return Settings()