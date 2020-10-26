import json
para1 = {"b":"Nexus", "c":"cisco","a":"15.5"}
#print(para1)
#print(type(para1))

para2=json.dumps(para1,sort_keys=True,indent=4, separators=("," ,":")) #排序,换行加缩进,压缩
print(para2)
print(type(para2))