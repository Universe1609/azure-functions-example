import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        
@app.route(route="sum_trigger", methods=["POST"])
def sum(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_num1 = req.params.get('num1')
        req_num2 = req.params.get('num2')
        
        if not req_num1 or not req_num2:
            logging.info("No query parameters found")
        
        suma = int(req_num1) + int(req_num2)
        return func.HttpResponse(f"Sum of {req_num1} and {req_num2} is {suma}")
    except ValueError:
        return func.HttpResponse("Invalid input", status_code=400)