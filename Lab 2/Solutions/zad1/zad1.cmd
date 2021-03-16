@echo off
SetLocal EnableDelayedExpansion

if "%1" == "-h" (
    echo ---Help---
    echo zad1.cmd [directory] [extension]
    echo This script shows names of files with passed extension in passed directory
    echo default options:
    echo   extension = .*
    echo   directory = .
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set directory=.
) else (
    set directory=%1
)

if "%2" == "" (
    set extension=*.*
) else (
    set extension=%2
)

echo Directory: %directory%
echo Extension: %extension%

echo Founded files:
for /r %directory% %%x in (%extension%) do echo %%~nxx

EXIT /B %ERRORLEVEL%