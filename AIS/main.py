from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import sqlite3
import os
import plotly.graph_objs as go
from dash import Dash, html, dcc
import dash
import numpy as np
import config
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
DB_PATH = config.DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inadimplencia(
                mes TEXT PRIMARY KEY,
                inadimplencia REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS selic(
                mes TEXT PRIMARY KEY,
                selic_diaria REAL
            )
        ''')

vazio = 0

@app.route('/')
def index():
    return render_template_string('''
        <h1> Upload de dados Economicos </h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            
            <label for="campo_inadimplencia"> Arquivo de Inadimplencia: (CSV)</label>
            <input name="campo_inadimplencia" type="file" required>
                                  <br><br>  
             
            <label for="campo_selic"> Arquivo de Taxa SELIC: (CSV)</label>
            <input name="campo_selic" type="file" required>
                                  
                                  <br><br>  

            <input type="submit" value="Fazer Upload">
        </form>
        <br><br> 
        <hr>
            <br><a href="/consultar"> Consultar dados Armazenados </a>
            <br><a href="/graficos"> Visualizar Graficos </a>
            <br><a href="/editar_inadimplencia"> Editar dados de Inadimplencia </a>
            <br><a href="/correlacao"> Analisar Correlação </a>
    ''')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)



