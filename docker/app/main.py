from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "voce esta indo muito bem com fastAPI"}

@app.get("/api/{name}")
async def get_user(name):
    return{
        "name": name,
        "message": f"Hello, {name} from fastAPI"
    }