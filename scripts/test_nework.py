from init_driver.init_driver_open import Init_driver_open
from search_pages.search_driver import Search_Driver
from appium import webdriver
import pytest

class Test_Network():
    def setup_class(self):
        self.driver = Init_driver_open()
        self.ope = Search_Driver(self.driver).search()
        self.net = Search_Driver(self.driver).network()
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class")
    def clik_sear(self):
        self.ope.search_click()

    @pytest.mark.usefixtures('clik_sear')
    @pytest.mark.parametrize('text',['Wi',123,'铃声'])
    def test_box_001(self,text):
        self.ope.search_send(text)

    def test_return_002(self):
        self.ope.search_retue()

    def test_mobile_web_003(self):
        self.net.network()
