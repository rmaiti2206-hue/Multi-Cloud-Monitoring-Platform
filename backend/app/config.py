from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
 secret_key:str='CHANGE_ME';database_url:str='postgresql+psycopg2://postgres:postgres@localhost:5432/multicloud';aws_default_region:str='ap-south-1';prometheus_url:str='http://localhost:9090';grafana_url:str='http://localhost:3000';model_config=SettingsConfigDict(env_file='.env',extra='ignore')
settings=Settings()
