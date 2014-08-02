import urllib
from bs4 import BeautifulSoup
import re
import argparse


def parser():

    par = argparse.ArgumentParser()
    par.add_argument("tag_name", help="The tag name e.g python or java or re etc.")
    par.add_argument("type", help="The type of questions to find. e.g frequent or active")
    args = par.parse_args()

    if args.type.lower() in ["newest", "frequent", "active", "votes", "featured", "unanswered"]:
        overflow(args.tag_name.lower(),args.type.lower())
    else:
        print("Invalid types. Types allowed: newest\n frequent\n active\n votes\n featured\n unanswered")


def overflow(tagname, type):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=%s" % (tagname, type)
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)

    k = len(soup.findAll('a',{'class':'question-hyperlink'}))

    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n', ''))
        print(views.replace('\r\n', ''))
        print(votes+" Votes")

    elif k == 0:
        print("No posts found for this tag.")

    else:
        for i in range(0,k):
         views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[i])
         title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
         votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[i]

         print('[%d] %s   %s   %s votes ' % (i+1,title,views.replace(' ',''),votes) )
         print('\n\n')

if __name__ == '__main__':

    parser()

