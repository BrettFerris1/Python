import data_load
import searcher
import indexer
import webcrawler


data_load.traverser()
webcrawler.webcrawler()
d=indexer.process_data("raw_data.pickle","webdata.pickle")

searcher.search("fortune_shelve")



