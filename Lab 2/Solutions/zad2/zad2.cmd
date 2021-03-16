@echo off
SetLocal EnableDelayedExpansion

if "%1" == "-h" (
    echo ---Help---
    echo zad2.cmd [destination] [source]
    echo This script copies folders from source path do destination path
    echo default options:
    echo   destination = .\test_destination
    echo   source = .
    echo ----------
    exit /B %ERRORLEVEL%
)

if "%1" == "" (
    set destination=.\test_destination
) else (
    set destination=%1
)

if "%2" == "" (
    set source=.
) else (
    set source=%2
)

echo Source: %source%
echo Destination: %destination%
echo Working...
call :CopyFolders %source% , %destination%
echo Done.
EXIT /B %ERRORLEVEL%

Rem CopyFolders(source, destination)
:CopyFolders
for /f %%D in ('dir %~1 /a:d /b') do (
    mkdir %~2\%%~nxD
    call :CopyFolders %~1\%%~nxD %~2\%%~nxD
)
EXIT /B 0
