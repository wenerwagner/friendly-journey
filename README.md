# friendly-journey

## Temp

### Tasks
- [ ] Install pytest and create basic tests.
- [ ] Create CI/CD pipeline running tests.
- [ ] Install and configure ruff.
- [ ] Install and configure mypy.
- [ ] Add to linter to CI/CD pipeline.
- [ ] Add static type checker to CI/CD pipeline.
- [ ] Add pre-commit hook with linter, formatting and testing.
- [ ] Dockerize application.
- [ ] Deploy in some place (AWS, Azure, GCP?).

## Requisites

You should have installed:
- Python 3.14.3
- Poetry 2.3.2

## Development

- Make sure that you have all the requisites correctly installed.
- Install the dependencies with:
    ```
    poetry sync
    ```
- Activate the poetry environment with:
    ```
    poetry env activate
    ```

### Running the application

- Run the command:
    ```
    fastapi dev src/friendly-journey/main.py
    ```
### Notes

- Requisites (tech needed to run the project)
- Package Manager: poetry
- Linter: ruff
- Formater: ruff
- Static Type Checker: mypy
- Good information in README

### Future topics

- Toml formatter.
- Markdown formatter.
- OpenAPI customization.