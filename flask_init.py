from raspadorBetway import *
from executeRaspador import *
from flask import Flask, jsonify, request
from flask import send_file
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os


app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def teste():
	return "Correto"
@app.route('/api/startRasparTodosJogos/<string:esporte>', methods=['GET'])
def callFunction_startRasparTodosJogos(esporte):
	data = startRasparTodosJogos(esporte)
	return jsonify(data)		

@app.route('/rasparTodosJogos/<string:esporte>', methods=['GET'])
def callFunction_rasparTodosJogos(esporte):
	data = rasparTodosJogos(esporte)
	return jsonify(data)

@app.route('/rasparLigas/<string:esporte>/<string:liga>', methods=['GET'])
def callFunction_(esporte, liga):
	data = rasparLigas(esporte,liga)
	return jsonify(data)

@app.route('/lerTodasOddsPorLiga/<string:esporte>/<string:liga>', methods=['GET'])
def callFunction_lerTodasOddsPorLiga(esporte, liga):
	data = lerTodasOddsPorLiga(esporte,liga)
	return jsonify(data)

@app.route('/capturaEsportes', methods=['GET'])
def callFunction_capturaEsportes():
	data = capturaEsportes()
	return jsonify(data)

@app.route('/startleraovivo', methods=['GET'])
def callFunction_startlerAovivo():
	data = startlerAovivo()
	return jsonify(data)

@app.route('/leraovivo', methods=['GET'])
def callFunction_lerAovivo():
	data = lerAovivo()
	return data
@app.route('/imagem', methods=['GET'])
def callFunction_imagem():
	print("a")
	return send_file("screenshot.png", mimetype='image/gif')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)