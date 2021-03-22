@ECHO OFF
SETLOCAL EnableDelayedExpansion

set /p n=Podaj n: 
IF %n% LEQ 0 (
    echo Nieprawidlowe n!
) ELSE (
    set /A act=1
    FOR /L %%G IN (1, 1, %n%) DO (
        set /A act=!act!+!G!
        echo !act!
    )
)

PAUSE

