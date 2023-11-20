#Алексей Шалдин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

#Позитивная проверка.
#Функция создает заказ, забирает трек-номер и передает его на получение заказа по трек-номеру
#проверяет что код ответа 200
def positive_assert(body):
    track = sender_stand_request.post_new_order(body)
    track_number = {'t': track}
    order_response = sender_stand_request.get_order_track(track_number)

    assert order_response.status_code == 200

#Тест 1. успешное получение заказа по трек-номеру
def test_request_status_code_new_order():
    positive_assert(data.order_body)
