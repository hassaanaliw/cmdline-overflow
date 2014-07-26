import urllib
from BeautifulSoup import BeautifulSoup
import re
import argparse
from tabulate import tabulate

def parser():

    par = argparse.ArgumentParser()
    par.add_argument("tag_name",help="The tag name e.g python or java or re.")
    par.add_argument("type",help="Newest,featured")
    args = par.parse_args()

    if args.type.lower() == "newest":
        newest(args.tag_name)
    elif args.type.lower() == "frequent":
        frequent(args.tag_name)
    elif args.type.lower() == "votes":
        votes(args.tag_name)

    elif args.type.lower() == "featured":
        featured(args.tag_name)
    elif args.type.lower() == "active":
        active(args.tag_name)
    elif args.type.lower() == "unanswered":
        unanswered(args.tag_name)
    else:
        print("Invalid types. Types allowed: newest\n frequent\n active\n votes\n featured\n unanswered")




def newest(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=newest" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    k = len(soup.findAll('a',{'class':'question-hyperlink'}))

    if k == 1:
        votes = (re.search(r'<strong>(.*)</strong>',str(soup.find('span',{'class':'vote-count-post '}).contents[0]))).group(1)
        views = str(soup.find('div',{'class':'views '}).contents[0])
        title = str(soup.find('a',{'class':'question-hyperlink'}).contents[0])

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
        print("No posts found for this tag.")


    else:
     for i in range(0,k):
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
        views = str(soup.findAll('div',{'class':'views '})[i].contents[0]).replace('\r\n','')
        votes = (re.search(r'<strong>(.*)</strong>',str(soup.findAll('span',{'class':'vote-count-post '})[i].contents[0]))).group(1)+" votes"

        print('[%d] %s   %s   %s ' % (i+1,title,views.replace(' ',''),votes) )
        print('\n\n')

        #table = [['[%d]' % i,title,views,votes]]
        #print(tabulate(table))

def frequent(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=frequent" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)

    k = len(soup.findAll('a',{'class':'question-hyperlink'}))

    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
        print("No posts found for this tag.")




    else:
        for i in range(0,k):
         views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[i])
         title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
         votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[i]

         print('[%d] %s   %s   %s votes ' % (i+1,title,views.replace(' ',''),votes) )
         print('\n\n')



def votes(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=votes" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    k = len(soup.findAll('a',{'class':'question-hyperlink'}))




    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
        print("No posts found for this tag.")

    else:
        for i in range(0,k):
         views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[i])
         title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
         votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[i]

         print('[%d] %s   %s   %s votes ' % (i+1,title,views.replace(' ',''),votes) )
         print('\n\n')

def active(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=active" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    k = len(soup.findAll('a',{'class':'question-hyperlink'}))




    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
        print("No posts found for this tag.")

    else:
        for i in range(0,k):
         views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[i])
         title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
         votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[i]

         print('[%d] %s   %s   %s votes ' % (i+1,title,views.replace(' ',''),votes) )
         print('\n\n')

def unanswered(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=unanswered" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    k = len(soup.findAll('a',{'class':'question-hyperlink'}))




    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
        print("No posts found for this tag.")

    else:
        for i in range(0,k):
         views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[i])
         title = str(soup.findAll('a',{'class':'question-hyperlink'})[i].contents[0]).replace('\n','')
         votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[i]

         print('[%d] %s   %s   %s votes ' % (i+1,title,views.replace(' ',''),votes) )
         print('\n\n')

def featured(tagname):
    link = "https://stackoverflow.com/questions/tagged/%s?sort=featured" % tagname
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    k = len(soup.findAll('a',{'class':'question-hyperlink'}))




    if k == 1:
        views = str(re.findall(r'\s+<div class="views .*?" title=(.*)>',html)[0])
        title = str(soup.findAll('a',{'class':'question-hyperlink'})[0].contents[0]).replace('\n','')
        votes = re.findall(r'<span class="vote-.*><strong>(.*?)</strong>',html)[0]

        print(title.replace('\n',''))
        print(views.replace('\r\n',''))
        print(votes+" Votes")

    elif k == 0 :
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

