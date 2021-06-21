@echo off
    rem sprawdzamy czy jestesmy zalogowani jako administrator

    echo Detecitng your current permissions:
    net session 1>nul 2>&1
    if %errorLevel% == 0 (
        echo Success: You are an administrator!!
    ) else (
        echo Failure: You are not an administrator.
    )

    pause 