from search_pages.search_open import Search_Open
from search_pages.search_network import Search_Network

class Search_Driver():
    def __init__(self,driver):
        self.driver = driver

    def search(self):
        return Search_Open(self.driver)
    def network(self):
        return Search_Network(self.driver)

