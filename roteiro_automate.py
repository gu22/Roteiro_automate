# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:23:43 2020

@author: glpyz
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
import easygui
import time

driver = webdriver.Chrome()
site = "https://sso-tms.jdadelivers.com/sp/startSSO.ping?PartnerIdpId=https%3A%2F%2Fsts.windows.net%2Ffcb2b37b-5da0-466b-9b83-0014b67a7c78%2F&TargetResource=https://monsantoprdtms.jdadelivers.com/tm/framework/Frame.jsp"
driver.get(site)
# assert "Python" in driver.title
elem = driver.find_element_by_name('loginfmt')
# elem.clear()
elem.send_keys("gustavo.dossantos@bayer.com")
elem.send_keys(Keys.RETURN)
button = easygui.msgbox("Aguarde","aguarde")

controle = 1
contador = 50
if button == "OK":
    while controle <= contador:
        
        if controle == 14:
            controle = 2
        if controle == 13:
            for i in range(1,14):
                rolagem = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
                rolagem.click()
                
        check = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[%d]/td[1]/div/span'%controle)
        arquivo = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[%d]/td[3]/div'%controle).text
        print(arquivo)
        check.click()
           
        mapa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[11]/div/table/tbody/tr/td")
        mapa.click() 
            
        # button = easygui.msgbox("Aguarde","aguarde")
        time.sleep(10)
        # button = "OK"
        # if button == "OK":
        try:
            mapa_select = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/span")
        except NoSuchElementException:
            mapa_select = driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/span")
            
        mapa_select.click() 
        
        try:
            roteiro = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/div[5]/div/table/tbody/tr/td")
        except NoSuchElementException:
            roteiro = driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[2]/div/div[1]/div[5]/div/table/tbody/tr/td")
            
        roteiro.click() 
        
        # button = easygui.msgbox("Aguarde","aguarde")
        # if button == "OK":
        arquivo2 = (arquivo+".html")
        with open(arquivo2, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
                
        time.sleep(1)        
        fechar = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div/div[2]/img')
        fechar.click()
        time.sleep(1)
        fechar = driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[9]/div/img')
        fechar.click()
        
        time.sleep(3)
        check = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[%d]/td[1]/div/span'%controle)
        check.click()
        controle += 1
        
        time.sleep(1)

driver.close()
#print(driver.get_log("browser"))                                   
# assert "No results found." not in driver.page_source
