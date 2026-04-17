from pydantic import (
    BaseModel,
    ConfigDict,
    FilePath,
    HttpUrl,
)


class BaseCfrog(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        strict=True,
    )


class TestCase(BaseCfrog):
    input: str
    output: str


class Problem(BaseCfrog):
    path: FilePath
    name: str
    url: HttpUrl | None
    accepted: bool = False
    problem_statement: str = ""
    examples: list[TestCase] = []


class Contest(BaseCfrog):
    path: FilePath
    name: str
    url: str
    problems: list[Problem]


class Project(BaseCfrog):
    name: str
    compile_command: list[str]
    problems: list[Problem]
    contests: list[Contest]
