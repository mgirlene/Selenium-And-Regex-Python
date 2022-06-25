
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebScraping:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://portal.ifrn.edu.br/'
        self.input_search = 'searchGadget'
        self.button_search = 'searchButton'


    def navigate(self):
        self.driver.get(self.url)
    
    def noticias_nadic(self):
        links = []
        input_search = self.driver.find_element(By.ID, self.input_search)
        input_search.send_keys('nadic')
        self.driver.find_element(By.CLASS_NAME, self.button_search).click()
        
        link = self.driver.find_elements(By.TAG_NAME, 'a') 
        for i in link: 
            if "dados-e-inteligencia-computacional" in i.get_attribute('href'):
                links.append(i.get_attribute('href')) 
                
        noticia1 = links[0]
        self.driver.get(noticia1)
        
        texto_noticia1 = self.driver.find_elements(By.TAG_NAME, 'body')
        for i in texto_noticia1:
            arquivo = open('noticia1.txt','w')
            arquivo.write(i.text)
            arquivo.close()
        
        noticia2 = links[1]
        self.driver.get(noticia2)
        texto_noticia2 = self.driver.find_elements(By.TAG_NAME, 'body')
        
        for i in texto_noticia2:
            arquivo = open('noticia2.txt','w')
            arquivo.write(i.text)
            arquivo.close()
        
        noticia3 = links[3]
        self.driver.get(noticia3)
        texto_noticia3 = self.driver.find_elements(By.TAG_NAME, 'body')
        for i in texto_noticia3:
            arquivo = open('noticia3.txt','w')
            arquivo.write(i.text)
            arquivo.close()
    
    

def regex_txt1():
    with open('noticia1.txt', 'r') as f:  
        texto = f.read()
        
    dict_noticia1 = {}
        
    regex_titulo_noticia =  re.compile('NADIC\n([A-zÀ-ú ]+)', re.DOTALL)
    dict_noticia1["titulo_noticia"] = re.search(regex_titulo_noticia, texto).group(1)
    
    regex_data_noticia = re.compile('\n([0-9\/]+)', re.DOTALL)
    dict_noticia1["data_noticia"] = re.search(regex_data_noticia, texto).group(1)
    
    regex_coordenador = re.compile('Dr. ([A-zÀ-ú ]+)', re.DOTALL)
    dict_noticia1["coordenador_nadic"] = re.search(regex_coordenador, texto).group(1)
    
    regex_numero_edital = re.compile('Edital Nº ([0-9\/-]+[A-zÀ-ú\/]+)', re.DOTALL)
    dict_noticia1["numero_edital"] = re.search(regex_numero_edital, texto).group(1)
    
    regex_vigencia = re.compile('vigência de ([1-9]+[A-zÀ-ú ]+)', re.DOTALL)
    dict_noticia1["vigencia_do_processo"] = re.search(regex_vigencia, texto).group(1)
    
    return dict_noticia1

def regex_txt2():
    with open('noticia2.txt', 'r') as f:  
        texto = f.read()
        
    dict_noticia2 = {}
    
    regex_titulo_noticia =  re.compile('NADIC\n([A-zÀ-ú ]+)', re.DOTALL)
    dict_noticia2["titulo_noticia"] = re.search(regex_titulo_noticia, texto).group(1)
    
    regex_data_noticia = re.compile('\n([0-9\/]+)', re.DOTALL)
    dict_noticia2["data_noticia"] = re.search(regex_data_noticia, texto).group(1)
    
    regex_evento = re.compile('ê:([A-zÀ-ú: ]+)', re.DOTALL)
    dict_noticia2["evento"] = re.search(regex_evento, texto).group(1)
    
    regex_data_evento = re.compile('Data: ([0-9\/ ]+)', re.DOTALL)
    dict_noticia2["data_evento"] = re.search(regex_data_evento, texto).group(1)
    
    regex_horario_evento = re.compile('Horário: ([0-9\/ ]+[a-z])', re.DOTALL)
    dict_noticia2["horario_evento"] = re.search(regex_horario_evento, texto).group(1)
    
    regex_transmissao = re.compile('transmissão ([A-zÀ-ú, ]+)', re.DOTALL)
    dict_noticia2["transmissao"] = re.search(regex_transmissao, texto).group(1)
    
    regex_site_nadic = re.compile('NADIC:\n([A-zÀ-ú, :\/.]+)', re.DOTALL)
    dict_noticia2["site_nadic"] = re.search(regex_site_nadic, texto).group(1)
    
    return dict_noticia2 

def regex_txt3():
    with open('noticia3.txt', 'r') as f:  
        texto = f.read()
        
    dict_noticia3 = {}
    
    regex_titulo_noticia =  re.compile('NADIC\n([A-zÀ-ú ]+)', re.DOTALL)
    dict_noticia3["titulo_noticia"] = re.search(regex_titulo_noticia, texto).group(1)
    
    regex_data_noticia = re.compile('\n([0-9\/]+)', re.DOTALL)
    dict_noticia3["data_noticia"] = re.search(regex_data_noticia, texto).group(1)
    
    regex_periodo_inscricao = re.compile('de ([0-9\/ ]+[A-zÀ-ú ]+[0-9\/ ]+)', re.DOTALL)
    dict_noticia3["periodo_inscricao"] = re.search(regex_periodo_inscricao, texto).group(1)
    
    regex_valor_dev_nivel1 = re.compile('Nível I \([A-zÀ-ú ]+ R\$ ([0-9,.]+)\)', re.DOTALL)
    dict_noticia3["valor_bolsa_dev_nivel1"] = re.search(regex_valor_dev_nivel1, texto).group(1)
    
    regex_valor_dev_nivel2 = re.compile('Nível II \([A-zÀ-ú ]+ R\$ ([0-9,.]+)\)', re.DOTALL)
    dict_noticia3["valor_bolsa_dev_nivel2"] = re.search(regex_valor_dev_nivel2, texto).group(1)
    
    regex_resultado_final = re.compile('dia ([0-9\/]+)', re.DOTALL)
    dict_noticia3["resultado_final"] = re.search(regex_resultado_final, texto).group(1)
    
    regex_numero_edital = re.compile('Edital Nº ([0-9\/-]+[A-zÀ-ú\/]+)', re.DOTALL)
    dict_noticia3["numero_edital"] = re.search(regex_numero_edital, texto).group(1)
    
    
    return dict_noticia3

def convert_to_json(dicionario,nome_arquivo):
        with open(nome_arquivo, "w") as data:
            json.dump(dicionario, data)

        
navegador = webdriver.Chrome()
ws = WebScraping(navegador)
ws.navigate()
dict_noticias = ws.noticias_nadic()
navegador.quit()

dict_noticia1 = regex_txt1()
convert_to_json(dict_noticia1,"noticia1.json")

dict_noticia2 = regex_txt2()
convert_to_json(dict_noticia2,"noticia2.json")

dict_noticia3 = regex_txt3()
convert_to_json(dict_noticia3,"noticia3.json")


