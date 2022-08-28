# FindFile

This program will search your pc full directory (other than folders that it doesnt have 
permission to enter), for a specific file that youve typed (The name and the ext). 

HOW_DOES_IT_WORK
The way in which it works is mainly recursion. Is lists the current directory that its in,
it the loops through this list, checks if its a folder or not, if it is, then it will repeat
this by calling the function again. If it is not a folder, it will check to see if that file
name is the same as the one written by the user. If so, it prints out the directory, else, 
it loops back round through the loop.
