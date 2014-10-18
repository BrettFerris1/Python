from datetime import datetime
import data_load
import indexer
import shelve
import weather
def search(shelve_file):
        print("SEARCHER")
        again="yes"
        s=shelve.open("fortune_shelve")
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
                slot_set=set({})
                
                dt1=datetime.now()
                if AndCount>=1 or total==1 or AndCount==0 and OrCount==0:
                        print("\nAND SEARCH FOR\n\n ",Query_list)
                        
                        for query in Query_list:
                                if query in s:  #if query is in shelve
                                        found=found+1
                                        if len(slot_set)>0:
                                                slot_set=set(s[query])&slot_set
                                                
                                        else:
                                                slot_set=set(s[query])
                                if found == len(Query_list):
                                        for spots in list(slot_set):
                                                print("FOUND AT : ", spots)
                                        
                                                                                        
                x=[]
                if (OrCount>=1 and AndCount==0):
                        
                        print("\nOR SEARCH FOR ",Query_list)
                        print("\n")
                        for query in Query_list:
                                if query in s:
                                        for paths in set(s[query]):
                                                x.append(paths)


                        for spots in set(x):
                                print("\nFOUND AT ", spots)
                                        
                        
                dt2=datetime.now()
                weather.weather(Query_list)              
                print("\n\nTotal Search time = ",dt2.microsecond-dt1.microsecond," microsecnds")        
                                                
                again = input("do you want to play again? ")                      
           
    
