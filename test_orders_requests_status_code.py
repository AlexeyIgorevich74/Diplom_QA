#Алексей Шалдин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

#Функция для проверки, что при получении заказа по номеру статус ответа 200
def test_request_status_code_new_order():
    order_response = sender_stand_request.get_order_track()

    assert order_response.status_code == 200