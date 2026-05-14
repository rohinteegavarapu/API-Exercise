from fastapi import FastAPI

# This creates our "waiter"
app = FastAPI()

# This tells the waiter what to do when someone goes to the home page ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to my first API!"}
