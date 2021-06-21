@ECHO OFF
set /p pathsource=Podaj sciezke zrodlowa: 
set /p pathtarget=Podaj sciezke docelowa: 
xcopy "%pathsource%" "%pathtarget%" /T /E 
::"/T /E will include empty folders and subfolders"