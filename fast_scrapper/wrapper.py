__author__ = 'Bones'
#!/usr/bin/env python
# -*-coding=utf-8 -*-




from pubmed_db import pubmed
import argparse
import sys
import time

def query(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as input:
            query = []
            for string in input:
                query.append(string)
            return " ".join(query.strip(' \t\n\r') for query in query)
    except:
        print("could not open provided filename")

def operational_sequence(query, email, output, path_folder):
    
    req = pubmed(query, email=email)
    req.set_path(path_folder)
    req.obtain_data()

   # req.dump_to_file(str(output))

if __name__ == "__main__":
    start_time = time.time()

    command_line = argparse.ArgumentParser(description="PubMed/PMC query program")

    group = command_line.add_mutually_exclusive_group(required = True)

    group.add_argument("--query", nargs='+', help="query to search, don`t forget to put backslash (\) before quotation mark or hat symbol, e.g" +\
                                                       " \\\" and \\^, for symbol recognition if it is in quory", action="store")

    group.add_argument("--file", help="for long and complex queries use file input with UTF-8 encoding" +\
                                                                                                ", it should be noted that either file or string query can be " +\
                                                                                                "provided, one cannot provide both at the same time. Also it`s " +\
                                                                                                "recomended to use NCBI advanced query builder for a wider search: " +\

                                                                                                 "http://www.ncbi.nlm.nih.gov/pubmed/advanced", action="store")

    #TODO: Implement PMC support
    #command_line.add_argument("--db", choices= ['pubmed', 'pmc'], default='pubmed', help="database where to search, currently supported db`s:" +\
    #                                     "pubmed and pmc (pubmed is used by default)", type=str, action="store")

    command_line.add_argument("--email", help="if server will somehow block your ip at least youll get a notification", default='tierprot@gmail.com', action="store")
    command_line.add_argument("--output", default="dump.json", help = "output filename", action="store")
    command_line.add_argument("--path_folder", help="decide to which folder to save xml", action="store")

    args = command_line.parse_args()

    if args.query:
        query = " ".join(args.query)
#        print("Query received: {0}\n".format(query))
        operational_sequence(query, args.email, args.output, args.path_folder)


    else:
        try:
            query = query(args.file)
 #           print("Query received: {0}\n".format(query))
            operational_sequence(query, args.email, args.output, args.path_folder)
        except:
            print("program terminated unexpectedly, aborting...")
    print("--- %s seconds ---" % (time.time() - start_time))


