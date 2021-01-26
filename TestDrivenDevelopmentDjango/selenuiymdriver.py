from selenium import webdriver

wd = webdriver.Chrome(executable_path=r"C:\Users\shubham\Downloads\chromedriver_win32\chromedriver.exe")
wd.get('http://localhost:8000/')
assert wd.page_source.find("Congratulations")