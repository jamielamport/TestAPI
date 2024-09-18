from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return "Welcome to the books api"

@app.get("/test")
def get_test():
    return "blah blah"
