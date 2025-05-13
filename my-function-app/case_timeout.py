import logging
import asyncio
import azure.functions as func

async def handle_timeout_case() -> func.HttpResponse:
    try:
        logging.info("🕒 Simulating timeout case.")
        result = await asyncio.wait_for(fetch_data(), timeout=10)
        return func.HttpResponse(f"✅ Result: {result}")
    
    except asyncio.TimeoutError as e:
        logging.error("⏱️ TimeoutError: fetch_data exceeded 10-second limit.")
        logging.exception(e)
        return func.HttpResponse("⏱️ Timeout occurred.", status_code=500)

    except Exception as e:
        logging.error(f"❌ Unexpected error in timeout case: {e}")
        logging.exception(e)
        return func.HttpResponse("❌ Internal server error.", status_code=500)

async def fetch_data():
    await asyncio.sleep(15)  # מדמה תקיעה
    return "done"
