import os 
if(not os.path.exists("Data")) :
    os.mkdir("Data")

for i in range(0,100) :
    os.mkdir(f"data/Day{i+1}") ## Create Folders or Directory

# for i in range(0,100) :
#     os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}") ## Rename The Folders
