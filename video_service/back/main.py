import uvicorn
from fastapi import FastAPI
from timecode_api import routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(routes.router)

origins = [
    "http://localhost",
    "http://192.168.1.64:8080/",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
