from fastapi import FastAPI, status, HTTPException


app = FastAPI()


@app.get("/", tags=["ROOT"])
async def root() -> dict:
    return {"Ping": "Pong"}


#Get/all
@app.get("/todos", tags=["GET ALL TODOS"], status_code=status.HTTP_200_OK)
async def fetch_todos() -> dict:
    if todos:
        return {"data": todos}
    raise HTTPException(
        detail="No todos on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )


#Get/id
@app.get("/todos/{todo_id}", tags=["GET ONE TODO"], status_code=status.HTTP_200_OK)
async def fetch_one_todo(todo_id: int) -> dict:
    todo: dict = list(filter(lambda t: t.get("id") == todo_id, todos))[0]
    if todo:
        return {"data": todo}
    raise HTTPException(
        detail=f"No todo with id {todo_id} on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )


#Post/to do
@app.post("/todos", tags=["ADD TODO"], status_code=status.HTTP_201_CREATED)
async def add_todo(todo: dict) -> dict:
    if todo:
        todos.append(todo)
        return {"data": todo}
    raise HTTPException(
        detail="Todo not created. Body request must be empty",
        status_code=status.HTTP_204_NO_CONTENT
    )

#Update/id/activity?
#Delete/id


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