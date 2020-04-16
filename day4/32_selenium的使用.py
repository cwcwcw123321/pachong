from selenium import webdriver

firefox=webdriver.Firefox()
firefox.get('http:www.baidu.com')

html=firefox.page_source

print(html)

firefox.quit()