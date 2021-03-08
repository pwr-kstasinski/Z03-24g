@echo off
net session >nul 2>&1
if %errorlevel% equ 0 (
    echo running as administrator
) else (
    echo not in admin mode
)