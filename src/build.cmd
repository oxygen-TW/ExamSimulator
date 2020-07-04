pipenv install --skip-lock
IF "%1"=="dev" GOTO dev

:Release
echo Build command [Release]
pyinstaller -F -w viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL
GOTO End

:Dev
echo Build command [Dev]
pyinstaller -F viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL
GOTO End

:End
copy config.json dist