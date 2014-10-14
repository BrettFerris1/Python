import data_load
import pickle
import shelve
filepath_dict={}
entry={}
path_list=[]
def process_data(fortune_file,url_file):
    
    s=shelve.open("fortune_shelve")
    with open(fortune_file,'br') as f:
        p=pickle.load(f)
        for filepath,text in p:
            words = text.split()
            for word in words:
                path_list=[]
                for filepath,text in p:
                    if word in text:
                        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                        path_list.append(filepath)
                entry={word:path_list}
                filepath_dict.update(entry)
                
    with open(url_file,'br') as g:
        q=pickle.load(g)
        for filepath,text in q:
            words = text.split()
            for word in words:
                path_list=[]
                for filepath,text in q:
                    if word in text:
                        word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                        path_list.append(filepath)
                if word in filepath_dict:
                    filepath_dict[word].append(filepath)
                else:
                    
                    entry={word:path_list}
                    filepath_dict.update(entry)
                



    for key in filepath_dict:
        s[key]=filepath_dict[key]

   
    s.close()

    f.close()

