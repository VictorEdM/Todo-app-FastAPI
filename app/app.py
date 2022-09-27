from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["ROOT"])
async def root() -> dict:
    return {"Ping": "Pong"}


#Get/all
@app.get("/todos", tags=["TODOS"])
async def fetch_to_dos() -> dict:
    return {"data": todos}


#Get/id
@app.get("/todos/{todo_id}", tags=["ONE TODO"])
async def fetch_one_to_do(todo_id: int) -> dict:
    return {"data": list(filter(lambda todo: todo.get("id") == todo_id, todos))[0]}

#Post
#Update
#Delete


todos = [
    {
        "id": 1,
        "activity": "Wash car"
    },
    {
        "id": 2,
        "activity": "Read 'The Sea-Wolf'"
    }
]