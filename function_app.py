import azure.functions as func
import logging
from function_subtract import bp as subtract
from function_add import bp as add
from function_multiply import bp as multiply

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_functions(subtract)
app.register_functions(add)
app.register_functions(multiply)