def check (expr):
    stack = []
    # Відображення пар дужок
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()
    # Симетрично, якщо стек порожній
    return "Симетрично" if not stack else "Несиметрично"

# Приклади використання:
print(check ("( ){[ 1 ]( 1 + 3 )( ){ }}"))    
print(check ("( 23 ( 2 - 3);)"))            
print(check ("({ 11 }")) 