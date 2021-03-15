@echo off
if "%1" == "" exit /b
::%1 source
if "%2" == "" exit /b
::%2 destination

xcopy /t/e "%1" "%2">nul


