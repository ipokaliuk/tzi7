from fastapi import FastAPI 
import uvicorn 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, HTTPS world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="mycert.key", ssl_certfile="mycert.crt")
