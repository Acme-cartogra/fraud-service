from fastapi import FastAPI

app = FastAPI(title="fraud-service", version="1.0.0")

@app.get("/actuator/health")
def health(): return {"status": "UP"}

@app.get("/frauds")
def route_0(): return {"status": "ok"}

@app.post("/frauds")
def route_1(): return {"status": "ok"}

@app.get("/frauds/{id}")
def route_2(): return {"status": "ok"}
