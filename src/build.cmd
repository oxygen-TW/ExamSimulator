pipenv run pip freeze > requirements.txt
rem pip install -r requirements.txt
pyinstaller -F -w viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL
copy config.json dist