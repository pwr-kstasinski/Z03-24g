@echo off

rem jako argument podajemy ile wyrazow ciagu fibonnaciego chcemy policzyc 

set f0= 0 

set f1=1

set result=1

set param=%1
if %param% lss 1 (
echo wrong input
pause
)else call :Fibonacci
goto :eof

:Fibonacci 

echo %result%
set /a result = %f0% + %f1%
set /a f0= %f1%

set /a f1=%result%

set /a param-=1


IF %param% GTR 0 (
GOTO Fibonacci)

pause
