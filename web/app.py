from fastapi import FastAPI
import asyncio
import uvicorn
app = FastAPI()

@app.get("/async")
async def async_api():
    await asyncio.sleep(5)
    return {"msg": "done"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)