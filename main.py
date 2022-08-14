from random import randint
from threading import Thread
from time import sleep
from selenium import webdriver





def run(firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex):
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
        
    for numbers in mainList:
        def tryAccount():
            driver = webdriver.Chrome(executable_path='./chromedriver.exe')
            for number in numbers:
                print(number)
            
        t = Thread(target=tryAccount)
        t.start()
    
    print({firstNum, secondNum, totalTabs, totalAccount, prefix, newPass, customPass, passwordIndex})