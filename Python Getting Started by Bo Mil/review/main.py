#  import inheritance

# james = inheritance.HighSchoolStudent("james")
# print(james.get_name_capitalize())

from inheritance import HighSchoolStudent #Use * if wanting to import everything from that file

james = HighSchoolStudent("james")
print(james.get_name_capitalize())