@echo off
if "%1" == "" exit/b	
::%1 filename
if "%2" == "" exit/b
::%2 frame number
if "%3" == "" exit/b
::%3 icon name

ffmpeg -y -ss %2 -i %1 -vframes 1 %3 >nul 2>nul