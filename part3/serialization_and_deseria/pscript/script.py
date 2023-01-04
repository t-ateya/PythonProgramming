import os 

def moveFileToDestination(fileName, targetDir):
    """moves a file from one location to another"""
    moveCmd = "mv " + fileName + " " +  targetDir
    print("Moving files: "+ moveCmd)
    os.system(moveCmd)


moveFileToDestination("test.txt", "../")