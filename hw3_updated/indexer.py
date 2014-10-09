import data_load
import pickle
import shelve
filepath_dict={}
entry={}

def process_data(pickle_file,shelve_file):
    global s
    s=shelve.open(shelve_file)
    with open(pickle_file,'br') as f:
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

    
##    for places in s:
##        print (places)
##    for text in filepath_dict:            
##        for words in text:
##            r=set({})
##            for y,slots in enumerate(filepath_dict):
##                print (slots)
##                if word in slots: #if a word is in an entry in the dictionary
##                    r.add(filepath_dict)    #add the slot where that entry is located to a list
##                if y==(len(filepath_dict)-1):#when the counter reaches the one less than the length
##                    s[word]=(r)  #shelve the word and have its value be the list of slots where that word was found in the dictionary.
##                    
##

            
##
##        for entries in filepath_dict: #dictionary of text:filepath
##            words = entries.split()#split text into list of words
##            for word in words:  #go word by word 
##                r=set({})
##                for y,slots in enumerate(filepath_dict):
##                    if word in slots: #if a word is in an entry in the dictionary
##                        r.add(y)    #add the slot where that entry is located to a list
##                    if y==(len(filepath_dict)-1):#when the counter reaches the one less than the length
##                        s[word]=(r)  #shelve the word and have its value be the list of slots where that word was found in the dictionary.
##                        
    #my shelve has every word in all of the files and the location in the dictionary where that word can be found

   

