import data_load
import searcher
import indexer


data_load.traverser()
d=indexer.process_data("raw_data.pickle","fortunes_shelve")
searcher.search("fortunes_shelve")




