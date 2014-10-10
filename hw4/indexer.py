import data_load
import webcrawler
import pickle
import shelve
filepath_dict={}
entry={}

def process_data(fortunepickle_file,fortuneshelve_file,webpickle_file,urlshelve_file):
    filepath_dict={}
    entry={}
    global s
    global w
    s=shelve.open(fortuneshelve_file)
    with open(fortunepickle_file,'br') as f:
        p=pickle.load(f)
        for filepath,text in p:
            entry={filepath:text}
            filepath_dict.update(entry)

        for entry in filepath_dict:
            words=filepath_dict[entry].split()
            
            for each_word in words:
                r=[]
                for y, slots in enumerate(filepath_dict):
                    if each_word in filepath_dict[slots]:
                        r.append(slots)
                    if y==(len(filepath_dict)-1):
                        s[each_word]=(r)

    f.close()
    url_dict={}
    urlentry={}
    w=shelve.open(urlshelve_file)
    with open(webpickle_file,'br') as ff:
        pp=pickle.load(ff)
        for filepath,text in pp:
            urlentry={filepath:text}
            #print("ENTRY - ", urlentry)
            url_dict.update(urlentry)

        for entry in url_dict:
            words=str(url_dict[entry]).split()
            
            for each_word in words:
                g=[]
                for y, slots in enumerate(url_dict):
                    if each_word in list(url_dict[entry]):
                        g.append(slots)
                    if y==(len(url_dict)-1):
                        w[each_word]=(g)

                        
    ff.close()                    
    
        

   

