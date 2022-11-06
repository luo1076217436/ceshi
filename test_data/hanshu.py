def login_page(user_name,password,drver):
    from selenium.webdriver.common.by import By
    drver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/input").send_keys(user_name)
    drver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/input").send_keys(password)
    drver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/button").click()

def open_url(url,drver):
    drver.get(url)
    drver.maximize_window()


def search_key(url,drver,user_name,password,key):
    open_url(url,drver)
    login_page(user_name,password,drver)
    from selenium.webdriver.common.by import By
    drver.find_element(By.XPATH, "/html/body/div[1]/aside/div/section/div[2]/ul/li[1]/ul/li[1]/a/span").click()
    import time
    time.sleep(1)
    drver.switch_to.frame(1)
    element_1 = drver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/input")
    element_1.send_keys(key)
    drver.find_element(By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[10]/a[1]/span").click()



