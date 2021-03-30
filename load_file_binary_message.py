with open("input.txt","r") as entrance:
    entrance_contents = entrance.read()
    entrance_contents.replace(" ", "")
    number_of_all_objects = len(entrance_contents)/8
    
result=0
result1=0

for i in range(0,int(number_of_all_objects)):
    if entrance_contents[i*8:(i*8)+8] == "00000000":
        result += 1
    elif entrance_contents[i*8+3] != entrance_contents[i*8+7]:
        result += 1
    else:
         result1 = entrance_contents[i:i+8] + str(result1)


with open("output.txt","w") as departure:
    departure.write("Number of all loaded objects: {} \nNumber of objects with error: {} \nAll objects which has no error: {}".format(number_of_all_objects,result,result1))
