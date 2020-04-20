from selenium import webdriver

firefox=webdriver.Firefox()
firefox.get('https://cn.bing.com/')
firefox.find_element_by_id(sb_form_q).send_keys('python')
firefox.find_element_by_id("sb_form_go").click()
html=firefox.page_source
firefox.quit()


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# #chrome = webdriver.Chrome(chrome_options=options)
# chrome = webdriver.Chrome()