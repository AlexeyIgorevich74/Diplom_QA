#Алексей Шалдин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import config
import requests

def post_new_order(body): #Функция создает новый заказ и возвращает трек-номер
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDERS,
                         json=body)
    return response.json()['track']



def get_order_track(track_number): #Функция отправляет запрос на получение заказа по трек-номеру
    return requests.get(config.URL_SERVICE + config.GET_TRACK,
                        params=track_number)
