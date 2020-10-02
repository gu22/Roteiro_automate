# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:23:43 2020

@author: glpyz

PEGAR INFORMAÇÕES TMS


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
dt.sort()
valor = len(dt)

dt13=[]
# for i in range(13):
    
    
try:    
    for i in range(15):
        dt13.append(dt[0])
        dt.remove(dt[0])
except IndexError:
    pass

print(dt)
print("______________________")
print(dt13)
print("\n")
dt13 = ",".join(dt13)
print("______________________")
print(dt13)
print("\n")


button = easygui.msgbox("Aguarde","aguarde")

#pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[7]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
try:
    caixa_remessa = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/form/div/table/tbody/tr/td[2]/div/span/div/input')
    print("caixa acessada\n")
except:
    caixa_remessa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/form/div/table/tbody/tr/td[2]/div/span/div/input")
    print("caixa acessada except\n")

#inserindo o texto:
    
#caixa_remessa.click()    
caixa_remessa.send_keys(dt13)    
caixa_remessa.send_keys(Keys.RETURN)    
    
# try:
#     cxtexto = driver.find_element_by_name("isc_TextAreaItem_0")
#     # cxtexto = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
# except NoSuchElementException:
#     cxtexto = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div[1]/div[1]/div/form/table/tbody/tr[2]/td[2]/nobr/textarea")
# cxtexto.send_keys(dt13)
# cxtexto.send_keys(Keys.RETURN)

time.sleep(10)
controle = 1
contadori = 1
contadorf = valor
ff1 = 0
ff2 = 0
mapc = 0
print("{} contador\n\n".format(contadorf))
if button == "OK":
    while contadori <= contadorf:
        
        if controle == 14:
            dt13=[]
            # for i in range(0,13):
            #     dt13.append(dt[i])
    
            try:    
                for i in range(13):
                    dt13.append(dt[0])
                    dt.remove(dt[0])
        
            except IndexError:
                pass
            
            dt13 = ",".join(dt13)            
            print(dt)
            print("______________________")
            print(dt13)
            print("\n")
            print(contadori)
            print("\n")
            dt.sort()
            
            time.sleep(2)
            # button = easygui.msgbox("Aguarde","aguarde")
            try:
                caixa_remessa = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/form/div/table/tbody/tr/td[2]/div/span/div/input')
                print("caixa acessada\n")
                
            except:
                caixa_remessa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/form/div/table/tbody/tr/td[2]/div/span/div/input")
                print("caixa acessada\n")
            
            time.sleep(3)
            #inserindo o texto:
            #caixa_remessa.click()
            caixa_remessa.clear()
            
            #caixa_remessa.send_keys(Keys.BACKSPACE)  
            
            caixa_remessa.send_keys(dt13)    
            caixa_remessa.send_keys(Keys.RETURN)  




            # try:
            #     fechar = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[9]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
            # except NoSuchElementException:
            #     fechar = driver.find_element_by_xpath("/html/body/div[11]/div[1]/div/div[2]/img")
            # TIP inserir apagar remessas   
            
            time.sleep(5)
            
            # try:
            #     pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[7]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img").click()
            # except NoSuchElementException:
            #     pesquisa = driver.find_element_by_xpath("")
                
            # pesquisa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
            # cxtexto = driver.find_element_by_name("isc_TextAreaItem_0")
            # cxtexto.send_keys(dt13)
            # cxtexto.send_keys(Keys.RETURN)
            
            controle = 1
            # time.sleep(10)
        # if controle == 13:
        #     for i in range(1,14):
        #         rolagem = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
        #         rolagem = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/img[3]")
        #         rolagem.click()
                
        check = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[%d]/td[1]/div/span'%controle)
        arquivo = driver.find_element_by_xpath(('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[{}]/td[2]/div').format(controle)).text
        print(arquivo)
        check.click()
        
        #botão mapa
        mapa = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[6]/div/table/tbody/tr/td")
        mapa.click() 
            
        # button = easygui.msgbox("Aguarde","aguarde")
        time.sleep(10)
        # button = "OK"
        # if button == "OK":
            
        # seletor(combobox) mapa 
        while True:
            try:
                mapa_select = driver.find_element_by_xpath(("/html/body/div[{}]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/span").format(mapc))
                break
            except NoSuchElementException:
                # mapa_select = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr/td[1]/div/span")
                mapc+=1
                
        mapa_select.click() 
        
        time.sleep(10)
        # botao do trajeto/roteiro
        try:
            roteiro = driver.find_element_by_xpath(("/html/body/div[{}]/div[2]/div/div/div[2]/div/div[1]/div[5]/div/table/tbody/tr/td").format(mapc))
        except NoSuchElementException:
            roteiro = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div/div/div[2]/div/div[1]/div[5]/div/table/tbody/tr/td")
            
        roteiro.click() 
        
        # button = easygui.msgbox("Aguarde","aguarde")
        # if button == "OK":
        arquivo2 = (arquivo+".html")
        with open(arquivo2, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
                
        time.sleep(1)
        
        
        while True:
            try:
                fechar = driver.find_element_by_xpath('/html/body/div[{}]/div[1]/div/div[2]/img'.format(ff1))
                break
            except:
               ff1+=1 
                
        fechar.click()
        time.sleep(1)
        
        while True:
            try:
                fechar = driver.find_element_by_xpath('/html/body/div[{}]/div[1]/div/div[9]/div/img'.format(ff2))
                break
            except:
               ff2+=1 
       
        
        fechar.click()
        
        time.sleep(3)
        check = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[%d]/td[1]/div/span'%controle)
        check.click()
        controle += 1
        contadori += 1
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(arquivo)
            f.write("\n")
            
        
        time.sleep(1)

driver.close()
#print(driver.get_log("browser"))                                   
# assert "No results found." not in driver.page_source
 