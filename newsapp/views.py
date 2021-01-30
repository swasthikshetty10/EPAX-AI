from django.shortcuts import render
from . import theindianexpress as news
from . import e_sports
from . import hackernews  as hn
# Create your views here.
valid_urls = ['https://indianexpress.com/section/india/',
              'https://indianexpress.com/section/sports/',
              'https://indianexpress.com/section/cities/',
              'https://indianexpress.com/section/entertainment/',
              'https://indianexpress.com/section/lifestyle/',
              ]
def home(request):
    titles , links , dates , descriptions , images = news.news_articles('https://indianexpress.com/section/india/page/0/')
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    num = 1


    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'newsapp/home.html' ,stuff_for_frontend )


def hackerarticle(request):
    link = request.POST.get('hackerarticle_')
    p,q,r = hn.full_article(link)
    print(link)
    final_posting = []
    final_posting.append([p,q,r])
    stuff_for_frontend = {
        'final_postings': final_posting,
        
    }
    return render(request, 'news.html' ,stuff_for_frontend)


def article(request):
    link = request.POST.get('article_')
    p,q,r,s = news.full_news(link)
    print(link)
    final_posting = []
    final_posting.append([p,q,r,s])
    num = 1
    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }
    return render(request, 'news.html' ,stuff_for_frontend)


def earticle(request):
    link = request.POST.get('article_')
    title , date , image , body = e_sports.full_news(link)
    print(link)
    final_posting = []
    final_posting.append([title , date , image , body])
    num = 1
    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }
    return render(request, 'esportsnews.html' ,stuff_for_frontend)


def sports(request):
    titles_S , links_S , dates_S , descriptions_S , images_S = news.news_articles('https://indianexpress.com/section/sports/page/0/')
    final_posting = []
    for i in range(len(titles_S)):
        final_posting.append((titles_S[i] , links_S[i] , dates_S[i] , descriptions_S[i] , images_S[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'newsapp/sports.html' ,stuff_for_frontend )


def esports(request):
    titles, links ,dates, descriptions ,images  = e_sports.allarticles('https://esportsobserver.com/tag/india/')
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'newsapp/esports.html' ,stuff_for_frontend )



def entertainment(request):
    return render(request , 'entertainment.html' )

def lifestyle(request):
    titles , links , dates , descriptions , images = news.news_articles(valid_urls[4])
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'newsapp/lifestyle.html' ,stuff_for_frontend )


def cities(request):
    titles , links , dates , descriptions , images = news.news_articles(valid_urls[2])
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'newsapp/cities.html' ,stuff_for_frontend )

def hackernews(request):
    a,b,c,d,e = hn.article('https://thehackernews.com/')
    finalposting = []
    for i in range(len(a)):
        finalposting.append([a[i], b[i], c[i][0:250],d[i], e[i]])
    stuff_for_frontend = {
        'final_postings' : finalposting,
    
    }
    print(stuff_for_frontend)
    return render(request , 'hackernews.html' , stuff_for_frontend)



def pages(request , val   , num ):
    if val == 'home':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/india/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'newsapp/home.html' ,stuff_for_frontend )
    elif val == 'sports':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'newsapp/sports.html' ,stuff_for_frontend )
    
    elif val == 'lifestyle':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'newsapp/lifestyle.html' ,stuff_for_frontend )
    
    elif val == 'cities':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'newsapp/cities.html' ,stuff_for_frontend )
    elif val == 'esports':
        
        titles , links , dates , descriptions , images = e_sports.allarticles(f'https://esportsobserver.com/tag/india/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'newsapp/esports.html' ,stuff_for_frontend )