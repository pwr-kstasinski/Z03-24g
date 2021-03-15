@echo off
if "%1" == "" exit/b
::%1 number count (first is 1)

setlocal ENABLEDELAYEDEXPANSION

set A=1
set B=1

for /l %%i in (1,1,%1) do (
	echo !A!
	set /A C= A+B
	set /a A = B
	set /a B = C
)
