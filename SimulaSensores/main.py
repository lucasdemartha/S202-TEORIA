"""
    Nome: Lucas Ribeiro de Martha
    Mat: 198 GES
"""

import threading    # Lib Threads
import time         # Controle de tempo dos Threads
import random       # Num Random
from pymongo import MongoClient # Conexao


# conexao mongodb
client = MongoClient('mongodb://localhost:27017')

# database
db = client['bancoiot']

# collection
sensores = db.sensores

#Threads

def simulaTemp(num, sensor, intervalo):
    temp = random.randint(30, 40)
    
    documento = {
        "nomeSensor": sensor,
        "valorSensor": temp,
        "unidadeMedida": "C",
        "sensorAlarmado": False
    }
    
    insercao = sensores.insert_one(documento)
    if insercao.acknowledged:
        print('Sensor', num, 'criado')
    else:
        print('Erro ao criar sensor', num)
    while temp <= 38:
        temp = random.randint(30, 40)
        atualiza_temp = sensores.update_one(
            {"nomeSensor": sensor},
            {"$set": {"valorSensor": temp}}
        )
        if atualiza_temp.acknowledged:
            print('Temperatura', num, 'atualizada')
        else:
            print('Erro ao atualizar temperatura', num)
        time.sleep(intervalo)
    atualiza_alarm = sensores.update_one(
        {"nomeSensor": sensor},
        {"$set": {"sensorAlarmado": True}}
    )
    if atualiza_alarm.acknowledged:
        print('Alarme', num, 'atualizado p/ TRUE')
    else:
        print('Erro ao atualizar alarme', num)
    print('Atenção! Temperatura muito alta! Verificar Sensor', num, '!')

#Limpando cachê

deleta = sensores.delete_many(
    {"nomeSensor": {"$exists": True}}
)

#Threads

tempo = 3

a = threading.Thread(target=simulaTemp, args=(1, 'Temp1', tempo))
a.start()
b = threading.Thread(target=simulaTemp, args=(2, 'Temp2', tempo))
b.start()
c = threading.Thread(target=simulaTemp, args=(3, 'Temp3', tempo))
c.start()