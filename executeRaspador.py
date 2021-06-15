#!/usr/bin/env python
from raspadorBetway import *
import sys

def rasparTodosJogos(esporte):
    driver = raspador.iniciaNavegador()
    dataRasparTodosJogos = raspador.raspadorPaises(driver,esporte)
    raspador.fechaNavegador(driver)
    print(dataRasparTodosJogos)
    return dataRasparTodosJogos

def rasparLigas(esporte,liga):
    driver = raspador.iniciaNavegador()
    dataLiga = raspador.raspadorLigasPaises(driver,esporte,liga)
    raspador.fechaNavegador(driver)
    print(dataLiga)
    return dataLiga

def lerTodasOddsPorLiga(esporte,liga):
    driver = raspador.iniciaNavegador()
    dataLiga = raspador.raspadorLigasPaises(driver,esporte,liga)
    oddsLiga = []
    print("dataLiga")
    for x in dataLiga[liga]:
        _id = x.get("id")
        dataOdds = raspador.capturaOddLink(driver,_id)
        oddsLiga.append({x.get('Equipes'):dataOdds})
    dataExport = {liga:oddsLiga}
    print(dataExport)
    return dataExport

def lerAovivo():
    driver = raspador.iniciaNavegador()
    jogosAovivo = raspador.aoVivo(driver)
    print(jogosAovivo)
    return jogosAovivo

def capturaEsportes():
    driver = raspador.iniciaNavegador()
    esportes = raspador.capturaEsportesPaginaInicial(driver)
    print(esportes)
    return esportes

if sys.argv[1] == "rasparLigas":
    rasparLigas(sys.argv[2],sys.argv[3].replace("."," "))
elif sys.argv[1] == "lerTodasOddsPorLiga":
    lerTodasOddsPorLiga(sys.argv[2],sys.argv[3].replace("."," "))
elif sys.argv[1] == "rasparTodosJogos":
    rasparTodosJogos("soccer")
elif sys.argv[1] == "lerAovivo":
    lerAovivo()
elif sys.argv[1] == "capturaEsportes":
    capturaEsportes()
