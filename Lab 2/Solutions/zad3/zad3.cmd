@echo off
NET SESSION >nul 2>&1
IF %ERRORLEVEL% == 0 (
    ECHO Wykryto prawa administratora!
) ELSE (
    ECHO NIE wykryto praw administratora!
)

EXIT /B 0