@echo off

if "%1" == "-h" (
    echo ---Help---
    echo zad6.cmd [source]
    echo This script lists folders in source.
    echo default options:
    echo   source = .
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set source=.
) else (
    set source=%1
)

echo Source: %source%
call :ListFolders %source% ""
EXIT /B %ERRORLEVEL%

Rem ListFolders(source, prefix)
:ListFolders
for /f %%D in ('dir %~1 /a:d /b') do (
    echo %~2%%~nxD
    call :ListFolders %~1\%%~nxD "%~2-"
)
EXIT /B 0