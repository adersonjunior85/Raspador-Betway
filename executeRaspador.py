from raspadorBetway import *

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

    
#rasparLigas("tennis","Nottingham")
#lerTodasOddsPorLiga("tennis","Nottingham")
#data = rasparTodosJogos("soccer")
#lerAovivo()
#capturaEsportes()