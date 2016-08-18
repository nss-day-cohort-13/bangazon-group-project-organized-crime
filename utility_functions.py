import sqlite3

def write_to_order_line_items(database_file, sql_commands, sql_row_values):
  with sqlite3.connect(database_file) as conn:
    c = conn.cursor()

    c.execute(sql_commands, sql_row_values)

    conn.commit()

def read_order_line_items(database_file, sql_commands):
  return_list = []
  with sqlite3.connect(database_file) as conn:
    c = conn.cursor()

  for row in c.execute(sql_commands):
    return_list.append(row)

  print(return_list)
  return return_list
