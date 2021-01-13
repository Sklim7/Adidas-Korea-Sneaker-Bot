#Auto Sneaker Purchaser by Seungkwon Lim
#program used for personal purchase only. 
#element id, class name, xpath found using developer tools in chrome. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#using chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH) 

#login link
driver.get("https://shop.adidas.co.kr/PF0608011.action?checkbtn=fromTop&returnURL=https://shop.adidas.co.kr/adiMain.action")

#debouncing 
time.sleep(1)

#ID and Password
driver.find_element_by_id ('MEM_ID').send_keys('ID')
driver.find_element_by_id("MEM_PW").send_keys('passsword')
driver.find_element_by_class_name("btn-ctm.btn-blue.anim").click()


#debouncing
time.sleep(3)

#llink to specific sneaker 
driver.get("https://shop.adidas.co.kr/PF020401.action?PROD_CD=EG4958&NFN_ST=Y")

#debouncing 
time.sleep(5)

#size US 9
driver.find_element_by_xpath('/html/body/div[11]/div[6]/div/div[3]/div[1]/div[3]/div[2]/div/div[5]/div/div[1]/ul/li[10]').click()


#Buy Now button 
driver.find_element_by_xpath('/html/body/div[11]/div[6]/div/div[3]/div[1]/div[3]/div[2]/div/div[6]/a[1]').click()

#debouncing 
time.sleep(1)

#Terms and Conditions
driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/form/div/div/div[1]/div[3]/div[3]/div[1]/div/label/a').click()

#debouncing 
time.sleep(1)



#Payment option continued(kakao Pay)
driver.find_element_by_xpath('/html/body/div[3]/div[6]/div/form/div/div/div[1]/div[3]/div[4]/a').click()


