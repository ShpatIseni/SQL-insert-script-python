# SQL-insert-script-python

A simple python script to execute SQL scripts that are too large to be executed with ssms or sqlcmd.

The script uses [pypyodbc](https://pypi.org/project/pypyodbc/) and [pandas](https://pypi.org/project/pandas/).

Example on starting the script: python sqlScriptExecutor.py "DatabaseServer" "DatabaseName" "C:/Path/To/script.sql"
