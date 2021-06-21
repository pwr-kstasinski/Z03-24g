@ECHO OFF


set /p path=Podaj sciezke z plikiem wideo: 
ffmpeg.exe -i "%path%" -ss 00:00:01.000 -vframes 1 thumbnail.png
PAUSE