@echo off
set "padding= "
set padding=%padding:~1%
call :Process %1 .
goto End
:Process
	echo %padding%%~2
	set padding=	%padding%
	for /f "tokens=*" %%D in ('dir %1 /b /ad') do call :Process "%~1/%%D" "%%D"
	set padding=%padding:~1%
:End