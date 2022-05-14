captains = {}
captains = {"Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko"}

if "Enterprise" not in captains:
   captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

for ship, captain in captains.items():
    print(f"{captain} is the captain of {ship}.")

#captains.__delitem__("Discovery")

del captains["Discovery"]

for ship, captain in captains.items():
    print(f"{captain} is the captain of {ship}.")
    


