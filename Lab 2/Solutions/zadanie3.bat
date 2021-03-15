@echo off

net session >nul 2>nul
    if %errorLevel% == 0 (
        echo Masz uprawnienia administratora.
    ) else (
        echo Nie masz uprawnien administratora.
    )