from Base.Base import Base

import search_pages


class Search_Open(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def search_click(self):
        self.click_element(search_pages.search_dfn)

    def search_send(self,text):
        self.send_element(search_pages.search_input,text)

    def search_retue(self):
        self.click_element(search_pages.search_fan_dfn)
