

def write_to_database(file_name, object):
  with open(file_name, "ab+") as pickle_file:
    pickle.dump(object, pickle_file)

def retrieve_from_database(file_name):
  with open(file_name, "rb+") as pickle_file:
    deserialized_data = []
    while True:
      try:
        deserialized_data.append(pickle.load(pickle_file))
      except FileNotFoundError:
        print("i'm a duck")
      except EOFError:
        break

    return deserialized_data
