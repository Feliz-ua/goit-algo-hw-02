from queue import Queue
import time
import random

# Створити чергу заявок
queue = Queue()

# Генерація нової заявки з унікальним номером
def generate_request():
    request_id = random.randint(1000, 9999)
    print(f"Нова заявка #{request_id} додана в чергу")
    queue.put(request_id)

# Обробка заявки
def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Заявка #{request_id} оброблена")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
while True:
    user_input = input("Натисніть Enter для нової заявки, 'p' для обробки заявки або 'exit' для завершення: ")
    if user_input == "":
        generate_request()
    elif user_input.lower() == "p":
        process_request()
    elif user_input.lower() == "exit":
        break
    time.sleep(0.5)

