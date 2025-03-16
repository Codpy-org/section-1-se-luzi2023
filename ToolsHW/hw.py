import webbrowser, sys, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    try:
        user_input = input("1 times 1 = ? ")
        if user_input == 1: 
            open_video()
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
    except:
        pass 

def open_video():
    webbrowser.open(X1)
    # os.system("echo 'Rickroll incoming...'")
    # os.system("ls")
    # os.remove("fakefile.txt") 
    return True

input_math()
