# from app import app
import urllib.request,json
from .models import Sources
from .models import Headlines


# Sources = sources.Sources
# Headlines = headlines.Headlines



#getting api key
apiKey = None


# getting the sources url
base_url = None
articles_base_url = None


def configure_request(app):
    global apiKey, base_url,articles_base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_URL']
    articles_base_url = app.config['NYT_ARTICLES_URL']


def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, apiKey)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        # print(get_sources_response)
        
        sources_results = None
        
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            
            
    return sources_results

def process_results(sources_list):
    '''
    function that processes the sources results and transforms them into a list of objects
    
    Args:
        sources_list: A list of dictionaries that contain sources details
        
    Returns:
        sources_results: A list of sources objects
    '''
    
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        
        sources_object = Sources(id, name, description, url, category, language, country)
        sources_results.append(sources_object)
            
    return sources_results
        
        
def get_headlines(sources):
    '''
    function that gets the json response to our url request
    '''
    get_headlines_url = articles_base_url.format(sources,apiKey)
    print(get_headlines_url)
    
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        
        print(get_headlines_response)
        
        headlines_results = None
        
        
        if get_headlines_response['articles']:
            articles_results_list = get_headlines_response['articles']
            headlines_results = process_headlines_results(articles_results_list)
            
            
    return headlines_results
    print (headlines_results)

def process_headlines_results(headlines_list):
    '''
    function that processes the sources results and transforms them into a list of objects
    
    Args:
        sources_list: A list of dictionaries that contain sources details
        
    Returns:
        sources_results: A list of sources objects
    '''
    
    headlines_results = []
    for headlines_item in headlines_list:
        id = headlines_item.get('id')
        author = headlines_item.get('author')
        title = headlines_item.get('title')
        description = headlines_item.get('description')
        url = headlines_item.get('url')
        urlToImage = headlines_item.get('urlToImage')
        publishedAt = headlines_item.get('publishedAt')
        content = headlines_item.get('content')
        
        headlines_object = Headlines(id, author, title, description, url, urlToImage, publishedAt, content)
        headlines_results.append(headlines_object)
            
    return headlines_results    
    print(headlines_results)
        
        
        
     

