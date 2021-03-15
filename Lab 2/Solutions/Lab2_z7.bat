@echo off

setlocal EnableDelayedExpansion 

set /a res = 1
set /a n=%1

for /l %%i in (1,1,%n%) do (set /a res = !res! * %%i )

echo %res%

endlocal
pause