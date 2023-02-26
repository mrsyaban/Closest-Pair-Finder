from IO import IO

if __name__ == "__main__":
    exit : bool = False
    User = IO()

    User.landing()
    while not exit :
        User.set_number()
        User.set_dimensi()
        
