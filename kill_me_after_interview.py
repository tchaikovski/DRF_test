my_list_to_interview = [
    {'id': 1, "name": "simple"},
    {'id': 2, "name": "simple"},
    {'id': 3, "name": "simple3"},
    {'id': 4, "name": "simple"}
]

# for name in x:
#     if name['id'] == 3:ye
#         print(name["name"])
# name3 = [(i['name'] if i['id'] == 3) for i in my_list_to_interview]

region = list(filter(lambda r: r["id"] == 3, my_list_to_interview))[0]["name"]
# print(region)

region2 = [i['name'] for i in my_list_to_interview if i['id'] == 3][0]

print(region)
stop = ''