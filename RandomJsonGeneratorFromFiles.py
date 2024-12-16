import random
import json

"""
实现从文件中读取数据，随机生成JSON文件，并以JSON格式存储在记事本中
"""
def load_city_data(file_path):
    """从文件加载城市、街道、邮政编码数据"""
    city_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # 跳过空行和注释
            city, street, postal_code = line.split(",")
            if city not in city_data:
                city_data[city] = []
            city_data[city].append({"street": street, "postal_code": int(postal_code)})
    return city_data


def load_names(file_path):
    """从文件加载姓名数据"""
    names = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # 跳过空行和注释
            name, gender = line.split(",")
            names.append(name)
    return names


def generate_random_json(city_data, name_pool):
    """生成一个随机的 JSON 数据"""
    # 随机选择 name，确保不重复
    name = random.choice(name_pool)
    name_pool.remove(name)

    # 随机生成 friends，确保不重复
    num_friends = random.randint(1, 5)  # 1 到 5 个朋友
    friends = random.sample(name_pool, num_friends)
    for friend in friends:
        name_pool.remove(friend)

    # 随机生成 students，确保不重复
    num_students = random.randint(1, 5)  # 1 到 5 个学生
    students = {}
    for _ in range(num_students):
        student_name = random.choice(name_pool)
        name_pool.remove(student_name)
        students[student_name] = random.randint(15, 24)

    # 随机选择一个城市和对应的街道、邮政编码
    city = random.choice(list(city_data.keys()))
    address_data = random.choice(city_data[city])
    address = {
        "street": address_data["street"],
        "city": city,
        "postal_code": address_data["postal_code"]
    }

    # 组装完整的 JSON 数据
    random_json = {
        "name": name,
        "friends": friends,
        "students": students,
        "address": address
    }

    return random_json


if __name__ == "__main__":
    # 文件路径
    json_data_number = 5
    city_data_file = "city-street-postcode.txt"
    name_file = "name_gender.txt"
    output_file = "output.json"
    output_fiel_txt = "output.txt"

    # 加载数据
    city_data = load_city_data(city_data_file)
    name_pool = load_names(name_file)

    # 生成 JSON 数据并保存到文件
    # result_data = []
    # for _ in range(5):  # 生成 5 个 JSON 数据
    #     random_json = generate_random_json(city_data, name_pool.copy())  # 使用副本防止重用
    #     result_data.append(random_json)

    # 将结果保存到文件
    with open(output_file, 'w', encoding='utf-8') as file:
        # json.dump(result_data, file, indent=4, ensure_ascii=False)
        for _ in range(json_data_number):  # 生成 5 个 JSON 数据
            random_json = generate_random_json(city_data, name_pool.copy())  # 使用副本防止重用
            file.write(json.dumps(random_json, ensure_ascii=False) + "\n")

    print(f"生成的 JSON 数据已保存到 {output_file}")