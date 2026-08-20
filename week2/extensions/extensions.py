file_name = input("File Name: ").lower().strip()

if "." in file_name:
    file_type = file_name.split(".")
    type = file_type[-1]
else:
    type = ""

if type == "jpg":
    type = "jpeg"


image = ["gif", "jpeg", "png"]
application = ["pdf", "zip"]
text = ["txt"]

if type in image:
    print("image/" + type)
elif type in application:
    print("application/" + type)
elif type in text:
    print("text/plain")
else:
    print("application/octet-stream")




