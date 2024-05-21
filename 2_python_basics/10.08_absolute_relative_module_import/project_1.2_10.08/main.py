from mymodule.subpackage.module2 import welcome

def main():
    welcome()
    
if __name__== "__main__": # will be executed only because this, if importing main.py as module into another Python script, the "main()" func. would not executed automatically.
    main()   

