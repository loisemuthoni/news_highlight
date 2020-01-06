from .request import get_news
from .requests import get_news,get_news

@app.route('/news/<int:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = movie)