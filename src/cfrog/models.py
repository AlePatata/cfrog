from pydantic import BaseModel

class TestCase(BaseModel):
    input: str
    output: str

class Problem(BaseModel):
    name: str
    url: str
    accepted: bool
    problem_statement: str
    examples: list[TestCase]

class Contest(BaseModel):
    name: str
    url: str
    problems: list[Problem]

class Project(BaseModel):
    name: str
    problems: list[Problem]
    contests: list[Contest]

