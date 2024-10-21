import logging

import azure.functions as func

bp = func.Blueprint()

@bp.route(route="http_add")
def add(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing addition request.')
    
    try:
        num1 = int(req.params.get('num1'))
        num2 = int(req.params.get('num2'))
        result = num1 + num2
        return func.HttpResponse(f"Result of addition: {result}", status_code=200)
    except (TypeError, ValueError):
        return func.HttpResponse(
            "Please pass valid 'num1' and 'num2' query parameters.",
            status_code=400
        )