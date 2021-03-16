@echo off
SetLocal EnableDelayedExpansion

if "%1" == "-h" (
    echo ---Help---
    echo zad3.cmd [number]
    echo This script shows a given number of next fibonacci numbers.
    echo default options:
    echo   number = 10
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set number=10
) else (
    set number=%1
)

if %number% LSS 1 (
    echo Number can not be lower than one!
    exit /B %ERRORLEVEL%
)

echo Number: %number%
echo Numbers of fibonacci:

set first=0
set second=1

for /L %%x in (1,1,%number%) do (
    echo !first!
    set temp=!first!
    set first=!second!
    set /a second=!temp!+!second!
)

EXIT /B %ERRORLEVEL%