# Simple script to delete BLANK_#.pdf files
import os

def removePrePdfs():
    num = input("Enter the last blank file num (blank#.pdf) : ")
    for n in range(int(num)):
        n=n+1
        
        #delFile = "blank" + str(n) + ".pdf" # use this for blank files
        delFile = "Slide" + str(n) + ".pdf" # use this for Slide files
        print("deleted ", delFile)
        os.remove(delFile) # Danger zone

    print("\n", n , " files deleted")

removePrePdfs()