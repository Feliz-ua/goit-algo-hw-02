# імпортуємо deque з collections для реалізації двонаправленої черги
from collections import deque

# Створюємо функцію для перевірки, чи є рядок паліндромом
def is_palindrome(s):
    # Попередня обробка: видалити пробіли, привести до нижнього регістру й залишити лише алфавітно-цифрові символи
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Створюємо двонаправлену чергу з очищеного рядка
    d = deque(cleaned)
    # Порівнюємо символи з початку і кінця черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            # Якщо символи не співпали, функція повертає False (рядок не є паліндромом)
            return False
    # Якщо всі символи співпали (цикл завершився), рядок паліндром — повертається True
    return True


print(is_palindrome("Сир і рис")) 
print(is_palindrome("Ротатор"))
print(is_palindrome("Hello"))
print(is_palindrome("A man a plan a canal Panama"))