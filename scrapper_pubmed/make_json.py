import json

year_json = {}
year_json["year"] = 2015
year_json["count_articles"] = 65

mesh_titles = {}

mesh_titles["a"] = 32
mesh_titles["b"] = 45

year_json["mesh_titles"] = mesh_titles

print(json.dumps(year_json, indent=4))

'''
{
  "year":"1990",
  "count_articles":"65",
  "mesh_titles":[
    {"jdshja/fhdsj": "21"},
    {"3212": "32"}
  ],
  "chemicals":[
    {"jdshja": "21"},
    {"3212": "32"}
  ]
}
'''