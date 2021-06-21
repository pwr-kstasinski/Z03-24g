@echo off

ECHO %~1
CALL :print "%~1" "   "
goto :eof

:print
FOR /D %%I IN ("%~1\*") DO (
    echo %~2%%~nxI
    CALL :print "%~1\%%~nxI" "%~2   "
)

