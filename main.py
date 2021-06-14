import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime
import webbrowser

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.add_argument('--headless')
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(options=options, executable_path=PATH)

# [Trondeim, Oslo]
cityUrls = {"Trondheim": "https://www.vg.no/spesial/corona/fylker/50/kommuner/5001/",
            "Oslo": "https://www.vg.no/spesial/corona/fylker/03/kommuner/0301/"}


def quitApp():
    driver.close()
    exit()

def wantAnotherCity():
    y = False
    while not y:
        yesOrNo = input("Do you want statistics for another city? [y/n]\n")

        if yesOrNo == "y" or yesOrNo == "Y":
            y = True
            main()
        elif yesOrNo == "n" or yesOrNo == "N":
            y = True
            quitApp()
        else:
            print("Please enter valid input! [y/n]\n")

def drawOptions():
    print("[0]: Trondheim ")
    print("[1]: Oslo")
    print("[Q]: Quit \n")

def main():
    drawOptions()
    userInput = input("What city do you want statistics from? \n")

    if userInput == "Q" or userInput == "q":
        quitApp()
    elif userInput == "0" or userInput == "1":
        getStatistics(int(userInput))

        if not wantAnotherCity():
            quitApp()
        else:
            main()
    else:
        print("Please enter a valid value! \n")
        time.sleep(1)
        main()


#def getUserInput():
#    x = False
#
#    while not x:
#        userInput = input("What city do you want statistics from? \n")
#
#        if userInput == "Q" or userInput == "q":
#            quitApp()
#        elif userInput == "0" or userInput == "1":
#            return int(userInput)
#        else:
#            print("Please enter a valid value! \n")
#            time.sleep(1)
#            getUserInput()


def getStatistics(index):
    try:
        keys_list = list(cityUrls)
        key = keys_list[index]
        url = cityUrls[key]
        driver.get(url)
        numOfInfectedTotal = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/div[2]/div[6]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[1]/div[1]")
        numOfInfectedYesterday = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/div[2]/div[6]/div[2]/div/div/div/div/div[1]/div[1]/ul/li[2]/div[1]")

        print("\nTotal infected: " + numOfInfectedTotal.text)
        print("Infected last 7 days: " + numOfInfectedYesterday.text + "\n")
    except:
        print("Something went wrong!")


print("|------- Welcome! --------|\n")
#drawOptions()
#print("|-------------------------|")

main()

#driver.close()
