import os
import json
import time
import requests
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

class raspador():
    def iniciaNavegador():
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    def fechaNavegador(driver):
        driver.quit()

    def aceitaCoockie(driver):
        try:                                                                            #tentativa de fechar o coockie
            driver.find_element_by_class_name("cookiePolicyAcceptButton").click()       #comando para clicar em OK
            print("Coockie aceitado")                                                   #caso dê certo retorna essa mensagem
        except:                                                                         #caso dê errado abre uma exceção
            print("Coockie não identificado")

    def raspadorPaises(driver,esporte):
        dicionarioGlobal = []
        driver.get("https://betway.com/pt/sports/ctg/"+esporte)
        time.sleep(5)
        raspador.aceitaCoockie(driver)
        ligasTabela = driver.find_elements_by_class_name("collapsablePanel")
        buttons = driver.find_elements_by_class_name("showAllButton")                   #
        linhas = 10
        clica = 0
        try:
            while clica != linhas:            
                driver.find_elements_by_class_name("showAllButton")[clica].click() 
                time.sleep(4)
                print("c")
                raspador.expandirLigas(driver)
                print("b")
                dicionarioGlobal.append(raspador.ligasParser(driver))
                print("a")
                driver.get("https://betway.com/pt/sports/ctg/"+esporte)
                time.sleep(4)
                linhas = len(driver.find_elements_by_class_name("showAllButton"))
                clica += 1
        except:
            print("Erro raspadorPaises")  
        return dicionarioGlobal

    def raspadorLigasPaises(driver,esporte,liga):
        dicionarioLigas = []
        driver.get("https://betway.com/pt/sports/ctg/"+esporte)
        time.sleep(5)
        raspador.aceitaCoockie(driver)
        raspador.expandirPaisesClica(driver,liga)
        ligasNomes = driver.find_elements_by_class_name("listItemContent")
        ligaData = raspador.ligaUnicaParser(driver)
        return ligaData

    def ligaUnicaParser(driver):
        global dicionarioGlobal
        print("Iniciando leitura de liga")
        addDicionarioGlobal = []
        dictLigas = []
        dictJogos = []
        print("Iniciando leitura")
        painelCentral = driver.find_element_by_class_name("mainPanel")
        ligaNome = driver.find_element_by_class_name("title").text
        tabelas = painelCentral.find_elements_by_class_name("collapsablePanel")
        print("Iniciando captura de dados na página")
        for tabelaData in tabelas:
            linhas = tabelaData.find_elements_by_class_name("oneLineEventItem")
            for linha in linhas:
                idJogo = linha.find_element_by_class_name("scoreboardInfoNames").get_attribute('href')
                dia = tabelaData.find_element_by_class_name("titleText").text
                hora = linha.find_element_by_class_name("scoreAndTime").text
                equipe = linha.find_element_by_class_name("scoreboardInfoNames").text
                odd1 = linha.find_elements_by_class_name("odds")
                odd = []
                for z in odd1:
                    odd.append(z.text)
                dictJogos.append({'Equipes': equipe,'id':idJogo , 'Dia': dia, 'Hora': hora, 'Odds': odd})
        dictLigas = {ligaNome:dictJogos}
        return dictLigas
        
    def ligasParser(driver):
        global dicionarioGlobal
        print("Iniciando leitura de ligas")
        addDicionarioGlobal = []
        dictLigas = []
        dictJogos = []
        print("Iniciando leitura")
        painelCentral = driver.find_element_by_class_name("mainPanel")
        paisNome = driver.find_element_by_class_name("title").text
        tabelas = painelCentral.find_elements_by_class_name("alternativeHeaderBackground")
        print("Iniciando captura de dados na página")
        for tabela in tabelas:
            liga = tabela.find_element_by_class_name("collapsableHeader")
            datasOdds = tabela.find_elements_by_class_name("collapsablePanel")
            ligaNome = liga.text.split("\n")[0]
            for tabelaData in datasOdds:
                linhas = tabelaData.find_elements_by_class_name("oneLineEventItem")
                for linha in linhas:
                    idJogo = linha.find_element_by_class_name("scoreboardInfoNames").get_attribute('href')
                    dia = tabelaData.find_element_by_class_name("titleText").text
                    hora = linha.find_element_by_class_name("scoreAndTime").text
                    equipe = linha.find_element_by_class_name("scoreboardInfoNames").text
                    odd1 = linha.find_elements_by_class_name("odds")
                    odd = []
                    for z in odd1:
                        odd.append(z.text)
                    dictJogos.append({'Equipes': equipe,'id':idJogo , 'Dia': dia, 'Hora': hora, 'Odds': odd})
            dictLigas.append({ligaNome:dictJogos})
        date = {paisNome:dictLigas}
        print(date)
        return date

    def expandirLigas(driver):
        try:
            painelCentral = driver.find_element_by_class_name("mainPanel")#captura o painel central com todas as tabelas com dados
            tabelas = painelCentral.find_elements_by_class_name("alternativeHeaderBackground")#captura as tabelas dentro do painel central
            if len(tabelas) < 1:
                tabelas = painelCentral.find_elements_by_class_name("subCategoryListWrapperContent")
            for x in tabelas:#inicia um laço dentro das tabelas
                print("Abertura de abas de ligas ocultas iniciado...")
                try:
                    x.find_element_by_class_name("eventTableItemCollection")#procura uma tabela que deveria estar aparecendo 
                    liga = x.find_element_by_class_name("collapsableHeader")#captura a liga
                except Exception as err:#caso de errado a tentiva acima incia o tratamento da exceção
                    print("Aba oculta detectada, abrindo...")
                    x.find_element_by_class_name("collapsableHeader").click()#clica na aba oculta
                    time.sleep(0.3)#espera 1 segundo para continuar
                    liga = x.find_element_by_class_name("collapsableHeader")#captura a liga que antes estava oculta
                datasOdds = x.find_elements_by_class_name("collapsablePanel")#captura a tabela com dados dentro da tabela para procurar mais tabelas ocultas
                for x in datasOdds:#inicia um laço para pesquisar mais abas ocultas
                    print("Abertura de abas de dias ocultas iniciado...")
                    try:
                        x.find_element_by_class_name("collapsableContent.empty")
                        x.find_element_by_class_name("collapsableHeader").click()
                        time.sleep(1)
                        print("Aba oculta detectada, abrindo...")
                    except:
                        pass 
        except:
            pass
                
    def expandirPaisesClica(driver,liga):
        linhas = driver.find_elements_by_class_name("collapsablePanel")
        try:
            for linha in linhas:
                try:
                    linha.find_element_by_class_name("collapsableContent.empty")
                    linha.find_element_by_class_name("collapsableHeader").click()
                    ligasPorPais = linha.find_elements_by_class_name("description")
                    for x in ligasPorPais:
                        if x.text == liga:
                            x.click()
                            time.sleep(4)
                except:
                    ligasPorPais = linha.find_elements_by_class_name("description")
                    for x in ligasPorPais:
                        if x.text == liga:
                            x.click()
                            time.sleep(4)
        except:
            pass

    def capturaOddLink(driver,href):
        driver.get(href)
        time.sleep(6)
        raspador.aceitaCoockie(driver)
        mainPanel = driver.find_element_by_class_name("mainPanel")
        tituloMainPanel = mainPanel.find_element_by_class_name("title").text
        tabela = mainPanel.find_elements_by_class_name("collapsablePanel")
        dicionario  = {}
        for x in tabela:
            title = x.find_element_by_class_name("title").text
            nome  = x.find_elements_by_class_name("outcomeHeader")
            odd   = x.find_elements_by_class_name("odds")
            if len(nome) < 1:
                nome  = x.find_elements_by_class_name("outcomeItemHeader")
            a = []
            b = []
            c = {}
            for x in nome:
                a.append(x.text)
            for y in odd:
                b.append(y.text)
            for z in range(len(a)):
                add1 = {a[z]:b[z]}
                c.update(add1)
            add = {title: c}
            dicionario.update(add)
        return dicionario

    def pegaHrefAoVivo(driver):
        driver.get("https://betway.com/pt/sports/lve")
        time.sleep(5)
        mainPanel = driver.find_element_by_class_name("layout.inPlayLayout.collection.vertical")
        tabelaJogos = driver.find_element_by_class_name("overflowHidden.scrollableArea.horizontalButtons.horizontal")
        jogos = tabelaJogos.find_elements_by_class_name("contentSelectorItem")
        html = []
        for pegaLink in jogos:
            html.append(pegaLink.get_attribute("href"))
        return html

    def expandirLive(jogo):
        try:
            jogo.find_element_by_class_name("collapsableContent.empty")
            jogo.find_element_by_class_name("collapsableHeader").click()
        except:
            pass

    def aoVivo(driver):
        dicionario = []
        dicionarioCampeonato = []
        dicionarioEsporte = []
        esporte = []
        partida = []
        htmls = raspador.pegaHrefAoVivo(driver)
        for abreGuia in htmls: 
            driver.get(abreGuia)
            time.sleep(5)
            raspador.aceitaCoockie(driver)
            mainPanel = driver.find_element_by_class_name("mainContent")
            jogos = mainPanel.find_elements_by_class_name("collapsablePanel")
            dicionarioCampeonato = []
            for jogo in jogos:
                raspador.expandirLive(jogo)
                nomeCampeonato = jogo.find_element_by_class_name("titleText").text
                linhaDados = jogo.find_elements_by_class_name("eventHolder")
                dicionario = []
                for linha in linhaDados:
                    linhaOdd = linha.find_element_by_class_name("eventMarket")
                    score = linha.find_element_by_class_name("oneLineScoreboard")
                    placar = score.find_element_by_class_name("scoreAndTime").text
                    times = score.find_element_by_class_name("scoreboardInfoNamesWrapper").text
                    tempo = score.find_element_by_class_name("infoTextContainer.infoText").text
                    _id = score.find_element_by_class_name("scoreboardInfoNames").get_attribute("href")
                    odds = linhaOdd.find_elements_by_class_name("baseOutcomeItem")
                    oddsLista = []
                    for odd in odds:
                        oddsLista.append(odd.text)
                    add = {"placar":placar,"tempo":tempo,"odds":oddsLista, "id": _id}
                    dicionario.append({times:add})
                dicionarioCampeonato.append({nomeCampeonato:dicionario})
            dicionarioEsporte.append({abreGuia.split("/")[-1]:dicionarioCampeonato})
        return dicionarioEsporte

    def capturaEsportesPaginaInicial(driver):
        esportes = []
        driver.get("https://betway.com/pt/sports")
        time.sleep(6)
        classeEsportes = driver.find_element_by_class_name("categoryListLayout.stacked")
        listaEsportes = classeEsportes.find_elements_by_class_name("categoryListItem")
        for esporte in listaEsportes:
            esportes.append(esporte.text)
        return esportes