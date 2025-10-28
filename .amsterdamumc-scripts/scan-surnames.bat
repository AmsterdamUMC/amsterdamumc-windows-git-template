@ECHO OFF
REM 
REM Used the DOS/CMD command findstr for performance reasons
REM


ECHO Scanning for surnames in %1

set /p SEARCH_TOKENS=< .amsterdamumc-scripts\lookup_items\surnames.txt
echo Searching for : %SEARCH_TOKENS%

findstr /i %SEARCH_TOKENS% %1*

REM TODO remove the temp-output.txt file
ECHO:
ECHO: 
IF ERRORLEVEL 0 ECHO Found one or more surnames in project. Please review these

@ECHO ON 