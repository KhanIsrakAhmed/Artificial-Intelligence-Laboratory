name_dict = {
    "joseph": 3.85,
    "alex": 3.2,
    "john": 3.9,
    "jane": 3.5
}

print(name_dict["joseph"])
print(name_dict["john"])

if "jane" in name_dict:
  print("jane exists")
if "doe" in name_dict:
  print("doe exists")

name_dict["doe"] = 3.65
print(name_dict)

if "jane" in name_dict:
  print("jane exists")
if "doe" in name_dict:
  print("doe exists")

name_dict.pop("jane")
print(name_dict)

if "jane" in name_dict:
  print("jane exists")
if "doe" in name_dict:
  print("doe exists")
