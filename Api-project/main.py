from fastapi import FastAPI, HTTPException, status, Header
from pydantic import BaseModel
from typing import List
from fastapi import  Header

app = FastAPI()

# Глобальный массив для хранения элементов
elements = []

# Модель для обработки входных данных для /list и /calculator
class ElementRequest(BaseModel):
    element: str

class CalculatorRequest(BaseModel):
    expr: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{n}")
def sum_to_n(n: int):
    result = sum(range(1, n + 1))
    return {"result": result}

@app.get("/fibo")
def fibonacci(n: int):
    if n <= 0:
        return {"error": "n must be a positive integer"}
    
    # Вычисляем n-ое число Фибоначчи
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return {"result": a}

@app.post("/reverse")
def reverse_string(string: str = Header(...)):
    reversed_string = string[::-1]
    return {"result": reversed_string}

@app.get("/list")
def get_list():
    return {"result": elements}

@app.put("/list")
def add_to_list(item: ElementRequest):
    elements.append(item.element)
    return {"result": elements}

@app.post("/calculator")
def calculator(request: CalculatorRequest):
    expr = request.expr.split(',')
    
    # Проверка корректности формата выражения
    if len(expr) != 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")
    
    try:
        num1 = float(expr[0])
        operator = expr[1]
        num2 = float(expr[2])
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")
    
    # Выполнение арифметической операции
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="zerodiv")
        result = num1 / num2
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")

    return {"result": result}
