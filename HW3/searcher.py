from datetime import datetime
import data_load
import indexer
def search(s):
        again="yes"

        while (again=="yes"):
                found=0
                

        #REMOVES AND/OR
                
                AndCount,OrCount = 0,0
                found_set=set([])
                Query_Set=set()
                query=input("query:")
                split_query=query.split()
                if (len(split_query) > 1):
                        while ("and" in split_query):
                                split_query.remove("and")
                                AndCount=AndCount+1
                        while ("or" in split_query):
                                split_query.remove("or")
                                OrCount=OrCount+1 
                Query_Set=set(split_query)
                Query_list=list(Query_Set)
                total=len(Query_list)

                
                found=0
                t=[]
                slot_set=set({})
                
                dt1=datetime.now()
                if AndCount>=1 or len(Query_list)==1 or AndCount==0 and OrCount==0:
                        print("\nAND SEARCH FOR\n ",Query_list)
                        
                        for query in Query_list:
                                if query in indexer.s:  #if query is in shelve
                                        found=found+1   
                                        if len(slot_set)>0: #slot_set keeps track of the places where these queries are found
                                                slot_set=indexer.s[query]&slot_set  # & is used to find intersection of those places
                                        else:
                                                slot_set=indexer.s[query]
                                       
                                if found == len(Query_list): #if found counter reaches the length of the query list then all values were found
                                        for i,value in enumerate(indexer.words_dict): #for every entry in the dictionary where the text:filepath are stored
                                                for spot in sorted(slot_set):   #for every spot in the sorted slot_set
                                                        if i==spot:             #if the element # in the dictionary == the number in our slot_set
                                                                key=value       #store the text from the dictionary into a variable
                                                                print("\n\nFOUND AT ", indexer.words_dict[key]) #use that text to find the value in the dictionary which is the path
                                
                                                       
                x=[]        
                if (OrCount>=1 and AndCount==0):
                        
                        print("\nOR SEARCH FOR ",Query_list)
                        print("\n")
                        for query in Query_list:
                                if query in indexer.s:
                                        found=found+1
                                        x=x+list(indexer.s[query])
                                        
                        for i,value in enumerate(indexer.words_dict):
                                if i in x:
                                        key=value
                                        print("\n\nFOUND AT ", indexer.words_dict[key])
                              
                dt2=datetime.now()
                              
                print("\n\nTotal Search time = ",dt2.microsecond-dt1.microsecond," microsecnds")        
                                                
                again = input("do you want to play again? ")                      
           
    
