from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers import productController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/ProductImages", StaticFiles(directory="ProductImages"), name="ProductImages")
app.include_router(productController.router)

app.add_middleware(
    CORSMiddleware, allow_origins=["http://127.0.0.1:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers =["*"]
)