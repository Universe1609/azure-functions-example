import azure.functions as func
import logging
from function_subtract import bp

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_functions(bp)