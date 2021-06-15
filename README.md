## Raspador-Betway
 Web Scrapping usando python e selenium


Raspador-Betway é um raspador que utiliza selenium e python para capturar diversos dados do site da betway.

## Uso

```python
>>> 

>>> rasparLigas = rasparLigas("soccer","Brasileirão Série A")
>>> lerTodasOddsPorLiga = lerTodasOddsPorLiga("soccer","Brasileirão Série A")
>>> RasparEsporte = rasparTodosJogos("tennis")
>>> rasparEsportesAoVivo = lerAovivo()
>>> raspartTabelaDeEsportes = capturaEsportes()
```
## Uso com CMD
#Para executar basta abrir a pasta do onde encontra o arquivo digitar o nome do arquivo que é: executeRaspador.py e enviar os argumentos, de acordo com a execução Python.

C:\Users\Administrador\Documents\Raspador-Betway> python executeRaspador.py <NOMEDAFUNÇÃO> <ARGUMENTo1> <ARGUMENTO2>}
C:\Users\Administrador\Documents\Raspador-Betway>python executeRaspador.py rasparLigas soccer Brasileirão.Série.A
C:\Users\Administrador\Documents\Raspador-Betway>python executeRaspador.py rasparLigas soccer Copa

## Bibliotecas
	
beautifulsoup4==4.9.3
requests==2.25.1
selenium==3.141.0
webdriver-manager==3.3.0

## Comandos

pip install beautifulsoup4
pip install requests
pip install selenium
pip install webdriver-manager
