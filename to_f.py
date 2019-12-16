import os
import glob
list = os.listdir("G:\Code_School/python/Test/htdocs/test/images") # dir is your directory path
number_files = len(list)
print(number_files)

total_files=number_files
current_files=0    

while 1:
    list = os.listdir("G:\Code_School/python/Test/htdocs/test/images") # dir is your directory path
    number_files = len(list)
    #print(number_files)


    list_of_files = glob.glob('G:\Code_School/python/Test/htdocs/test/images\*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    #print(latest_file)
    
    total_files=number_files
    

    def DetectFruit():
        os.popen('python C:\\tensorflow1\\models\\research\\object_detection\\own_detection_image.py '+latest_file,"r")


    if total_files!=current_files:
        DetectFruit()
        print("ok")
        current_files=total_files

