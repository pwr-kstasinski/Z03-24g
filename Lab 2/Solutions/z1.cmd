@echo off
if "%1" == "" exit /b
::%1 path
if "%2" == "" exit /b
::%2 extension

dir /a-d /b "%2\*%1"
