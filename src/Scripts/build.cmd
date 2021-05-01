@echo off
pipenv install --skip-lock
IF "%1"=="dev" GOTO dev
IF "%1"=="rmtool" GOTO rmtool
IF "%1"=="viewer" GOTO viewer

:Release
echo Build command [Release]
pyinstaller -F -w viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL --icon=assests/icon.ico
GOTO rmtool

:viewer
echo Build command [Build viewer]
pyinstaller -F -w viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL --icon=assests/icon.ico
GOTO End

:Dev
echo Build command [Dev]
pyinstaller -F viewer.py .\question.py .\tools.py --hidden-import=toml --hidden-import=PIL --icon=assests/icon.ico
GOTO End

:rmtool
echo Build command [Build RemoveTool]
pyinstaller -c -F removePackage.py
copy dist/removePackage.exe .
GOTO End

:NSIS
echo Build command [Compile NSIS Installer]

:End
copy config.json dist
copy assests\icon.ico dist