@ECHO OFF
FSUTIL DIRTY QUERY %systemdrive% >nul
IF NOT %errorlevel% == 0 echo No administrator rigths.