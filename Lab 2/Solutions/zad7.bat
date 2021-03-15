@echo off

rem podajemy liczbe z ktorej chcemy policzyc silnie

set result=1
set param=%1

FOR /L %%a IN (1,1,%param%) DO (
set /a result*=%%a
)
IF %param% == 0 set /a result=1
IF %param% lss 0 (
echo wrong input
goto :eof
)	
echo %result%
pause



