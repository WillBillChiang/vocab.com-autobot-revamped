def readData():
    print("Reading in file...")
    try:
        credFile = open("CRED.txt", "r")
        print("Success!")
        usrpass = credFile.read().splitlines()
        return usrpass
    except IOError:
        print("Could not open file; Does it exist?")

