from fastapi import FastAPI
import os
from fastapi import UploadFile, File
from fastapi import Request
import uvicorn
from typing import List
from dotenv import load_dotenv
load_dotenv()
from fasiss_handlers import *
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/normal_upload")
async def upload_file(request: Request, files: List[UploadFile] = File(...)):
    try:
        for file in files:
            filename = file.filename
            try:
                if file.content_type == "application/pdf":
                    content = await file.read()
                    filepath = filename
                    with open(filepath, "wb") as file:
                        file.write(content)
                    base=pdf_to_json_and_insert(filepath=file.name)
                    print(base)
                    if os.path.exists(file.name):
                        os.remove(file.name)
                else:
                    return {"staus":"fail","reason":"extension invalid only pdf must be uploaded"}
            except (Exception,BaseException) as e:
                print(str(e))
                if filepath is not None and os.path.exists(filepath):
                    os.remove(filepath)
                return {"status":"fail","reason":str(e)}
            if filepath is not None and os.path.exists(filepath):
                os.remove(filepath)
        return {"status": True,"docs_status":"context"}
    except Exception as e:
        return {"status":False,"error":str(e)}
    
@app.post("/predict")
async def predict(
    request: Request, query: str):
    try:
        response=retriever_faiss(query=query)
        return {"status":True,"response":response}
    except Exception as e:
        return{"status":False,"reason":str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)