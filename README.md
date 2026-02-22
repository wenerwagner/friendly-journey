# friendly-journey

## Temp

### App Version 0.1.0

- Project should have initial good folder structure.
- Create CRUD operations for User.
- User have name, e-mail and password.
- Everything should be stored in memory.
- The application should be deployed and accessible in some place.

### App Version 0.2.0

- ID generation and handling. Maybe using dependency injection.
- Use Pydantic for models.
- The password should be correctly stored (encrypted).
- The application should have CI/CD for deploy and testing.
- We should have basic testing.
- The API should have api versioning like `/api/v1` in the path.
- E-mail should be unique.

### Tasks
- [X] Define application version 1.0.0.
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