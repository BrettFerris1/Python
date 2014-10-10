import data_load
import searcher
import indexer
import webcrawler

data_load.traverser()
d=indexer.process_data("raw_data.pickle","fortunes_shelve","webdata.pickle","url_shelve")

searcher.search("fortunes_shelve","url_shelve")




