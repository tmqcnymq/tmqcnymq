# Este es un script de Python para mi currículum de GitHub
# Muestra el número de Fibonacci correspondiente a mi edad

# Definir una función para calcular el número de Fibonacci
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Asignar mi edad a una variable
edad = 25

# Llamar a la función con mi edad como argumento
fib = fibonacci(edad)

# Imprimir el resultado
print(f"El número de Fibonacci correspondiente a mi edad ({edad}) es {fib}")
