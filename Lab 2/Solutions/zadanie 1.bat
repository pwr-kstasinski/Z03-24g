@ECHO OFF
set /p extension=Podaj rozszerzenie: 
set /p path=Podaj sciezke: 
dir /b "%path%"\*.%extension%
PAUSE
