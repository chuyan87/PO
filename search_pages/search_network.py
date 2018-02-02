from Base.Base import Base

import search_pages


class Search_Network(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def network(self):
        self.click_element(search_pages.search_geng)
        self.click_element(search_pages.search_move)
        self.click_element(search_pages.search_3G)
        self.click_element(search_pages.search_kuan)