#How to run it on cli
# 1) clone the file wiki.py
# 2)make sure already installed wikipedia-api package
# Also make sur to download wiki.txt file and keep it in same folder as wiki.py
# 3) python3 wiki.py -> command on cli 

import sys
import wikipediaapi

def searchWikiLinks(wordtoSearch):
    
    wiki_wiki = wikipediaapi.Wikipedia('en')
    filename = "wikiLinks.txt"
    page_py = wiki_wiki.page(wordtoSearch)

    try:
        pageURL = page_py.fullurl
        f = open(filename,  "r")
    
         #If the link already exists in file then we do not re-enter the file link    
        if pageURL in f.read():
            print("This link already exists")
        else:
            file1 = open(filename, "a")  # append mode
            file1.write(pageURL + " \n")
            file1.close()
            print("Link Added", pageURL)
        
         #if no wiki url is found about the keyword      
    except KeyError as ee:
        print("Key Error : try new keyword")
        
        
if __name__ == '__main__':
    search_key = ' '
    
    if len(sys.argv) == 1:
            search_keyword = input("Search key? ")
    else:
            search_keyword = search_key.join(sys.argv[1:])
    searchWikiLinks(search_keyword)
