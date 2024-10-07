from utils.startup import startHtml
from utils.extractPrice import extractPriceFromText
from utils.extractRating import getRating
import pandas as pd

Burl = 'https://books.toscrape.com/'

Bheader = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

def getArticle(article):
    title = article.find('h3').find('a')['title']
    textPrice = article.find('p',attrs={'class':'price_color'}).text
    price = extractPriceFromText(textPrice)
    textRating = article.find('p',attrs={'class':'star-rating'}).attrs
    rating = getRating(textRating['class'][1])

    
    print()

    articleData={
        'title': title,
        'price': float(price),
        'rating': rating
    }

    print(articleData)
    return articleData
if __name__=="__main__":
    htmlData = startHtml(Burl, Bheader)
    articles = htmlData.find_all('article', attrs={"class":"product_pod"})

    for ar in articles:
        getArticle(ar)


    allArticle = [getArticle(ar) for ar in articles]
    pdArticle = pd.DataFrame(allArticle)

    print(pdArticle)

    ar3Rating = pdArticle.groupby('rating')
    total = ar3Rating['price'].sum()
    print(total)
    print()
    minPrice = ar3Rating['price'].min()
    print(minPrice)
    print()
    avgPrice = ar3Rating['price'].sum()/len(ar3Rating)
    print(avgPrice)


    pdArticle.to_csv('article.csv')