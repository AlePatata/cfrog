import typer
from .project_io import load_project, init_project, write_problem, write_project
from rich import print
from .models import Project, Problem

app = typer.Typer()

@app.command()
def show():
    print(load_project().model_dump())

@app.command()
def init():
    init_project()

@app.command()
def add(name: str, template: bool = False):
    project = load_project()
    problem = Problem(name=name, url="", accepted=True, problem_statement="", examples=[])
    write_problem(problem, template=template)
    if problem.name in project.problems:
        return
    project.problems[name] = problem
    write_project(project)
    show()

if __name__ == "__main__":
    app()
