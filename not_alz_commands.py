#Generates commmands for advanced search for substances, possibly related to alz desease 

file_object  = open('substances.txt', 'r')
subst_list = [i.strip('\n') for i in file_object.readlines()]
print (subst_list)
file_object.close()

valid_query = '((("2009"[Date - Publication] )) NOT alzheimer[MeSH Terms]) AND amyloid beta peptide[MeSH Terms] '

command_list = []
command = "python3 wrapper.py --query "

for year in [2007]:

    for i in range(len(subst_list)):
        command += "((\"{0}\"[Date - Publication])) NOT (alzheimer[MeSH Terms]) AND" \
                   "  \"{1}\" [MeSH Terms] ".format(year,subst_list[i])
        command += " --output \"" + str(year) + ".json\" "
        command_list.append(command)
        command = "python3 wrapper.py --query "
[print(x) for x in command_list]
