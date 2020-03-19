@echo off
setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure you want to save? This will overwrite your old save files.(Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END
rmdir /q /S Time\Saved\Laws 2>nul
rmdir /q /S Time\Saved\World 2>nul
del /q Time\Saved\File_Explorer.py 2>nul
xcopy /y /q /H /E /I Laws Time\Saved\Laws\
xcopy /y /q /H /E /I World Time\Saved\World\
copy /y  File_Explorer.py Time\Saved
echo game saved.
:END
endlocal
pause