import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app:app", port=15000, reload=True)
