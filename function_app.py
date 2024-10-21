import azure.functions as func
import logging
from function_subtract import bp
from function_add import add
from function_multiply import multiply

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_functions(bp)
app.register_functions(add)
app.register_functions(multiply)