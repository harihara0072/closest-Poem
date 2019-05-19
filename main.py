
#Importing libraries 
import re
import math


#Asking for the file name from the user
file_name = input("Give the name of the poetry file: ")

#Function that calculates the cosine distance 
def Calculate_Cosine_distance(file_poem, user_poem):
    
    #Lists where the vector will be saved
    poem = []
    user =[]
    
    #Geting the keys of both poems and combining them and using set function to get the unique keys
    poem_keys = list(file_poem.keys())
    user_keys = list(user_poem.keys())
    total_keys = list(set(poem_keys + user_keys))
    total_keys.sort()
    
    #Appending the vector list in order for both the poems using the keys in total keys
    for key in total_keys:
        poem.append(file_poem.get(key, 0))
        user.append(user_poem.get(key, 0))
    
    a = 0
    b = 0
    c = 0
    
    #Calculating the numerator and denominator values of the cosine formulae
    for i in range(0, len(poem)):
        a += poem[i] * user[i]
        b += poem[i]**2
        c += user[i]**2
    
    
    #Using the math library to get the square root of the terms in denominator
    b = math.sqrt(b)
    c = math.sqrt(c)
    
    distance = a /(b * c)
    
    #Returning the cosine distance
    #print(distance)
    
    print(file_poem, user_poem)
    return distance

try:
    
    #Trying to open and read the file
    file = open(file_name)
    file_data = file.readlines()
    
    #Asking the poem from the user
    user_data = input("Input your poem delineated by ''/'' for each line: ")
    
    #Dictionories to save the words and their count
    user_dict ={}
    poems = {}
    distance = {}
    
    #Spliting the lines in each poem
    user_data = user_data.replace("/", " ")
    user_data = user_data.split()
    
    #Calculating the words and count for each poem
    for word in user_data:
        if word in user_dict:
            user_dict[word] += 1
        else:
            user_dict[word] = 1
    
    for poem in file_data:
        poem_dict ={}
        poem = poem.rstrip("\n")
        poem = poem.replace("/", " ")
        
        #Geting the poet name and the poem
        poet, poem = poem.split(":")[0], poem.split(":")[1]
        poem = poem.split()
        
        #Using regular expression to remove the punctuation
        for word1 in poem:
            word = re.findall('[a-zA-Z]+', word1)[0]
            if word in poem_dict:
                poem_dict[word] += 1
            else:
                poem_dict[word] = 1
                
            #Calling the function to calculate the distance
            distance[poet] = Calculate_Cosine_distance(poem_dict, user_dict)
        
    #Geting the name and the poem of the closest poem to the user poem
    d_keys = list(distance.keys())
    d_val = list(distance.values())
    file.close()
    file = open(file_name)
    file_data = file.readlines()
    close_poet = d_keys[d_val.index(max(d_val))]
    for poem in file_data:
        if close_poet in poem:
            close_poem = poem.split(":")[1]
    
    
    
    #Printing the poet name and the poem
    print(f"The poem is closest to: \n {close_poet} : {close_poem}")
        
#Wrong file name exception handiling.   
except:
    print("Enter valid file name")
