import requests
from bs4 import BeautifulSoup
import sys
ratings = []
movie_name = str(sys.argv[1])
search_url = ('https://www.imdb.com/find?q=' +
              movie_name + '&s=tt&ref_=fn_al_tt_mr')
search_response = requests.get(search_url)
search_filter = BeautifulSoup(search_response.content, 'html.parser')
Response_movie = search_filter.find_all("td", {"class": "result_text"})
for tag in Response_movie:
    print('\n')
    print('Name : ' + tag.contents[1].text)
    movie_tag = tag.contents[1]['href']
    rating_url = 'https://www.imdb.com' + movie_tag + '?ref_=fn_tt_tt_1'
    rating_response = requests.get(rating_url)
    rating_filter = BeautifulSoup(rating_response.content, 'html.parser')
    rating = rating_filter.find('span', {'itemprop': 'ratingValue'})
    if rating is None:
        print('Currently No Ratings')
    else:
        print(rating.text + ' Out of 10')
        rating = float(rating.text)
        ratings.append(rating)
avg = sum(ratings) / len(ratings)
print('\n')
print('Average is', avg)
