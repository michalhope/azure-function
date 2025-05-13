import azure.functions as func
import logging
from case_timeout import handle_timeout_case
from case_auth import handle_auth_case

app = func.FunctionApp()

@app.route(route="MyFunction", auth_level=func.AuthLevel.FUNCTION)
async def MyFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("🚀 Function started.")

    case = req.params.get("case", "").lower()

    if case == "timeout":
        return await handle_timeout_case()
    
    elif case == "auth":
        return handle_auth_case(req)
    
    else:
        logging.info("ℹ️ No valid 'case' parameter provided. Returning default response.")
        return func.HttpResponse(
        "👋 Hello! Please specify a case (?case=timeout or ?case=auth).",
        status_code=200
    )
