import os
import re

from google_images_search import GoogleImagesSearch



# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
# define search params:
from Constants import CUSTOME_SEARCH_DEVELOPER_KEY, CUSTOME_SEARCH_CX, IMAGE_FOLDER_KEY


class ImageSpider:
    def __init__(self):
        self.gis = GoogleImagesSearch(CUSTOME_SEARCH_DEVELOPER_KEY, CUSTOME_SEARCH_CX)


    def search(self, query, number_of_results, width=500, height=500):
        _search_params = {
            'q': query,
            'num': number_of_results,
            'safe': 'off', #'high|medium|off',
  #          'fileType': 'jpg', # 'jpg|gif|png',
  #           'imgType': 'photo', # 'clipart|face|lineart|news|photo',
  #           'imgSize': 'MEDIUM', # 'huge|icon|large|medium|small|xlarge|xxlarge',
 #           'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
 #           'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
        }

        # # this will only search for images:
        # self.gis.search(search_params=_search_params)
        #
        # # this will search and download:
        # self.gis.search(search_params=_search_params, path_to_dir=DEFAULT_IMAGE_FOLDER)

        # this will search, download and resize:
        DEFAULT_IMAGE_FOLDER = "./faces"
        self.gis.search(search_params=_search_params, path_to_dir=DEFAULT_IMAGE_FOLDER)

        # # search first, then download and resize afterwards:
        # self.gis.search(search_params=_search_params)
        # for image in self.gis.results():
        #     print("===================== yes")
        #
        #     image.download(DEFAULT_IMAGE_FOLDER)


