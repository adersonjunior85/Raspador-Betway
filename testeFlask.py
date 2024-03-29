from raspadorBetway import *
from executeRaspador import *
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os


app = Flask(__name__)

@app.route('/api/rasparTodosJogos/<string:esporte>', methods=['GET'])
def callFunction_rasparTodosJogos(esporte):
	data = rasparTodosJogos(esporte)
	return jsonify(data)

@app.route('/api/rasparLigas/<string:esporte>/<string:liga>', methods=['GET'])
def callFunction_(esporte, liga):
	data = rasparLigas(esporte,liga)
	return jsonify(data)

@app.route('/api/lerTodasOddsPorLiga/<string:esporte>/<string:liga>', methods=['GET'])
def callFunction_lerTodasOddsPorLiga(esporte, liga):
	data = lerTodasOddsPorLiga(esporte,liga)
	return jsonify(data)

@app.route('/api/capturaEsportes', methods=['GET'])
def callFunction_capturaEsportes():
	data = capturaEsportes()
	return jsonify(data)

@app.route('/api/leraovivo', methods=['GET'])
def callFunction_lerAovivo():
	data = lerAovivo()
	return jsonify(data)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)