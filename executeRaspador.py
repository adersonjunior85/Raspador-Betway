from raspadorBetway import *

def rasparTodosJogos(esporte):
    driver = raspador.iniciaNavegador()
    dataRasparTodosJogos = raspador.raspadorPaises(driver,esporte)
    raspador.fechaNavegador(driver)
    return dataRasparTodosJogos

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

def lerAovivo():
    driver = raspador.iniciaNavegador()
    jogosAovivo = raspador.aoVivo(driver)
    raspador.fechaNavegador(driver)
    return jogosAovivo

def capturaEsportes():
    driver = raspador.iniciaNavegador()
    esportes = raspador.capturaEsportesPaginaInicial(driver)
    raspador.fechaNavegador(driver)
    return esportes
