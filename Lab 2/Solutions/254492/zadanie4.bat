@echo off
@REM W tym zadaniu zakladam, ze zerowy wyraz ciagu fibonacciego to 0, pierwszy to 1, itd.

if %1% LSS 0 (
    echo Error - given number has to be positive or 0
    goto :eof

)
SET /A a = 0
SET /A b = 1


FOR /l %%i IN (0, 1, %1) DO call :ForBody
goto :eof

:ForBody
echo %a%
set /A helper = %b%
set /A b = %a% + %b%
set /A a = %helper%
goto :eof

:eof