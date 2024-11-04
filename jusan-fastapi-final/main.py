from fastapi import FastAPI, HTTPException, status, Header, Request
from pydantic import BaseModel
from typing import List
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response

app = FastAPI()

# Глобальный массив для хранения элементов
elements = []

# Модель для обработки входных данных для /list и /calculator
class ElementRequest(BaseModel):
    element: str

class CalculatorRequest(BaseModel):
    expr: str

# Метрики Prometheus
http_requests_total = Counter(
    'http_requests_total', 'Number of HTTP requests received', ['method', 'endpoint']
)
http_requests_duration = Histogram(
    'http_requests_milliseconds', 'Duration of HTTP requests in milliseconds', ['method', 'endpoint']
)
last_sum1n = Gauge('last_sum1n', 'Value stores last result of sum1n')
last_fibo = Gauge('last_fibo', 'Value stores last result of fibo')
list_size = Gauge('list_size', 'Value stores current list size')
last_calculator = Gauge('last_calculator', 'Value stores last result of calculator')
errors_calculator_total = Counter('errors_calculator_total', 'Number of errors in calculator')

# Маршрут для метрик
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Middleware для отслеживания времени и подсчета запросов
@app.middleware("http")
async def track_metrics(request: Request, call_next):
    method = request.method
    endpoint = request.url.path
    http_requests_total.labels(method=method, endpoint=endpoint).inc()
    start_time = time.time()

    response = await call_next(request)

    duration = (time.time() - start_time) * 1000  # в миллисекундах
    http_requests_duration.labels(method=method, endpoint=endpoint).observe(duration)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{n}")
def sum_to_n(n: int):
    result = sum(range(1, n + 1))
    last_sum1n.set(result)
    return {"result": result}

@app.get("/fibo")
def fibonacci(n: int):
    if n <= 0:
        return {"error": "n must be a positive integer"}
    
    # Вычисляем n-ое число Фибоначчи
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    last_fibo.set(a)
    return {"result": a}

@app.post("/reverse")
def reverse_string(string: str = Header(...)):
    reversed_string = string[::-1]
    return {"result": reversed_string}

@app.get("/list")
def get_list():
    list_size.set(len(elements))
    return {"result": elements}

@app.put("/list")
def add_to_list(item: ElementRequest):
    elements.append(item.element)
    list_size.set(len(elements))
    return {"result": elements}

@app.post("/calculator")
def calculator(request: CalculatorRequest):
    expr = request.expr.split(',')
    
    # Проверка корректности формата выражения
    if len(expr) != 3:
        errors_calculator_total.inc()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")
    
    try:
        num1 = float(expr[0])
        operator = expr[1]
        num2 = float(expr[2])
    except ValueError:
        errors_calculator_total.inc()
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
            errors_calculator_total.inc()
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="zerodiv")
        result = num1 / num2
    else:
        errors_calculator_total.inc()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")

    last_calculator.set(result)
    return {"result": result}

