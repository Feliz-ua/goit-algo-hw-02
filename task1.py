#Імпортуємо необхідні модулі: Queue для створення черги (FIFO), time для створення затримок та random для генерації унікальних номерів заявок.
from queue import Queue
import time
import random

# Створюємо порожню чергу заявок
queue = Queue()

# Генеруємо заявки з унікальним номером
def generate_request():
    # генеруємо випадковий номер заявки 
    request_id = random.randint(1000, 9999)
    print(f"Нова заявка #{request_id} додана в чергу")
    # Додаємо заявку у кінець черги
    queue.put(request_id)

# Обробляємо заявки
def process_request():
    # Перевіряємо чи черга не порожня
    if not queue.empty():
        # Видаляємо заявку з початку черги
        request_id = queue.get()
        print(f"Заявка #{request_id} оброблена")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Робимо цикл програми. Користувач вводить команду: Enter — додати заявку, 'p' — обробити, 'exit' — завершити
while True:
    user_input = input("Натисніть Enter для нової заявки, 'p' для обробки заявки або 'exit' для завершення: ")
    if user_input == "":
        generate_request()
    elif user_input.lower() == "p":
        process_request()
    elif user_input.lower() == "exit":
        break
    # Затримка півсекунди між ітераціями циклу для імітації реального очікування/обробки заявок
    time.sleep(0.5)
print("Програма завершена.")
    

