@echo off
setlocal enabledelayedexpansion
set /a P=0
set /a C=1
for /l %%x in (1, 1, %1) do (
	echo !C!
	set /a N=!P!+!C!
	set /a P=!C!
	set /a C=!N!
)