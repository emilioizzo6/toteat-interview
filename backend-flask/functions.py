import os
import datetime
import json
import pandas as pd

# Se define el formato de fecha del json entregado
time_format = '%Y-%m-%d %H:%M:%S'

# Decidí hacer una gran funcion que busca las métricas para recorrer el json una sola vez
# Y así optimizar el tiempo de ejecución
def means():
    '''
    Funcion que busca medias en distintas métricas, además de
    encontrar los distintos meseros, productos y categorías.
    '''
    # Se lee el archivo json entregado
    with open(os.path.join("assets/ventas.json")) as file:
        data = json.load(file)

    # Se cran variables para asignar datos
    total_orders = len(data)
    total_time = datetime.timedelta()
    total_bill = 0
    total_diners = 0
    categories = {}
    products = {}
    waiters = []
    zones = []

    # Se recorren las órdenes del json
    for order in data:
        # Se calcula el tiempo de estadía de las personas en cada orden
        dcd = datetime.datetime.strptime(order['date_closed'], '%Y-%m-%d %H:%M:%S')
        dod = datetime.datetime.strptime(order['date_opened'], '%Y-%m-%d %H:%M:%S')
        diff_time = dcd - dod
        total_time += diff_time
        
        # Se suma el total de cada orden
        total_bill += order['total']

        # Se suma el total de personas de cada mesa
        total_diners += order['diners']

        # Se agrega la zona si es que no está en la lista
        if order['zone'] not in zones: zones.append(order['zone'])

        # Se agrega el mesero si es que no está en la lista
        if order['waiter'] not in waiters:
            waiters.append(order['waiter'])

        # Se recorren los productos pedidos de cada orden
        for product in order['products']:
            if product['category'] not in categories.keys():
                categories[product['category']] = 1
            else:
                categories[product['category']] += 1

            if product['name'] not in products.keys():
                products[product['name']] = 1
            else:
                products[product['name']] += 1


    # Se calculan promedios
    mean_table_time = str(total_time / total_orders).split('.')[0]
    mean_table_bill = total_bill / total_orders
    mean_table_diners = total_diners / total_orders

    # print(products)

    # Se retornan los valores de interés
    return mean_table_time, mean_table_bill, mean_table_diners, categories, products, waiters, zones

def waiter_info(waiter):
    '''
    Función para caclualr métricas de algún mesero elegido
    '''
    with open(os.path.join("assets/ventas.json")) as file:
        data = json.load(file)
    
    total_orders = 0
    total_waiter_billing = 0

    for order in data:
        if order['waiter'] == waiter:
            total_orders += 1
            total_waiter_billing += order['total']

    return total_orders, total_waiter_billing

def zone_info(zone):
    '''
    Función para caclualr métricas de alguna zona elegida
    '''
    with open(os.path.join("assets/ventas.json")) as file:
        data = json.load(file)

    total_bills = 0
    total_time_sitting = datetime.timedelta()
    total_orders = len(data)

    for order in data:
        if order['zone'] == zone:
            total_bills += order['total']

            dcd = datetime.datetime.strptime(order['date_closed'], '%Y-%m-%d %H:%M:%S')
            dod = datetime.datetime.strptime(order['date_opened'], '%Y-%m-%d %H:%M:%S')
            diff_time = dcd - dod
            total_time_sitting += diff_time
    
    mean_bills = round(total_bills / total_orders)
    mean_time = str(total_time_sitting / total_orders).split('.')[0]

    return mean_bills, mean_time

def group_by(period):
    with open(os.path.join("assets/ventas.json")) as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df['date_closed'] = pd.to_datetime(df['date_closed'], format='%Y-%m-%d %H:%M:%S')
    

if __name__ == '__main__':
    print(zone_info('Vip'))