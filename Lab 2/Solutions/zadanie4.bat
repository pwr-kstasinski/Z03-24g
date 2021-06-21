
@echo off

:start


set /p n="ile pragniesz zobaczyć cyfer fibonnacciego: "
set t1=0
set t2=1
set nT=1
if %n% EQU 0 (
goto End
)
if %n% EQU 1 (
echo %t1%
goto End
)
echo %t1%
echo %t2%
set /a n=%n%-2
set counter=0 



:loop

if %counter% GEQ %n% (
pause>nul
goto End
)
echo %nT%
set /a t1=%t2%
set /a t2=%nT%
set /a nT=%t1%+%t2%
set /a counter=%counter%+1
goto loop


:End