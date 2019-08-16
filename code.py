import os # needed for deleting notes

# In case of adding a graphical interface, PySimpleGUI and Kivy are recommended

# ‘r’ – Read mode which is used when the file is only being read 
# ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
# ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
# ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file

def create():
    #print("create")
    d = input("What's the note?")
    n = input("What do you want to call it? ") + ".txt"
    
    f = open(n, "w")
    f.write(d)
    
    f.close()

def read():
    #print("read")
    n = input("What's the name of the note? ") + ".txt"
    f = open(n, "r")
    print("Here is the note: ")
    print("- " + f.read())
    print(" ")
    f.close()

def delete():
    #print("read")
    n = input("What's the name of the note? ") + ".txt"
    print("Are you sure you want to delete the note " + n + "?")
    print("1 = yes")
    print("2 = no")
    a = int(input())
    if(a == 1):
        os.remove(n)
    else:
        main()
        

def main():
    while True:
        print("What do you want to do? ")
        print("1 = create a note, ")
        print("2 = read a note")
        print("3 = delete a note")
        print("4 = quit")
        a = int(input())

        if(a == 1):
            create()
        elif(a == 2):
            read()
        elif(a == 3):
            delete()
        elif(a == 4):
            break
            break
        else:
            print("Invalid input")
            continue


main()





