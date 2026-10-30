from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from processor import LogsProcessor
from execution_time import LogsTimer

app = FastAPI()
processor = LogsProcessor()

class LogsRequest(BaseModel):
    logs: list[str]
    filter_level: str

class LogsResponse(BaseModel):
    Processed_count: int
    Match_count: int
    execution_time: float
    Matching_logs: list[str]

@app.post("/Logs_filter/by keyword/", response_model=LogsResponse)
def logs_filter(log_batch: LogsRequest):        
    try:
        timer = LogsTimer()
        with timer:
            result = processor.log_filter(log_batch.model_dump())

        result["execution_time"] = timer.elapsed_time

        return result
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host="localhost")    