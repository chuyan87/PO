from appium import webdriver
from search_pages.search_driver import Search_Driver
from init_driver.init_driver_open import Init_driver_open
import pytest
class Test_search():
    def setup_class(self):
        self.driver = Init_driver_open()
        self.ser_open = Search_Driver(self.driver).search()
    def teardown_class(self):
        self.ser_open.search_retue()
        self.driver.quit()
    @pytest.fixture(scope="class")
    def clik_search(self):
        self.ser_open.search_click()
    @pytest.mark.usefixtures('clik_search')
    @pytest.mark.parametrize('text',['Wi',123,'铃声'])
    def test_box(self,text):
        self.ser_open.search_send(text)


