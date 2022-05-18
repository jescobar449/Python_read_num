#Name: Jose Melquiades Escobar

#Define main ():
def main ():

    #Declare variables: line and counter, and initialize them
    line = 0
    counter = 0
        
    #Prompt for file name: use input function, should be num_list
    file_name = input ('Enter the name of the file: ' )

    #check for different spellings by user
    file_name_check = 'no'
    while file_name_check == 'no':
        #different spelling variations for the file nem 
        if (file_name == 'num_list') or (file_name == 'num_list.txt') or (file_name == 'num_list.text'):
            #gives the correct name if different spelling was used
            file_name = 'num_list.text'
            #sentinal is changed to proceed with the program
            file_name_check = 'yes'
        else:
            #error message for wrong file name used
            print ('Error: wrong file name was input, try again')
            #ask theuser to try again 
            file_name = input ('Enter the name of the file: ' )

        
        

    #Open the file in read mode.
    input_file = open ( file_name, 'r')

    #initialize counter to 1
    counter = 1

    #Use a while loop to read and display the first 10 lines
    while counter <= 10:
        #Read the lines in the file with readline function: ‘inline.readline()’
        line = input_file.readline()
        #Use rstrip method to remove \n characters at the end of the line
        #Print the line
        print (line.rstrip ('\n'))
        #Update the counter when the line is read
        counter += 1

    #Close file
    input_file.close ()


#End main()
main ()
