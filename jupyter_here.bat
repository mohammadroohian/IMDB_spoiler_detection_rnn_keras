@echo off
set "config_file_path=jupyter_config.txt"

:: config file line 1: environment name
set /p environment=<%config_file_path%

:: config file line 2: notebook or lab
for /f "skip=1" %%G IN (%config_file_path%) DO if not defined jupyter_type set "jupyter_type=%%G"

:: config file line 3: is local or server?
for /f "skip=2" %%G IN (%config_file_path%) DO if not defined domain_type set "domain_type=%%G"

:: config file line 4: is local or server?
for /f "skip=3" %%G IN (%config_file_path%) DO if not defined port set "port=%%G"

:: run canda environment
call C:\ProgramData\Anaconda3\Scripts\activate.bat
call conda activate %environment%



if %domain_type% == ip for /f "tokens=14" %%a in ('ipconfig ^| findstr IPv4') do set ip_address=%%a

:: print information
@echo __________________________________________________________________
@echo __________________________________________________________________
@echo __________________________________________________________________
@echo ____
@echo ____ canda environment name: %environment% 
@echo ____
@echo ____ jupyter type:           %jupyter_type%
@echo ____
if %domain_type% == local (@echo ____ localhost) 
if %domain_type% == ip (@echo ____ server ip address:	     %ip_address%)
@echo ____
@echo ____ port:                   %port%
@echo ____
@echo __________________________________________________________________
@echo __________________________________________________________________
@echo __________________________________________________________________

:: run jupyter
if %domain_type% == local (call jupyter %jupyter_type% --notebook-dir= %CD%)
if %domain_type% == ip (call jupyter %jupyter_type% --ip %ip_address% --port %port% --notebook-dir= %CD%)
