rem Small script for running the init file, as some people are
rem unable to use basic logcal thinking.
rem
rem If needed change the scale variable below (the 2.0 part) to
rem better fit your system.


@echo OFF

set "scale=2.0"
python -m pip install -r .requirements
python "%~dp0init.py" -dpi=%dpi%

pause
