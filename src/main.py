import uvicorn

HOST = "0.0.0.0"
PORT = 8000
APP_NAME = "app.http.main:app"


if __name__ == "__main__":
    uvicorn.run(APP_NAME, host=HOST, port=PORT, reload=True)
