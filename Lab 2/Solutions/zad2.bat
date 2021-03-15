@echo off

REM Podajemy sciezke zrodlowa oraz docelowa aby skopiowac pliki

xcopy %1 %2 /t /e

if %ERRORLEVEL% neq 0 goto ERR
echo Copying done successfully!!
pause
goto:eof
:ERR
echo Error during copying
pause

