from flask import Flask, render_template, request
from funcoes import number
import json

app = Flask(__name__)


# def ola_mundo():
#     lista_de_numeros = []

#     for i in range(1,15):
 
#         numero = number(i)
        
#         lista_de_numeros.append(numero)
#     return render_template('lista.html', titulo='Fibonacci e Fatorial', lista_num = lista_de_numeros)

@app.route('/inicio', methods = ['POST', 'GET'])
def formulario():
    return render_template('formulario.html', titulo = 'Fibonacci e Fatorial')

@app.route('/resultado', methods = ['POST',])
def resultado():
    n = int(request.form['numero'])
    num = number(n)

    
    return render_template('resultado.html', titulo='Fibonacci e Fatorial', numero=num)


app.run()