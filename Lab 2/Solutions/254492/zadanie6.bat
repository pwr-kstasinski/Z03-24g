@echo off

set /A depth = 0
call :VisitFolder %1 , ,
goto :eof

:VisitFolder
set /A depth = %depth% + 1
for /F "delims=" %%i in ('dir "%~2%3%~1" /b /ad') do call :PrintFolder "%%i", "%~2%3%~1"
set /A depth = %depth% - 1
goto :eof

:PrintFolder
for /L %%i in (2, 1, %depth%) do echo |set /p dummyVariable=......
echo !-----%~1
call :VisitFolder "%~1" , %2 , \
