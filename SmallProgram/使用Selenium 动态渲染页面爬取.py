
# 7.1 Selenium的使用

### 基本使用
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
"""
browser = webdriver.Chrome()
try:
    browser.get('https:www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    #print(browser.get_cookies())
    #print(browser.page_source)
finally:
    browser.close()
    print('success')
"""
### 单个节点
'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
#print(browser.page_source)
#browser.close()
#input_first = browser.find_element_by_id('q')
#input_second = browser.find_element_by_css_selector('#q')
#input_third = browser.find_element_by_xpath('//*[@id="q"]')
#print(input_first,input_second,input_third)
input_forth = browser.find_element(By.ID,'q')
print(input_forth)
browser.close()
'''
### 多个节点
"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
"""

### 节点交互
'''
import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('短袖')
button = browser.find_element_by_class_name('btn-search')
button.click()
'''


### 动作链
"""
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
"""

### 执行 JavaScript
'''
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#下面是方法二
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
browser.execute_script('alert("To Bottom")')#提示框

'''

# 9 获取节点信息
from selenium import webdriver
from selenium.webdriver import ActionChains


#browser = webdriver.Chrome()
#url = 'https://www.zhihu.com/explore'
#browser.get(url)

### 获取属性
#logo = browser.find_element_by_id('zh-top-link-logo')
#print(logo)
#print(logo.get_attribute('class'))

### 获取文本
'''
input = browser.find_element_by_class_name('zu-top-add-question')
#input = browser.find_element_by_class_name('zu-top-link-logo')
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()
'''

### 切换Frame
'''
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:#try可以用于捕获异常，配合expect使用
    logo = browser.find_element_by_class_name('logo')
except Exception:
    #print(Exception)
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
'''

# 11 延时等待

### 隐式等待
'''
browser = webdriver.Chrome()
browser.implicitly_wait(10)
url = 'http://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
print(input)
'''
### 显式等待
'''
browser = webdriver.Chrome()
url = 'http://www.taobao.com'
browser.get(url)
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print("input:",input,'input.text:',input.text,'button:',button,'button.text:',button.text,sep='\n')
'''

# 12 前进和后退
'''
browser = webdriver.Chrome()
url1 = 'http://www.taobao.com'
url2 = 'http://www.zhihu.com/explore'
url3 = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url1)
browser.get(url2)
browser.get(url3)
browser.back()
time.sleep(3)
browser.forward()
time.sleep(1)
browser.close()
'''

# 13 Cookies
"""
browser = webdriver.Chrome()
url = 'http://www.zhihu.com/explore'
browser.get(url)
print(browser.get_cookies())

browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
"""

# 14 选项卡管理
"""
browser = webdriver.Chrome()
url = 'http://www.baidu.com'
browser.get(url)

browser.execute_script('window.open()')
print(browser.window_handles)

browser.switch_to_window(browser.window_handles[1])

browser.get('https://www.taobao.com')
time.sleep(2)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.zhihu.com/explore')
time.sleep(1)
"""

# 15 异常处理

### 以下是异常的代码，没有找到"hello"元素节点
#browser = webdriver.Chrome()
#url = 'http://www.baidu.com'
#browser.get(url)
#browser.find_element_by_id("hello")


### 以下是如何捕获异常
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('TIME OUT')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('NO ELEMENT')
finally:
    browser.close()
