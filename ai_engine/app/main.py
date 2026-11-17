from fastapi import FastAPI

app = FastAPI(title="FitCheck Intelligence Engine")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "FitCheck MAS Layer"}