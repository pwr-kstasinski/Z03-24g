@echo off

set /A result = 1

FOR /l %%i IN (%1, -1, 2) DO call :ForBody %%i
goto End

:ForBody
set /A result = %result% * %1
goto :eof

:End
echo %result%