# import urllib2
# import simplejson
# import cStringIO

# fetcher = urllib2.build_opener()
from image_spider import ImageSpider

searchTerm = 'face image'
google_spider = ImageSpider()
google_spider.search(searchTerm, 1500)
print("Finished")
