#Алексей Шалдин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import config
import requests
import data

def post_new_order(): #Функция делает запрос на создание нового заказа
    return requests.post(config.URL_SERVICE + config.CREATE_ORDERS,
                         json=data.order_body,)

#Функция превращает в строку полученный номер заказа, подставляет в путь запроса на получение заказа
#и делает запрос с новым номером заказа
def get_order_track():
    response = post_new_order()
    track_number = str(response.json()['track'])
    return requests.get(config.URL_SERVICE + config.GET_TRACK + track_number,)

