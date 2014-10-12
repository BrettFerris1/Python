import data_load
import pickle
import shelve
filepath_dict={}
entry={}
def process_data(fortune_file,url_file):
    
    s=shelve.open("fortune_shelve")
    with open(fortune_file,'br') as f:
        p=pickle.load(f)
        for filepath,text in p:
            words = text.split()
            for word in words:
                entry={word:filepath}
                filepath_dict.update(entry)
                
    with open(url_file,'br') as g:
        q=pickle.load(g)
        for filepath,text in q:
            words = text.split()
            for word in words:
                entry={word:filepath}
                filepath_dict.update(entry)
                



    for key in filepath_dict:

        s[key]=filepath_dict[key]

   
    s.close()

    f.close()

