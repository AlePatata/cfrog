import json
from .models import Project, Problem

template_content = """#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    return 0;
}
"""

def load_project() -> Project:
    with open("cfrog.json", "r", encoding="utf-8") as f:
        project_info = json.load(f)
    return Project.model_validate(project_info)

def write_project(project: Project):
    with open("cfrog.json", "w", encoding="utf-8") as f:
        f.write(project.model_dump_json(indent=2))


def init_project():
    project = Project(
        name="frog",
        problems={},
        contests={},
    )
    write_project(project)

def write_problem(problem: Problem, template: bool = False):
    with open(f"{problem.name}.cpp", "w", encoding="utf-8") as f:
        content = "// start your code here"
        if template:
            content = template_content 
        f.write(content)

