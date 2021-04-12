@echo off
set /p path ="Podaj katalog"
set /p ext ="Podaj typ pliku"
cd %path%
dir %.ext% /b
pause