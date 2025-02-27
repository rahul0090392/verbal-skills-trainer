from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI application instance


@app.get("/")  # Define a GET request handler for the root path
async def root():
    return {"message": "Hello World!"}
