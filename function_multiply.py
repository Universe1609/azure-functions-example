import logging

import azure.functions as func

multiply = func.Blueprint()

@multiply.route(route="http_multiply")
def main(req: func.HttpRequest) -> func.HttpResponse:
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