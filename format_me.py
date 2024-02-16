inputText = "Lorem ipsum dolor sit amet consectetuer adipiscing elit Duis pulvinar Itaque earum rerum hic tenetur a sapiente delectus ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat Duis sapien nunc commodo et interdum suscipit sollicitudin et dolor Itaque earum rerum hic tenetur a sapiente delectus ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat Mauris metus Vivamus porttitor turpis ac leo Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum Aliquam in lorem sit amet leo accumsan lacinia Sed ac dolor sit amet purus malesuada congue Nunc dapibus tortor vel mi dapibus sollicitudin Nullam eget nisl"

words = inputText.split()

counter = {}

for i in range(len(words)):
    if counter.get(words[i].lower()) == None:
        counter[words[i].lower()] = 1
    else:
        counter[words[i].lower()] += 1

print(counter)
