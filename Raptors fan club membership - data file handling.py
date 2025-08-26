# Data file Handling project in Python

# Question: Your local university's Raptors fan club maintains a register of its active members on a .txt document.
# Every month they update the file by removing the members who are not active. 
# You have been tasked with automating this with your Python skills.
#
# Given the file currentMem, remove each member with a 'no' in their Active column. 
# Keep track of each of the removed members and append them to the exMem file. 
# Make sure that the format of the original files is preserved. 
# (Hint: Do this by reading/writing whole lines and ensuring the header remains.)
#
# Run the code block below prior to starting the exercise. 
# The skeleton code has been provided for you. 
# Edit only the cleanFiles function.


from random import randint as rnd

memReg = '/members.txt'
exReg = '/inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


def cleanFiles(currentMem, exMem):
   # Open both files
    with open(currentMem, 'r+') as currFile, open(exMem, 'a+') as exFile:
        # Read all lines
        lines = currFile.readlines()
        
        # Header stays at the top
        header = lines[0]
        members = lines[1:]
        
        # Separate active and inactive
        active_members = []
        inactive_members = []
        
        for member in members:
            if 'no' in member:  # inactive member
                inactive_members.append(member)
            else:
                active_members.append(member)
        
        # Go back and rewrite currentMem (header + active)
        currFile.seek(0)
        currFile.write(header)
        currFile.writelines(active_members)
        currFile.truncate()  # remove leftover old content if any
        
        # Append inactive members to exMem
        exFile.writelines(inactive_members)


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

# test case: run it to test your implementation of cleanFiles.
testWrite = "/testWrite.txt"
testAppend = "/testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    


