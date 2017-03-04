import os

for year in [2007]:
  command = "python3 wrapper.py --query "
  command += "\"(alzheimer[MeSH Terms]) AND (\"{0}\"[Date - Publication])\"".format(year)
  command += " --output \"" + str(year) + ".json\" "
  os.system(command)
