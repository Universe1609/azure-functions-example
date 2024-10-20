import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="http_add")
@app.route(route="http_add")
def add(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing addition request.')
    
    try:
        num1 = int(req.params.get('num1'))
        num2 = int(req.params.get('num2'))
        result = num1 + num2
        return func.HttpResponse(f"Result of addition: {result}")
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Please pass valid 'num1' and 'num2' query parameters.",
            status_code=400
        )
        
@app.function_name(name="http_subtract")
@app.route(route="http_subtract")
def subtract(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing subtraction request.')
    
    try:
        num1 = int(req.params.get('num1'))
        num2 = int(req.params.get('num2'))
        result = num1 - num2
        return func.HttpResponse(f"Result of subtraction: {result}", status_code=200)
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Please pass valid 'num1' and 'num2' query parameters.",
            status_code=400
        )
        
@app.function_name(name="http_multiply")
@app.route(route="http_multiply")
def multiply(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing multiplication request.')
    
    try:
        num1 = int(req.params.get('num1'))
        num2 = int(req.params.get('num2'))
        result = num1 * num2
        return func.HttpResponse(f"Result of multiplication: {result}", status_code=200)
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Please pass valid 'num1' and 'num2' query parameters.",
            status_code=400
        )

@app.function_name(name="http_divide")
@app.route(route="http_divide")
def divide(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing division request.')
    
    try:
        num1 = int(req.params.get('num1'))
        num2 = int(req.params.get('num2'))
        result = num1 / num2
        return func.HttpResponse(f"Result of division: {result}", status_code=200)
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Please pass valid 'num1' and 'num2' query parameters.",
            status_code=400
        )
    except ZeroDivisionError:
        return func.HttpResponse(
            "Cannot divide by zero.",
            status_code=400
        )
        