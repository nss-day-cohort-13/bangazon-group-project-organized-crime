import sqlite3

def write_to_table(database_file, sql_commands, sql_row_values):
  with sqlite3.connect(database_file) as conn:
    c = conn.cursor()

    c.execute(sql_commands, sql_row_values)

    conn.commit()

def read_from_table(database_file, sql_commands):
  return_list = []
  with sqlite3.connect(database_file) as conn:
    c = conn.cursor()

  for row in c.execute(sql_commands):
    return_list.append(row)

  print("LIST RETURNED FROM read_from_table",return_list)
  return return_list
