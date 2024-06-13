import sys, time
import datetime
import math
import random
import os

group_range = {'1':[1,40,100,10],'2':[100,600,50,4],'3':[900,10000,10,10]}
path = "/home/cc/dataset/"
folder_name = "first_one"
sample_size = 4 # percent of total files in groups : for 100 files sample size = 4 means 4 sample files

mkdir_cmd = "mkdir "+path+folder_name+";"
os.system(mkdir_cmd)
for key, value in group_range.items():
    group_name = key
    low = value[0]
    high = value[1]
    n_files = value[2]
    bs = low
    n_samples = value[3]
    
    print("Group name: ",group_name," ", "Low: ", low, " ", "High: ", high, " ","number of files: ", n_files, " ", 
          "number of samples: ", n_samples)
    
    # create folder :
    cd_cmd = "cd "+path+folder_name+";"
    mkdir_cmd = "mkdir group_" + key
    temp_cmd = cd_cmd + mkdir_cmd
    os.system(temp_cmd)
    
    print("folder for group ",group_name," ", "is created.")
    
    print("Starting to create group ", group_name, " files. Please wait...")
    
    for num in range(n_files):
        #print(random.randint(low,high))
        count = int(random.randint(low,high)/bs)
        if count == 0 :
            count = 1
        cd_cmd = "cd "+path+folder_name+"/group_" + key + ";"
        
        dd_cmd = "dd if=/dev/zero of=file_"+str(group_name)+"_"+str(num)+" bs="+str(bs)+"M count="+str(count)
        main_dd = cd_cmd+dd_cmd
        
        #print(main_dd)
        os.system(main_dd)
    
    print("Files are created for group ", group_name, ".")
    
    print("Started to create SAMPLE files for group ", group_name,". number of sample folders ", n_samples)
    
    for sample in range(n_samples):  
        
        # create folder :
        cd_cmd = "cd "+path+folder_name+";"
        mkdir_cmd = "mkdir sample_"+ group_name + "_" + str(sample)
        sample_folder_cmd = cd_cmd + mkdir_cmd
        print("Folder created for sample ",sample, " in Group ",group_name)
        os.system(sample_folder_cmd)
        
        n_sample_files = int( (n_files*sample_size) / 100 )
        if n_sample_files == 0:
            n_sample_files = 1
        
        print("Number of sample files for sample ",sample, " in Group ",group_name, " is : ", n_sample_files)  
        
        
        cd_cmd = "cd "+path+folder_name+"/" + "sample_"+ group_name + "_" + str(sample)+";"
        
        print("Started creating sample files for sample ", sample, " in Group ", group_name,". Please wait ...")
        
        for s_file in range(n_sample_files):
            
            count = int(random.randint(low,high)/bs)
            if count == 0 :
                count = 1


            dd_cmd = "dd if=/dev/zero of=file_"+str(group_name)+"_"+str(s_file)+" bs="+str(bs)+"M count="+str(count)
            main_dd = cd_cmd+dd_cmd

            #print(main_dd)
            os.system(main_dd)
        
        print("finished creating sample files for sample ",sample, " in group ", group_name,".")