import pandas as pd
import pypyodbc 
import sys


if len(sys.argv) >= 4:
    print("\n")

    dbServer = sys.argv[1]
    database = sys.argv[2]
    sqlScript = sys.argv[3]

    print('Connecting to SQL Server... \n')

    # Connect to SQL Server
    conn = pypyodbc.connect('Driver={SQL Server};'
                        f'Server={dbServer};'
                        f'Database={database};'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    sqlCommand = ''

    print('Reading the file... \n')

    # reading .sql file 
    with open(sqlScript, mode='r', encoding='utf-16-le') as f2:
        
        print("Adding data to connected database:")
        
        for inDx, line in enumerate(f2):

            if "IDENTITY_INSERT" in line and "ON" in line:
                cursor.execute(line)
                conn.commit()
            elif "IDENTITY_INSERT" in line and "OFF" in line:
                cursor.execute(line)
                conn.commit()
            else:
                if "GO" not in line:
                    # If INSERT is in line then execute prior 
                    # sql command and replace it with the new line.
                    # This is done to ensure the commands are full
                    # and not cut in half.
                    if "INSERT" in line:  
                        print(inDx, end = "\r")
                        try:
                            cursor.execute(sqlCommand.replace('\n', ' '))
                            conn.commit()
                        except BaseException as sqlError:
                            print('\n')
                            print(sqlError)
                            print('\nSQL command that coused the error:')
                            print(sqlCommand)
                            break
                        sqlCommand = line 
                    else:
                        sqlCommand = sqlCommand + line            
        print('\nFinished. \n')
else:
    print("\n")
    print("Parameter missing. \n")
    # print("Enter paramenters in this order: DatabaseServer DatabaseName PathAndNameOfSQLScript")
    print("Example: python runSQLScript.py \"DatabaseServer\" \"DatabaseName\" \"C:/Path/To/script.sql\" \n")