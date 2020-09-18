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


time.sleep(8)

try:
    smart = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div[1]/table/tbody[2]/tr/td/div/table/tbody/tr[1]/td/a[2]")
    smart.click()
except NoSuchElementException:
    pass


dt = easygui.enterbox(msg='Enter something.', title=' ', default='', strip=True)
dt = dt.split(",")

dt13=[]
for i in range(0,13):
    dt13.append(dt[i])
    
try:    
    for i in range(0,13):
        dt.remove(dt[i])
except IndexError:
    pass

print(dt)
print("______________________")
print(dt13)
print("")
dt13 = ",".join(dt13)
print("______________________")
print(dt13)


button = easygui.msgbox("Aguarde","aguarde")

pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[7]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
try:
    cxtexto = driver.find_element_by_name("isc_TextAreaItem_0")
    # cxtexto = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
except NoSuchElementException:
    cxtexto = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div[1]/div[1]/div/form/table/tbody/tr[2]/td[2]/nobr/textarea")
cxtexto.send_keys(dt13)
cxtexto.send_keys(Keys.RETURN)

time.sleep(20)
controle = 1
contadori = 1
contadorf = 39
if button == "OK":
    while contadori <= contadorf:
        
        if controle == 14:
            dt13=[]
            for i in range(0,13):
                dt13.append(dt[i])
    
            try:    
                for i in range(0,13):
                    dt.remove(dt[i])
            except IndexError:
                pass
            
            dt13 = ",".join(dt13)            
            print(dt)
            print("______________________")
            print(dt13)
            print("")
            
            
            
            fechar = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[9]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
            time.sleep(5)
            pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[7]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
            # pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
            cxtexto = driver.find_element_by_name("isc_TextAreaItem_0")
            cxtexto.send_keys(dt13)
            cxtexto.send_keys(Keys.RETURN)
            
            controle = 1
            time.sleep(20)
        # if controle == 13:
        #     for i in range(1,14):
        #         rolagem = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
        #         rolagem = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
        #         rolagem.click()
                
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
        contadori += 1
        time.sleep(1)

driver.close()
#print(driver.get_log("browser"))                                   
# assert "No results found." not in driver.page_source
