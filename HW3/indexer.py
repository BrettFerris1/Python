import data_load
import pickle
import shelve
words_dict={}
entry={}
def process_data(pickle_file,shelve_file):
    global s
    s=shelve.open(shelve_file)
    with open(pickle_file,'br') as f:
        p=pickle.load(f)
        for filepath,text in p:
            entry={text:filepath}
            words_dict.update(entry)

        for entries in words_dict: #dictionary of text:filepath
            words = entries.split()#split text into list of words
            for word in words:  #go word by word 
                r=set({})
                for y,slots in enumerate(words_dict):
                    if word in slots: #if a word is in an entry in the dictionary
                        r.add(y)    #add the slot where that entry is located to a list
                    if y==(len(words_dict)-1):#when the counter reaches the one less than the length
                        s[word]=(r)  #shelve the word and have its value be the list of slots where that word was found in the dictionary.
                        
    #my shelve has every word in all of the files and the location in the dictionary where that word can be found

    f.close()

