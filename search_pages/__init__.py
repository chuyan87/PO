from selenium.webdriver.common.by import By
'''设置中搜索框的元素属性值'''
search_dfn = (By.ID,"com.android.settings:id/search")
search_input = (By.ID,"android:id/search_src_text")
search_fan_dfn = (By.CLASS_NAME,"android.widget.ImageButton")
'''设置中更多按钮操作元素属性值'''
search_geng = (By.XPATH,"//*[contains(@text,'更多')]")
search_move = (By.XPATH,"//*[contains(@text,'移动网络')]")
search_3G = (By.XPATH,"//*[contains(@text,'首选网络')]")
search_kuan = (By.XPATH,"//*[contains(@text,'3G')]")





