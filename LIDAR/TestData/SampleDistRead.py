#This is how we can pretend the .txt files are LIDAR readings

from numpy import array

#This function will read the text files generated by "GenerateSampleDist.py" and put them in a 
# numpy array as if they had just been read from the LIDAR

def getFakeData(fileName):

    rocks = []
    elements = []

    with open(fileName, 'r') as file:

        for line in file:

            elements = line.split(",")

            #angles and dist

            rocks.append(float(elements[0]), float(elements[1]))

    return array(rocks)     #turn into a numpy array before return

#Editted by Chris Sherman 6:25pm 1/3/19