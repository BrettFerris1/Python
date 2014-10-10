from datetime import datetime
import data_load
import indexer
def search(s,w):
        print("W _ ",indexer.w)
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
                filepath_list=set({})
                
                dt1=datetime.now()
                if AndCount>=1 or total==1 or AndCount==0 and OrCount==0:
                        print("\nAND SEARCH FOR\n ",Query_list)
                        
                        for query in Query_list:
                                if query in indexer.s:  #if query is in shelve
                                        found=found+1
                                        
                                        if (len(filepath_list))>0:
                                            filepath_list = filepath_list & set(indexer.s[query])
                                        else:
                                            filepath_list=set(indexer.s[query])
                                    
                                else:
                                        print("QUERY NOT FOUND!\n\n")
##                                if query in indexer.w:
##                                        found = found +1
##                                        if (len(filepath_list))>0:
##                                                filepath_list = filepath_list & set(indexer.w[query])
##                                        else:
##                                                filepath_list = set(indexer.w[query])
##                                else:
##                                        print("QUERY NOT FOUND!\n\n")
                                                

                                if found == total: #if found counter reaches the length of the query list then all values were found
                                        for paths in filepath_list:
                                                print("FOUND AT:  ", paths)


                                                                                               
                x=[]       #list of all values of query in shelf (s) 
                if (OrCount>=1 and AndCount==0):
                        
                        print("\nOR SEARCH FOR ",Query_list)
                        print("\n")
                        for query in Query_list:
                                if query in indexer.s:
                                        found=found+1
                                        x=x+list(indexer.s[query])
                                if query in indexer.w:
                                        x=x+list(indexer.w[query])
                                else:
                                       print("QUERY NOT FOUND!\n\n")
                                        
                        for paths in sorted(x):
                                print("FOUND AT: ",paths) 
                                
                        
                dt2=datetime.now()
                              
                print("\n\nTotal Search time = ",dt2.microsecond-dt1.microsecond," microsecnds")        
                                                
                again = input("do you want to play again? ")                      
           
    
