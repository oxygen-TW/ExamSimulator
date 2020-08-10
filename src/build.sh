pipenv install --skip-lock
if [ "$1" = "dev" ]
then
    echo Build command [Dev]
    pyinstaller -F viewer.py question.py tools.py --hidden-import=toml --hidden-import=PIL --hidden-import=tkinter --hidden-import='PIL._tkinter_finder'
elif [ "$1" = "install" ]
then
    sudo apt-get install python3 python3-tk python3-pip
    sudo pip3 install pyinstaller
else
    echo Build command [Release]
    pyinstaller -F -w viewer.py question.py tools.py --hidden-import=toml --hidden-import=PIL --hidden-import=tkinter --hidden-import='PIL._tkinter_finder'
fi

#cp config.json dist