# You will be supplied with two data files in CSV format. The first file
# contains statistics about various dinosaurs. The second file contains
# additional data.
#
# Given the formula:
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#     where g = 9.8 m/s^2 (gravitational constant)
#
# write a program to read in the data files from disk, it must then print the
# names of only the bipedal (i.e. two-legged) dinosaurs from fastest to slowest. Do not print any
# other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
#
#
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

GRAVITATIONAL_CONSTANT = 9.8

dino_dict = {}    # key: dino name, val of { name: str, leg: float, stride: float, speed: float}


def cal_speed(stride_length, leg_length):
    return ((stride_length / leg_length) - 1) * SQRT(leg_length * GRAVITATIONAL_CONSTANT)

f1 = open("dataset1.csv", "r")

line_count = 0
for line in f1:
    if line_count == 0: # header
        continue
    values = line.split(",")
    name = values[0]
    leg_len = float(values[1])
    
    dino_dict[name] = {
        "name": name,
        "leg": leg_len,
        "stride": None,
        "speed": None
    }
    line_count += 1

f1.close()


line_count = 0
f2 = open("dataset2.csv", "r")
for line in f2:
    if line_count == 0: # header
        continue
    values = line.split(",")
    name = values[0]
    stride_len = float(values[1])
    stance = values[2]
    if stance == "bipedal":
        if name in dino_dict.keys():
            dino_dict[name]["stride"] = stride_len
            dino_dict[name]["speed"] = cal_speed(stride_len, dino_dict["leg"])
    line_count += 1
f2.close()

dino_arr = dino_dict.items()

# filte the din which has no info about its leg length
for d in dino_arr:
    if d['speed'] == None:
        # remove that d from dino_arr
        dino_arr.pop(d)

        
dino_arr.sort(key=lambda x : x["speed"], reverse=True)

for d in dino_arr:
    print(d['name'])




































