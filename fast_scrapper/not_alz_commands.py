#Generates commmands for advanced search for substances, possibly related to alz desease 
import os
import time

start_time = time.time()
file_object  = open('substances.txt', 'r')
subst_list = [i.strip('\n') for i in file_object.readlines()]
file_object.close()

command_list = []
command = "python3 wrapper.py --query "

path = "/home/max/biohack/biohack/fast_scrapper/xml/"

years = []
for year in range(1990, 2018):
  years.append(year)
#print(years)


for substance in subst_list:
  new_path = path + str(substance) + "/"
  if not os.path.exists(new_path):
    os.makedirs(new_path)
  for year in years:
    command += "\"(\"{0}\"[Date - Publication]) NOT (alzheimer[MeSH Terms]) AND" \
                 "  \"{1}\" [MeSH Terms] \"".format(year,substance)
    command += " --path_folder "
    command += "\""
    command += new_path
    command += "\""
    os.system(command)
    command = "python3 wrapper.py --query "
print("--- %s seconds ---" % (time.time() - start_time))
