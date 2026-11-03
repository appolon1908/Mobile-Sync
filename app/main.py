from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel
app=FastAPI(title="Codestra Mobile Sync",version="0.1.0")
class Job(BaseModel):
    device_id:str;kind:str
@app.get("/v1/health")
def health():return {"status":"ok"}
@app.post("/v1/sync/jobs",status_code=202)
def create_job(body:Job,x_service_identity:str|None=Header(None)):
    if not x_service_identity:raise HTTPException(401,"service identity required")
    if body.kind not in {"contacts","media"}:raise HTTPException(422,"unsupported sync kind")
    return {"device_id":body.device_id,"kind":body.kind,"status":"queued"}