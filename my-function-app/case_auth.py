import logging
import azure.functions as func

def handle_auth_case(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("🔐 Simulating auth error case.")
        api_key = req.headers.get("x-api-key")
        expected_key = "secret123"

        if api_key != expected_key:
            logging.warning("🔐 Unauthorized – invalid API key.")
            return func.HttpResponse(
                "🔐 Unauthorized – Invalid API key.",
                status_code=401
            )
        
        return func.HttpResponse("✅ Authorized – access granted.")

    except Exception as e:
        logging.error(f"❌ Unexpected error in auth case: {e}")
        logging.exception(e)
        return func.HttpResponse("❌ Internal server error.", status_code=500)
