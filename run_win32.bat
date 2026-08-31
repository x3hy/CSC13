@echo OFF


rem Small script for running the init file, as some people are
rem unable to use basic logcal thinking.
rem
rem If needed change the scale variable below (the 2.0 part) to
rem better fit your system.


echo In order for the graphical system to work
echo please download and install vs buildtools.
echo To do this please go to the following URL:
echo https://aka.ms/vs/stable/vs_BuildTools.exe
echo
echo This will download vs_BuildTools.exe, please
echo run this file and wait 1-2 minutes for it to
echo install, thank you
echo
echo Once this is finished: Press any key to continue
pause


rem Install requirements
python -m pip install -U pip
python -m pip install flask --exists-action abort
if %ERRORLEVEL% neq 0 (
    echo An error occurred!
)


rem Run the main program initialisation file
python "%~dp0init.py"
if %ERRORLEVEL% neq 0 (
    echo An error occurred!
)


pause
