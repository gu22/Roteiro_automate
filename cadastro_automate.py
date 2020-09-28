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

##--------- Definindo o produto---

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

cidade_destino = driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[4]/td/table/tbody[2]/tr/td[2]/p[1]/span/div/a/span')
cidade_destino.click()

cidade_destino = driver.find_element_by_css_selector('#content > form > table > tbody > tr:nth-child(4) > td > table > tbody:nth-child(3) > tr > td:nth-child(2) > p:nth-child(1) > span > div > div > ul > li:nth-child(3918)')
cidade_destino.click()
