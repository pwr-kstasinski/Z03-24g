@echo off
if "%~1" == "" exit/b
::%1 directory name/path
::%2 offset

dir/b/ad "%~1" >tmpPrintStruct


for /f "tokens=*" %%i in (tmpPrintStruct) do (
	echo %2%%i
	call %0 "%~1\%%i" %2....
)

if exist tmpPrintStruct del /q/f tmpPrintStruct>nul


