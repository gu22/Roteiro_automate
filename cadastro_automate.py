# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:22:20 2020

@author: gusan
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *
import easygui
import time

#------- Iniciando site
driver = webdriver.Chrome()
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
----------------------------------------------------------------------------
#------- INicando processo de cadstro


#---------------- Cadastando Rotas ------------------------------
produto_solido = '//*[@id="content"]/form/table/tbody/tr[2]/td[1]/span/div/a/span'
produto_liquido = 'na'


