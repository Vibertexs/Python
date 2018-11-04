student = {
    "name": "Mark",
    "student_id" : 15163,
    "feedback" : None

}
student["last_name"] = "KOVA"
try: 
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding that")
except TypeError:
    print("Can't add intigers and a string together")
except Exception as error:
    print("unknown error")
    print(error)

print("This code executes!")
print("This code executes!")

