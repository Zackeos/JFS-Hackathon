from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

with open("badwords.txt", "r") as f:
    badwords = f.readlines()

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def scrape(url):
    # print(url)
    html = urllib.request.urlopen(url).read()
    allwords = text_from_html(html).split()
    # print(allwords)
    final = []
    for word in allwords:
        if word in badwords:
            final.append(word)
    percentage = round((len(final)/len(allwords))*100,2)
    print(final)
    return f"there are {len(final)} bad words that is {percentage}% of the website"


filter2 = ["a", "and", "this"]
def factcheck(urllist):
    testurl = urllist[0]
    html = urllib.request.urlopen(testurl).read()
    allwords = text_from_html(html).split()
    commonwords = []

    for word in allwords:
        if word not in filter2:
            for x in range(len(urllist)):
                html2 = urllib.request.urlopen(urllist[x]).read()
                allwords2 = text_from_html(html2).split()
                if word not in allwords2:
                    break
                if x == len(urllist) - 1:
                    commonwords.append(word)
    percentage = round((len(commonwords)/len(allwords))*100,2)

    return f"there are {len(commonwords)} words that are the same on all the websites that is {percentage}% of the keywords"

# print(scrape("https://road.cc/content/news/cycling-live-blog-29-march-2023-300243"))


# print(scrape("https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python"))