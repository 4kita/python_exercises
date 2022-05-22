number_of_cats = 100
cats = [False] * number_of_cats

print(cats)

round = 1
cat_number = 0

while round <= 100:
    while cat_number < 100:
       cats[cat_number] = not cats[cat_number]
       cat_number = cat_number + round    
    cat_number = 0
    round = round + 1

print(cats)