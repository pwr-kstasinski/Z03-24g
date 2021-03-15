@echo off
SetLocal EnableDelayedExpansion

if "%1" == "-h" (
    echo ---Help---
    echo zad7.cmd [number]
    echo This script calculates factorial of given number.
    echo default options:
    echo   number = 5
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set number=5
) else (
    set number=%1
)


echo Number: %number%
set factorial=1
call :Factorial %number%
echo Factorial: %factorial%
EXIT /B %ERRORLEVEL%

Rem Factorial(number)
:Factorial
if not %~1 == 1 (
    set /a factorial = factorial * %~1
    set /a val = %~1 - 1
    call :Factorial !val!
)
EXIT /B 0