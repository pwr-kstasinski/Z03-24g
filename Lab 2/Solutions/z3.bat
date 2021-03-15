@echo off

net session >nul 2>&1

if %errorLevel% == 0 (
echo Administrator
) else (
echo Not administrator
)

pause