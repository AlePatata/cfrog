import typer

app = typer.Typer()

@app.command()
def hello():
    print("Hello from frog!")

@app.command()
def bye(formal: bool = False):
    if formal:
        print("Bye Mr. Frog")
    else:
        print("chao sapoql")


if __name__ == "__main__":
    app()
