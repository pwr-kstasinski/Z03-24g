@echo off

rem podajemy nasz katalog zrodlowy

set count=1 
call :getSubFolderList %~1
goto :eof

:getSubFolderList  
    for /d %%a in (%~f1\*) do (
	call :print %%~fa
	set /a count-=1 
)
    goto :eof

:print

for /l %%a in (1,1,%count%) do echo |set /p level=______
echo %count% %~1

set /a count+=1
call :getSubFolderList %~1 