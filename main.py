from selenium import webdriver
from os import system
from time import sleep
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-crash-reporter")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)


def views(url):
    vidUrl = str(url)
    system("cls")
    print("Vues...")
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    sleep(2)
    system("cls")
    print("Url De la video...")
    driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/input").send_keys(vidUrl)
    sleep(2)
    system("cls")
    print("Search...")
    driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/form/div/div/button").click()
    sleep(4)
    system("cls")
    print("Envoi...")
    driver.find_element_by_xpath("/html/body/div[4]/div[5]/div/div/div[1]/div/form/button").click()
    print("Succes !!!")
    a = 190
    system("cls")
    while a != 0:
        system("cls")
        print("temps restant ",a)
        time.sleep(1)
        a = a-1
    driver.refresh()
    sleep(5)
    views()

def share(url):
    vidUrl = str(url)
    system("cls")
    print("Partage...")
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div[2]/div[5]/div/button").click()
    sleep(2)
    system("cls")
    print("Url De la video...")
    driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl)
    sleep(2)
    system("cls")
    print("Search...")
    driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button").click()
    sleep(4)
    system("cls")
    print("Envoi...")
    driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div[1]/div/form/button").click()
    print("Succes !!!")
    a = 180
    system("cls")
    while a != 0:
        system("cls")
        print("temps restant ",a)
        time.sleep(1)
        a = a-1
    driver.refresh()
    sleep(5)
    share()

def menu():
    sleep(2)
    system("cls")
    print("Tikviews || PETIT PRINCE || V1.2.4")
    url = input("Url du tiktok >> ")
    driver.get("https://zefoy.com")
    system("cls")
    print("Complete le Captcha >>")
    print("[1] Vues...")
    print("[2] Partages...")
    choice = int(input(">> "))
    if choice == 1:
        system("cls")
        print("Complete le Captcha...")
        a = 10
        while a != 0:
            print("temps restant ",a)
            time.sleep(1)
            a = a-1
        views(url)
    elif choice == 2:
        system("cls")
        print("Complete le Captcha...")
        a = 10
        while a != 0:
            print("temps restant ",a)
            time.sleep(1)
            a = a-1
        share(url)

menu()