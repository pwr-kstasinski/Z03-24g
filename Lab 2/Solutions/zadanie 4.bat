@ECHO OFF
SETLOCAL EnableDelayedExpansion

set /p n=Podaj N: 
IF %n% LEQ 0 (
    echo Nieprawidlowe N!
) ELSE (
    IF %n% GEQ 1 (
        echo 1
    )
    IF %n% GEQ 2 (
        echo 1
    )
    set /A prev=1
    set /A act=1
    FOR /L %%G IN (3, 1, %n%) DO (
        set /A suma=!prev!+!act!
        set /A prev=!act!
        set /A act=!suma!
        echo !suma!
    )
)
PAUSE

