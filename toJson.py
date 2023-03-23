import json


# write data to json file
def addData(data, destination):
    with open(destination, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# if __name__ == "__main__": obj = encryptDecrypt() datas = {'ID': {'Key': obj.getKey(), 'Book': {'Book1': 0,
# 'Book2': 1, 'Book3': 1}, 'E-Book': {'eBook1': 0, 'eBook2': 1, 'eBook3': 1} }}
#
#     update = toJson()
#     update.setData(datas)
#     update.addData()
