from .request import get_news
from .requests import get_news,get_news
from .requests import get_news,get_news,search_news
from flask import render_template,request,redirect,url_for
from .models import review
from .forms import ReviewForm
Review = review.Review

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_news = request.args.get('news_query')

    if search_:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

@app.route('/news/<int:author>')
def news(author):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(author)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

    @app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(author)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.author ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)

    @app.route('/news/<int:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)

    return render_template('news.html',title = title,news = news,reviews = reviews)