from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import json
 
def browser_initial():
    """"
    浏览器初始化
    """
    os.chdir('D:\\MyDesktop')
    option=Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=option)
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://www.hdtime.org/index.php')
    return browser
 
def loginWithUsername(browser):
        username= browser.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td/form[2]/table/tbody/tr[1]/td[2]/input')
        password= browser.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td/form[2]/table/tbody/tr[2]/td[2]/input')
        username.send_keys("username")
        password.send_keys("password")
        
        browser.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td/form[2]/table/tbody/tr[8]/td/input[1]').click()

def loginWithCookies(browser):
    # with open('signcookies.txt', 'r', encoding='utf8') as f:
    #     listCookies = json.loads(f.read())
        
    listCookies='here is your cookie'
    for cookie in listCookies:
        cookie_dict = {
        "domain": cookie.get('domain'),
        "expiry": cookie.get('expiry'),
        "httpOnly":  cookie.get('httpOnly'),
        "name":  cookie.get('name'),
        "path":  cookie.get('path'),
        "secure":  cookie.get('secure'),
        "value":  cookie.get('value')
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()   
    

 
def doSign(browser):
   
    
    browser.find_element(By.XPATH,'/html/body/table[2]/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[1]/span/a[5]').click()
    # /html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/h2  //签到成功Label的Xpath
    successLabel=browser.find_element(By.XPATH,'/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/h2')
    
    print(successLabel.text)
    

        
            
    
if __name__ == "__main__":
    browser = browser_initial()
    # loginWithUsername(browser)
    loginWithCookies(browser)
    doSign(browser)