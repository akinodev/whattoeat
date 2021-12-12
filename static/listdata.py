import os
import json

# 读取 foods 文件夹下的所有文件，并将其名称和路径存入字典中


def get_foods():
    foods = {}
    foods["list"] = []
    for file in os.listdir('static/foods'):
        foods["list"].append(".".join(file.split('.')[:-1]))
        foods[".".join(file.split('.')[:-1])] = 'static/foods/' + file
    return foods

# 读取 shops/meituan 和 shops/ele 文件夹下的所有文件，并将其名称和路径存入字典中


def get_shops():
    shops = {}
    shops['meituan'] = []
    shops['ele'] = []
    shops["detail"] = {}
    shops["detail"]["meituan"] = {}
    shops["detail"]["ele"] = {}
    for file in os.listdir('static/shops/meituan'):
        shops["meituan"].append(".".join(file.split('.')[:-1]))
        shops["detail"]["meituan"][".".join(file.split(
            '.')[:-1])] = 'static/shops/meituan/' + file
    for file in os.listdir('static/shops/ele'):
        shops["ele"].append(".".join(file.split('.')[:-1]))
        shops["detail"]["ele"][".".join(file.split(
            '.')[:-1])] = 'static/shops/ele/' + file
    return shops


def main():
    foods = get_foods()
    shops = get_shops()
    jsonfile = {"foods": foods, "shops": shops}
    with open('static/listdata.json', 'w', encoding="utf-8") as f:
        json.dump(jsonfile, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
    print("listdata.json 已生成")
