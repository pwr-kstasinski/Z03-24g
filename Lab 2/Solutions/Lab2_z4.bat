@echo off


set /a a=1
set /a b=0
set /a res=0
set /a i=%1

:loop
   echo %res%
   set /a res= %a% + %b%
   set /a a=%b%
   set /a b=%res%
   set /a i-=1
   if %i% GTR 0 (goto loop:)




pause