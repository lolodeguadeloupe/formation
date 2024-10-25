import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
is_deployment = os.getenv("REPLIT_DEPLOYMENT") == "1"

counter = 0


@app.get("/api/counter")
async def get_counter():
  return {"counter": counter}


@app.post("/api/counter")
async def increment_counter():
  global counter
  counter += 1
  return {"counter": counter}

port = 8080
if is_deployment:
  app.mount("/", StaticFiles(directory="dist", html=True), name="dist")
  port = 5173

# Run the app
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=port)
