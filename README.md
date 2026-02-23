# Name to be defined (currently friendly-journey)

This project is an evolving backend that works as a place to exercise good practices, experiment new things, at the same time that I'm building tools for personal user.

Currently, this projects consist in:
- An API with CRUD operations a User (name, e-mail, password).
- The API is running within FastAPI as framework and uvicorn as ASGI web server.
- poetry is being used for dependency management.
- ruff for linting and formatting.

## Requisites

You should have installed:
- Python 3.14.3
- Poetry 2.3.2

## Development

- Make sure that you have all the requisites correctly installed.
- Install the dependencies with:
    ``` shell
    poetry sync
    ```
- Activate the poetry environment with:
    ``` shell
    poetry env activate
    ```

### Running the application

- Run the command:
    ``` shell
    fastapi dev src/friendly-journey/main.py
    ```

## Temp

### App Version 0.1.0

- Project should have initial good folder structure.
- Create CRUD operations for User.
- User have name, e-mail and password.
- Everything should be stored in memory.

### App Version 0.2.0

- Install ruff.
- Install pytest
- Create one basic test.
- Create CI/CD pipeline running tests.


### App Version 0.3.0

- Create unit tests and other tests.
  - Create some kind of default tests for CRUD API entities.
    - NotFound, status codes returns, etc.
- Add linter to CI/CD pipeline.
- Add formatting check to CI/CD pipeline.
- Add static type checker to CI/CD pipeline.
- Install and configure mypy.
- Configure ruff linter rules. 
- configure ruff formatting rules.
- Dockerize application.
- Deploy in some place (AWS, Azure, GCP?).
- ID generation and handling. Maybe using dependency injection.
- The password should be correctly stored (encrypted).
- The application should have CI/CD for deploy and testing.
- We should have basic testing.
- The API should have api versioning like `/api/v1` in the path.
- E-mail should be unique.
- Add pre-commit hook with linter, formatting and testing.

### Issues

- When running `python src/app/main.py` in the root of the project we have the following error:
```shell
Traceback (most recent call last):
  File "/home/wener/Projects/friendly-journey/src/app/main.py", line 4, in <module>
    from src.app.routers import users
ModuleNotFoundError: No module named 'src'
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
- Application versioning.
- Release notes.
- Restful API
- API development good practices.
- API security.
- API HATEOAS.
- Documentation.
- Python docstring.
- CORS.
- Rate limit.
- Pagination.
- Querying.
- API parameters.
- Error handling.
- Good testing for API Http Status semantic.
- Better http test solution, something automatic like Postman scripts, maybe something open-source.
- Versioning (Semantic Versioning)
- Review ruff rules and create something that make sense and can be reusable. Look for industry standards.
- It is possible to create customizable rules for ruff?
- Define ruff rules selection explicit to not relay on defaults.