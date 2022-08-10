# Contributing to leetcode_py

## Workspace

* Use the setup from the project `Pipfile` using [Pipfile](https://github.com/pypa/pipfile).

## Template

Add the following items with respect to the problem solved.

* A definitions/[definition].py file where [definition] is the lower snake_case name of the introduced class. It's okay to add common testing functionality here that remains unused in the problem.
* A problems/[problem_title].py file where [problem_title] is the lower snake_case title of the problem.
  * The solution function as the lower snake_case version of the function used in the problem.
  * Additional helping functions used for the problem.
* A tests/test_[problem_title].py where [test_problem_title] is the is again the lower snake_case title of the problem.
  * Cover each example in a test_[example_n] function where [example_n] is the associated example from the problem description in lower snake_case.
  * Cover each additional discovered test_[distinction] function where [distinction] is what caused the test to fail in the problem submission in lower snake_case.

## Commit message

Use a [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style of commit message. Where [optional_scope] is the problem file added and [description] is the problem function. Completing a problem is considered a feat.

## Checks

These checks from the Pipfile dev-packages section should pass. These are checked in the project actions.

* `pipenv run isort .`
* `pipenv run pylint **/*.py`
* `pipenv run pytest` (with the new tests)
* `pipenv run black .`


## Evaluation

Solution quality is evaluated on a subjective mix of big o time, brevity, quality, and other traits.
