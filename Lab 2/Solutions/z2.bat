@echo off

set /p directory="Enter directory - "

set /p copydirectory="Enter copy directory - "

xcopy  %directory% %copydirectory% /t /e

pause