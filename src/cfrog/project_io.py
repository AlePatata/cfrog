import json
from .models import Project

def load_project() -> Project:
    with open("cfrog.json", "r", encoding="utf-8") as f:
        project_info = json.load(f)
    return Project.model_validate(project_info)

def init_project():
    project = Project(
        name="frog",
        problems=[],
        contests=[],
    )
    with open("cfrog.json", "w", encoding="utf-8") as f:
        f.write(project.model_dump_json(indent=2))

