import pyodbc 
import sys

def run_sql_script(db_server, database, sql_script):
    # Connect to SQL Server
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                            f'Server={db_server};'
                            f'Database={database};'
                            'Trusted_Connection=yes;')
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return

    cursor = conn.cursor()
    sql_command = ""

    # Read the .sql script file line by line
    with open(sql_script, mode='r', encoding='utf-16-le') as f:
        for line in f:
            # Skip lines with the "GO" command
            if "GO" not in line:
                # If the line contains the "INSERT" command, execute the previous command and replace it with the current line
                if "INSERT" in line:
                    try:
                        cursor.execute(sql_command.replace('\n', ' '))
                        conn.commit()
                    except Exception as e:
                        print(f"Error executing command: {e}")
                        break
                    sql_command = line 
                else:
                    sql_command = sql_command + line

    print("Finished executing script.")

if __name__ == "__main__":
    # Check if there are enough command line arguments
    if len(sys.argv) >= 4:
        db_server = sys.argv[1]
        database = sys.argv[2]
        sql_script = sys.argv[3]

        run_sql_script(db_server, database, sql_script)
    else:
        print("Error: Not enough command line arguments.")
        print("Usage: python runSQLScript.py DatabaseServer DatabaseName PathAndNameOfSQLScript")
