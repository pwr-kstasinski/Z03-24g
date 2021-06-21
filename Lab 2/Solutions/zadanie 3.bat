@ECHO OFF
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Uruchomiono jako administrator
) else (
    echo Nie uruchomiono jako administrator!
)

PAUSE