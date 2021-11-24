# run with: uvicorn main:app --reload

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def dashboard():
    """
    [summary]
    this is the docstring for the dashboard

    Returns:
        [type]: [description]
    """
    return {"Hello": "World 2"}

@app.get("/about")
def dashboard():
    """
    [summary]
    the about page

    Returns:
        [type]: [description]
    """
    return {"This is the About Page. Welcome!"}

# if __name__ == '__main__':
#     uvicorn.run(app)
