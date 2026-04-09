import typer
from .project_io import load_project, init_project
from rich import print

app = typer.Typer()

@app.command()
def show():
    print(load_project().model_dump())

@app.command()
def init():
    init_project()


if __name__ == "__main__":
    app()
