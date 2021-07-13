from raspadorBetway import *
from flask import Flask, jsonify, request

def startRasparTodosJogos(esporte):
    driver = raspador.iniciaNavegador()
    while True:
        dataRasparTodosJogos = raspador.raspadorPaises(driver,esporte)
        with open('json/TodosOsJogos'+str(esporte)+'.json','w',encoding='utf-8') as f:
            json.dump(dataRasparTodosJogos, f, ensure_ascii=False, indent=4)
    return dataRasparTodosJogos

def rasparTodosJogos(esporte):
    with open('json/TodosOsJogos'+str(esporte)+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(data)
    return data 

def rasparLigas(esporte,liga):
    driver = raspador.iniciaNavegador()
    dataLiga = raspador.raspadorLigasPaises(driver,esporte,liga)
    raspador.fechaNavegador(driver)
    return dataLiga

def lerTodasOddsPorLiga(esporte,liga):
    driver = raspador.iniciaNavegador()
    dataLiga = raspador.raspadorLigasPaises(driver,esporte,liga)
    oddsLiga = []
    for x in dataLiga[liga]:
        _id = x.get("id")
        dataOdds = raspador.capturaOddLink(driver,_id)
        oddsLiga.append({x.get('Equipes'):dataOdds})
    dataExport = {liga:oddsLiga}
    raspador.fechaNavegador(driver)
    return dataExport

def startlerAovivo():
    driver = raspador.iniciaNavegador()
    while True:
        jogosAovivo = raspador.aoVivo(driver)
        with open('json/jogosAovivo.json', 'w', encoding='utf-8') as f:
            json.dump(jogosAovivo, f, ensure_ascii=False, indent=4)
    return jogosAovivo

def lerAovivo():
    with open('json/jogosAovivo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

def capturaEsportes():
    driver = raspador.iniciaNavegador()
    esportes = raspador.capturaEsportesPaginaInicial(driver)
    with open('json/capturaEsportes.json', 'w', encoding='utf-8') as f:
        json.dump(esportes, f, ensure_ascii=False, indent=4)
    raspador.fechaNavegador(driver)
    return esportes
