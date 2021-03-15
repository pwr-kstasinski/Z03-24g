@echo off
if "%1" == "" exit/b
::%1 n

setlocal ENABLEDELAYEDEXPANSION

set mul=1

for /l %%i in (1,1,%1) do (
	set /A mul*= %%i
)
echo !mul!