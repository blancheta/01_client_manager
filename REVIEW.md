
# Client Manager Review

## General
- Delete unused files
- Rename client_manager_sqlalch.py to run.py
- Add requirements.txt file at the root of the project which lists project dependencies (e.g: rich) with a fixed version [More info here => requirements.txt](https://www.freecodecamp.org/news/python-requirementstxt-explained/#:~:text=requirements.txt%20is%20a%20file,environment%20and%20makes%20collaboration%20easier.)
- Add docstrings for each function using the sphinx format [Sphinx docstring](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
- Add typing for inputs/outputs [Typing doc](https://docs.python.org/es/3/library/typing.html)
- Use logging.info, logging.error instead of print [Print vs Logging](https://stackoverflow.com/questions/6918493/in-python-why-use-logging-instead-of-print)
- Isolate validation loops into functions. (You could create a new file called validators which will contain each function doing a field validation)
- You could remove print() by adding a \n before the string on the next print?
- Install pylint (Python linter)
- Fix pylint errors
- Install black
- Use black to automatically clean the source code
- Install isort
- Use isort to reorder imports and clean unused imports
- Install mypy (To check typing)
- Check typing with [mypy](https://mypy-lang.org/)
- Install [commitizen](https://commitizen-tools.github.io/commitizen/) (A commit message checker to make sure all commit messages follow a same pattern)
- Move the logic into three different files
  - *models.py* to store the Base, Client model definition
  - *views.py* to store functions responsible to display/interact with the user
  - *controllers.py* which will contain the current logic and will interact with the database and will call functions in views.py to show stuff/interact with the user
