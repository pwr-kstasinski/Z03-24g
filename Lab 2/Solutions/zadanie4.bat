@echo off

setlocal EnableDelayedExpansion
set N0=0
set N1=1

for /L %%x in (1, 1, %1) do (
    echo !N1!
    set /a N1 += !N0!
    set /a N0 = !N1! - !N0!
)