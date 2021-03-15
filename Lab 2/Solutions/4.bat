@echo off
set /a P=0
set /a C=1
for /l %%x in (1, 1, %1) do call :Loop
goto End
:Loop
	echo %C%
	set /a N=%P%+%C%
	set /a P=%C%
	set /a C=%N%
:End