import urllib.request
from urllib.error import  URLError
import re
import pickle

def visit_url(url, domain):
    global webcontent_dict 
    global crawler_backlog
    webcontent=tuple()
    content_data=[]
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            regexp_content = re.compile('<a class=.*>(?P<content>(.*))</a>{0}')

            result = regexp_title.search(content_string, re.IGNORECASE)

            if result:
                title = result.group("title")
                #print(title)

            result = regexp_keywords.search(content_string, re.IGNORECASE)

            if result:
                keywords = result.group("keywords")
                #print(keywords)

            
            result = re.findall(regexp_content, content_string)
            #print("RESULT - ",result)
            if result:
                for content in re.findall(regexp_content, content_string):
                    #print ("content - ", content)
                    content = set(content)
                    content = list(content)
                    #print ("content - ", content)
                    for word in content:
                        content_data.append(word)
                    #print ("CONTENT DATA _ ", content_data)
                

            webcontent = (url, content_data)
            #print ("web_content - ", webcontent)
                    
            webcontent_list.append(webcontent)
            #print ("content list - ", webcontent_list)
                    
                                        
            
            for (urls) in re.findall(regexp_url, content_string):
                    if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                        crawler_backlog[urls] = 0
                        visit_url(urls, domain)
    except URLError as e:
        print("error")

crawler_backlog = {}
webcontent_list = []
seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")
webdata = open("webdata.pickle",'bw')
pickle.dump(webcontent_list,webdata)
webdata.close()

