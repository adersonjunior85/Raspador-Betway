## Raspador-Betway
 Web Scrapping usando python e selenium


Raspador-Betway é um raspador que utiliza selenium e python para capturar diversos dados do site da betway.

## Uso

Basta iniciar o flask_init.py, usando comando no cmd:
python flask_init.py
E fazer a request das seguintes formas:
http://127.0.0.1:5000/api/capturaEsportes
http://127.0.0.1:5000/api/lerTodasOddsPorLiga/<ESPORTE>/<NOMEDALIGA>
http://127.0.0.1:5000/api/rasparTodosJogos/<ESPORTE>
http://127.0.0.1:5000/api/leraovivo
http://127.0.0.1:5000/api/rasparLigas/<ESPORTE>/<NOMEDALIGA>


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
