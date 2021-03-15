@echo off 

set /p n="Enter N - "

setlocal EnableDelayedExpansion

set /a silnia=1

for /l %%i in (1,1,%n%) do  (

set /a silnia=!silnia!*%%i


)

echo !silnia!

endlocal
pause