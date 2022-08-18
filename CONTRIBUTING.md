# Contributing to leetcode_py

## Workspace

- Use the setup from the project `Pipfile` using [Pipfile](https://github.com/pypa/pipfile).

## Template

Add the following items with respect to the problem solved.

- A definitions/[definition].py file where [definition] is the lower snake_case name of the introduced class. It's okay to add common testing functionality here that remains unused in the problem. These usually are not required. If one is required, it has probably already been defined.
- A problems/[problem_title].py file where [problem_title] is the lower snake_case title of the problem. Use a reasonable alternative if it begins with a number beyond the problem number.
  - The solution function as the lower snake_case version of the function used in the problem.
  - Additional helping functions used for the problem.
- A tests/test\_[problem_title].py where [problem_title] is again the lower snake_case title of the problem.
  - Cover each example in a test\_[example_n] function where [example_n] is the associated example from the problem description in lower snake_case.
  - Cover each additional discovered test\_[distinction] function where [distinction] is what caused the test to fail in the problem submission in lower snake_case.

## Commit message

Use a [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style of commit message. Where [optional_scope] is the problem file added and [description] is the problem function. Completing a problem is considered a feat.

## Checks

These checks from the Pipfile dev-packages section should pass. These are checked in the project actions.

- `pipenv run isort . --profile black`
- `pipenv run black .`
- `pipenv run pylint **/*.py`
- `pipenv run mypy .`
- `pipenv run pytest` # include the new tests

## Evaluation

Solution quality is evaluated on a subjective mix of big o time, brevity, quality, and other traits. Problems should follow a functional, iterative, recursive, or other programming style depending on what fits the problem best. Use abstractions from the Python standard library where it makes sense to do so.
