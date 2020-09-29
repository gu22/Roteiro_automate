# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:22:20 2020

@author: gusan
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import *
import easygui
import time



import openpyxl
from openpyxl import load_workbook
import pandas as pd
from unidecode import unidecode

## lendo dados

data = easygui.fileopenbox("Escolha o arquivo de orientacao, xmlx",default="*.xlsx")

tabela = pd.read_excel(data,2)

index = len(tabela.index)

c_origem = 2816


#------- Iniciando site
driver = webdriver.Chrome()
driver.maximize_window()
site = ('http://sistemas.dnit.gov.br/cargasperigosas')
driver.get(site)

#----------- Localizando itrns para login
# assert "Python" in driver.title
email = driver.find_element_by_id('__ac_name')
# email.clear()
email.send_keys("gustavo.dossantos@bayer.com")
# email.send_keys(Keys.TAB)

pw = driver.find_element_by_id('__ac_password')
pw.send_keys("alquimia22")
pw.send_keys(Keys.RETURN)

# time.sleep(5)

# driver.find_element_by_xpath('//*[@id="loginform"]/div[5]/input').click

#------- INicando processo de cadstro

meuperfil = driver.find_element_by_xpath('//*[@id="nav"]/span[1]/li/a/span')
meuperfil.click()

cadastrar_rotas = driver.find_element_by_xpath('//*[@id="example"]/tbody/tr[6]/td/b/span/input')
cadastrar_rotas.click()


#---------------- Cadastando Rotas ------------------------------#

##--------- Definindo o produto\origem\destino--------------

# produto = '//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/div/a/span'
# produto_liquido = 'na'

# produto.setAttribute("value", "3077 - 9 - - RESIDUO PERIGOSO, SOLIDO, N.E.")

#produto = '//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/select'
# produto = '//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/select'
# produto = '//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/select'
value = '946'
# produto = driver.find_element_by_name('id_produto')
produto = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/div/a/span')
# print("ok\n")
# time.sleep(2)
produto.click()
time.sleep(2)
# produto_texto = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/div/div/div/input')
# produto_texto.send_keys("3077")

# produto = 
# acao = driver.find_element_by_name("id_produto")
# acao.select_by_visible_text("3077 - 9 - - RESIDUO PERIGOSO, SOLIDO, N.E.")
# acao.select_by_value(value)

# element = driver.find_element_by_xpath("//select[@name='fruitType']")
# all_options = acao.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()

produto = driver.find_element_by_css_selector('#content > form > table > tbody > tr:nth-child(2) > td:nth-child(1) > span > div > div > ul > li:nth-child(916)')
produto.click()



## HINT trocar numeração li
cidade_origem = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[1]/p[1]/span/div/a/span')
cidade_origem.click()
cidade_origem = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[1]/p[1]/span/div/div/ul/li[{}]'.format(c_origem))
cidade_origem.click()

##--------------Informações em texto --------------
#liquido 918  solido 916

for i in range(index):
    
    rodovias_texto = str(tabela.iloc[i][5]) # >> seguir tabela\dados
    ano_texto = ('2019')
    nrisco_texto = ("3")
    toneladas_texto = str((int(tabela.iloc[i][3])/1000)) #>> seguir tabela\dados
    
    
    c_destino = (str(tabela.loc[i][7]).split('.')[0])
    
    if i == 0:
        cidade_destino = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[2]/p[1]/span/div/a/span')
        cidade_destino.click()
        
        cidade_destino = driver.find_element_by_css_selector('#content > form > table > tbody > tr:nth-child(4) > td > table > tbody:nth-child(3) > tr > td:nth-child(2) > p:nth-child(1) > span > div > div > ul > li:nth-child({})'.format(c_destino))
        cidade_destino.click()
           
        rodovia =  driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[3]/p[1]/input')
        ano =  driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input')
        nrisco = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[2]/td[2]/input')
        toneladas =  driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[3]/p[2]/input')
           
        rodovia.send_keys(rodovias_texto)
        
        time.sleep(5)
        ano.send_keys(ano_texto)
        nrisco.send_keys(nrisco_texto)
        toneladas.send_keys(toneladas_texto)
           
        # botao_salvarsair = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[3]/tr/td/input[1]')
        # botao_salvarsair.click()

        botao_salvarcont = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[3]/tr/td/input[2]')
        botao_salvarcont.click()
        
    else:
        
       cidade_destino = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[1]/span/div/a/span')
       cidade_destino.click()
        
       cidade_destino = driver.find_element_by_css_selector('#content > form > table > tbody > tr:nth-child(4) > td > table > tbody:nth-child(7) > tr > td:nth-child(1) > span > div > div > ul > li:nth-child({})'.format(c_destino))
       cidade_destino.click()
       
       rodovia =  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[4]/input')
       toneladas =  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[5]/input')
        
       rodovia.send_keys(rodovias_texto)
       toneladas.send_keys(toneladas_texto)
       
       add = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[8]/input')
       add.click()
       
       time.sleep(2)