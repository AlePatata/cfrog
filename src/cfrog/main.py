import os
from pathlib import Path

import typer
from pydantic import HttpUrl, ValidationError
from rich import print  # noqa: A004
from rich.table import Table
from rich.console import Console

from .models import Problem, Project
from .project_io import load_project, write_problem, write_project
from .run import build

console = Console()
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


@app.command(name="list")
@app.command(name="ls")
def list():
    project = load_project()
    table = Table("name", "path", "status")

    for problem in project.problems:
        status = "[green]accepted[/green]" if problem.accepted else "[yellow]unsolved[/yellow]"
        table.add_row(problem.name, str(problem.path), status)

    console.print(table)


@app.command()
def add(url: str, template: bool = True, name: str | None = None):
    name = name or url.split("/")[-1]
    write_problem(name, template=template)
    problem = Problem(
        path=Path(f"{name}.cpp"),
        name=name,
        url=HttpUrl(url),
        accepted=False,
    )
    project = load_project()
    project.problems.append(problem)
    write_project(project)


@app.command()
def accept(problem_name: str):
    project = load_project()
    problem = next(
        (problem for problem in project.problems if problem.name == problem_name), None
    )
    if problem is None:
        print("Problem not found.")
        return
    problem.accepted = True
    write_project(project)


@app.command()
def run(file):
    build(Path(file), Path("a.out"))
    os.execv("a.out", ["a.out"])


if __name__ == "__main__":
    app()
