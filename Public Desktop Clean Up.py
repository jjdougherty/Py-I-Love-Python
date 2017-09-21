#Joseph Dougherty
#9/21/07
#Desktop Central spits shortcuts that users cant kill on their public during updates.
# After this runs all short cut files will be removed from the Public Desktop!

import os #import used for navigation



os.chdir('c:/users/public/desktop') #CD [DESTINATION]

x = os.listdir(os.curdir) #listdir [Folder To List Objects From (os.curdir gets current dir)]


for i in x:     #For Each object on desktop 
    if ".lnk" in i:   #if file has type ".lnk"(short cut)
        os.remove(i)  #Remove .lnk file 