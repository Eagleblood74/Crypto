#Luno, ice-cube and altcoin trader.
#Bitcoin
#https://www.luno.com
#https://ice3.com
#https://www.altcointrader.co.za

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import threading

def pull_btc_rates():

    def luno_btc():
        try:
            driver = webdriver.Chrome(executable_path='./chromedriver')
            driver.get('https://www.luno.com')
            rate = driver.find_element_by_xpath('//*[@id="o-wrapper"]/nav[1]/div/div[2]/ul[2]/li[1]/a').text  # retrieve btc luno
            rate = rate[8:]  # String formatting
            rate = rate.replace(',', '')  # String formatting
            float(rate)
            print('Luno -', rate)
            rates['LUNO'] =  rate
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            print('Failed to retrieve Luno rates')

    def ice3_btc():
        try:
            driver = webdriver.Chrome(executable_path='./chromedriver')
            driver.get('https://ice3.com/trade/btc-zar')  # retrieve btc ice3
            sleep(2)
            rate = driver.find_element_by_xpath('//*[@id="main_container"]/div/div/section/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/span').text  # retrieve btc ice3
            rate = rate.replace(',', '')  # String formatting
            float(rate)
            print('Ice3 -', rate)
            rates['ICE3'] = rate
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            print('Failed to retrieve ice3 rate')

    def altcoin_btc():
        try:
            driver = webdriver.Chrome(executable_path='./chromedriver')
            driver.get('https://www.altcointrader.co.za')  # retrieve btc Altcoin Trader
            rate = driver.find_element_by_xpath('//*[@id="trade-history"]/table/tbody/tr[2]/td[1]').text  # retrieve btc altcointrader
            float(rate)
            print('Altcoint -', rate)
            rates['ALTCOIN'] = rate
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            print('Failed to retrieve altcoin-trader rate')



    rates = {}

    t1 = threading.Thread(target=luno_btc)
    t2 = threading.Thread(target=ice3_btc)
    t3 = threading.Thread(target=altcoin_btc)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    return rates

print(pull_btc_rates())