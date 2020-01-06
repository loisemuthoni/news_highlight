import os

class Config:
    '''
    General Configuration parent class
    '''
    # TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NYT_ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environment.get('SECRET_KEY')
    



class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        Config: parent configuration class with general configuration
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}