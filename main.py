import os
if __name__=='__main__':
    print("Welcome to Robot_Speaker created by fahim")
    print("If you want to quit then type quit!")
    while True:
        x=input("Enter what you want to speak: ")
        if x=="quit":
               os.system("say 'see you later!'")
               break
        command=f"say {x}"
        os.system(command)
