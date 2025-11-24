from collections import deque

def is_palindrome(s):
    # Попередня обробка: видалити пробіли, привести до нижнього регістру й залишити лише алфавітно-цифрові символи
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    d = deque(cleaned)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклад використання:
print(is_palindrome("Сир і рис")) 
print(is_palindrome("Ротатор"))  
