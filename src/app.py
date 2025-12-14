from fastapi import FastAPI

app = FastAPI(title="Azure Enterprise Document Intelligence (MVP)")

@app.get("/health")
def health():
    return {"status": "ok"}
