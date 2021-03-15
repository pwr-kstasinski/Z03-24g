@echo off
set /p extension="Enter file extension - "
set /p directory="Enter directory - "

FOR /R %directory% %%i IN (*.%extension%) DO  echo  %%i

pause