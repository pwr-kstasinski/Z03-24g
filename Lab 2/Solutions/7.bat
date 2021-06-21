@echo off
setlocal enabledelayedexpansion
set /a R=1
for /l %%n in (1,1,%1) do set /a R=!R!*%%n
echo %R%