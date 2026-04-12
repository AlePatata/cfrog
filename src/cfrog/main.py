import typer
from pathlib import Path
from .project_io import load_project, write_problem, write_project
from rich import print
from .models import Project, Problem

app = typer.Typer()


@app.command()
def init():
    project = Project(
        name="frog",
        problems=[],
        contests=[],
    )
    write_project(project)


@app.command()
def show():
    project = load_project()
    print(project)


@app.command()
def add(name: str, template: bool = False):
    write_problem(name, template=template)
    problem = Problem(
        path=Path(f"{name}.cpp"),
        name=name,
        url=None,
        problem_statement="",
    )
    project = load_project()
    project.problems.append(problem)
    write_project(project)
    show()


if __name__ == "__main__":
    app()
