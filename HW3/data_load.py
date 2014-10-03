import os
import shutil
import fnmatch
import pickle

def traverser():
        entry=list()
        data=list()
        start_dir = "fortune1"
        out = open("raw_data.pickle",'bw')
        for dirpath, dirs, files in os.walk(start_dir):
                for single_file in files:
                    if fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log"):
                            filepath=os.path.abspath(os.path.join(dirpath,single_file))
                            #print (filepath)
                            with open(filepath,'r') as f:
                                    text=f.read()
                                    entry=(filepath,text)
                         
                            print("\nCreating entry with ",single_file, "content and ",filepath)
                            data.append(entry)
                            

        pickle.dump(data,out)                    
        f.close()
        out.close()




    
