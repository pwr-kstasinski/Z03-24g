@echo off

:start


set /p n="Z jakiej liczby pragniesz silnii?: "
set counter=n

:loop

if %counter% EQU 1 (
goto End
)
set /a counter=%counter%-1
set /a n=%n%*%counter%
goto loop

:End
echo %n%