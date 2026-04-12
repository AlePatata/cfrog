from .models import Project

template_content = """#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    return 0;
}
"""


def load_project() -> Project:
    with open("cfrog.json", "r", encoding="utf-8") as f:
        return Project.model_validate_json(f.read())


def write_project(project: Project):
    with open("cfrog.json", "w", encoding="utf-8") as f:
        f.write(project.model_dump_json(indent=2))


def write_problem(name: str, template: bool = False):
    with open(f"{name}.cpp", "w", encoding="utf-8") as f:
        content = "// code goes here"
        if template:
            content = template_content
        f.write(content)
