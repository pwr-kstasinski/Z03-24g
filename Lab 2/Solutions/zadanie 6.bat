@ECHO OFF

set /p path=Podaj sciezke: 
call:dirListRec %path%

::1. argument: aktualna sciezka
::2. argument: glebokosc
:dirListRec 
    dir %~1%/b /ad
goto :eof


