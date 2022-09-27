from fastapi import FastAPI, status, HTTPException
from .schema import Todo

app = FastAPI()


#GET
@app.get("/todos", tags=["GET ALL TODOS"], status_code=status.HTTP_200_OK)
async def fetch_todos() -> dict:
    if todos:
        return {"data": todos}
    raise HTTPException(
        detail="No todos on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )


#GET
@app.get("/todos/{todo_id}", tags=["GET ONE TODO"], status_code=status.HTTP_200_OK)
async def fetch_one_todo(todo_id: int) -> dict:
    todo: Todo | None = list(filter(lambda t: t.id == todo_id, todos))[0]
    if todo:
        return {"data": todo}
    raise HTTPException(
        detail=f"No todo with id {todo_id} on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )


#POST
@app.post("/todos", tags=["ADD TODO"], status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    if todo:
        todos.append(todo)
        return {"data": todo}
    raise HTTPException(
        detail="Todo not created. Body request must be empty",
        status_code=status.HTTP_204_NO_CONTENT
    )


#PUT
@app.put("/todo/{todo_id}", tags=["UPDATE TODO"], status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, activity: str) -> dict:
    todo = list(filter(lambda t: t.id == todo_id, todos))[0]
    if todo:
        todo.activity = activity
        return {"data": todo}
    raise HTTPException(
        detail=f"No todo with id {todo_id} on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )


#Delete
@app.delete("/todo/{todo_id}", tags=["DELETE TODO"], status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int) -> None:
    todo = list(filter(lambda t: t.id == todo_id, todos))[0]
    if todo:
        todos.remove(todo)
        return
    raise HTTPException(
        detail=f"No todo with id {todo_id} on the list",
        status_code=status.HTTP_404_NOT_FOUND
    )
    

todos: list[Todo] = [
    Todo(id=1, activity="Wash car"),
    Todo(id=2, activity="Read 'The Sea-Wolf'"),
    Todo(id=3, activity="Buy some food for the week"),
    Todo(id=4, activity="Fix the shower"),
    Todo(id=5, activity="Sleep for 30 minutes")
]
