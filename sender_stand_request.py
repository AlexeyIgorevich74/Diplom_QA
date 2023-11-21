#Алексей Шалдин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import config
import requests
import data

def post_new_order(body): #Функция создает новый заказ и возвращает трек-номер
    return requests.post(config.URL_SERVICE + config.CREATE_ORDERS,
                         json=body)



def get_order_track(track_number): #Функция отправляет запрос на получение заказа по трек-номеру
    return requests.get(config.URL_SERVICE + config.GET_TRACK,
                        params=track_number)

