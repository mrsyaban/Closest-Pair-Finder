from IO import IO

if __name__ == "__main__":
    exit : bool = False
    
    IO.landing(IO)
    User = IO()
    while not exit :
        if User.mode == 0 :
            exit = True
        if User.mode == 1:
            User.set_number()
            User.set_dimensi()
            User.printResult()
            User.ask_next()
        if User.mode == 2:
            User.visual()
            User.ask_next()
