import schedule
import time
from datetime import datetime
import requests
import json
import pandas as pd
import os


while True:
    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
    json_data = json.loads(data.content)
    candidato = []
    apuracao = 0
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:
        #Seleciona os canditados desejados \/
        if informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4' or informacoes['seq'] == '1':
            apuracao = json_data['pst']
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])
    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'n° votos', 'porcentagem'])
    print(f'Porcentagem das Urnas Apuradas: {apuracao}%')
    print(df_eleicao)
    candidato.clear()
    votos.clear()
    porcentagem.clear()
    print('-'*30)
    os.system('cls')
    time.sleep(15)
