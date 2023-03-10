from database_reader import DatabaseReader

read_from_db = DatabaseReader()

result = read_from_db.get_all_referee()

for i in result:
    print(i)
