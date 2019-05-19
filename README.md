# closest-Poem

The file contains names of poets and an extract of their poetry. New lines in each
poem are represented by a ‘/’. The format of a line is the following:
<Poet’s name>:<poetry delineated by ‘/’>\n
The first string in each line is the name of the author followed by a ‘:’, followed by
the poetry which is delineated by ‘/’ to represent a new line in the poem.
The next line contains the next poem and so on.
You are required to input a few lines of your own poem to the python program
(with lines separated by “/”) and compute the cosine distance (similarity score)
between each line (of poetry from the file) and your own poem. Finally your
program should display the following:
1) Each poet and the similarity score with your poem.
2) Finally display the poem that is closest to your input.

### Algorithm:

- Take the file name form the user and verify the file.
- Open the file and read the lines
- Split each line by ":" to get the poet name and the peom.
- Take the poem from the user and split the words and by using the regular expressions we remove the punctuation.
- Now we calculate the count of words and put that in a dictionary for both the poems.
- Since there may be different words in both dictionries or words may be in different order we need to get the keys of both dictionories, combine them and use the set function to get all the unique key words in a function to calulate the cosine distance.
- We need to use get method in the dictionary with a default 0 so that if the key is not there in the dictionary there will be no error.
- Then we need to apply the cosine disctance and calulate the distance and return the distance
- Print the Poem and the poet with highest cosine distance.

### Instructions to run the program:

> Run the next cell to execute the program

### Expected output:

> Give the name of the poetry file: poetry_lines.txt

> Input your poem delineated by ''/'' for each line: This is a sample program

> The poem is closest to: 
 
> William Wordsworth :  The world is too much with us; late and soon,/Getting and spending, we lay waste our powers;/Little we see in Nature that is ours;/We have given our hearts away, a sordid boon!
