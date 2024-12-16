import random
import numpy as np


# 分隔符
DELIMITERS = [" ", "\t", ",", ";",":"]
MULTI_DELIMITERS = ["::", "||"]
# 随机生成姓名
# 姓氏库
surnames = [
    "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈",
    "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许",
    "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏",
    "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章",
    "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦",
    "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳",
    "酆", "鲍", "史", "唐", "费", "廉", "岑", "薛", "雷", "贺",
    "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常",
    "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余",
    "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹"
]

# 男性名字库
male_names = [
    "伟", "强", "磊", "涛", "斌", "峰", "杰", "超", "军", "勇",
    "帅", "洋", "浩", "宇", "凯", "健", "帆", "飞", "松", "昊",
    "楠", "晨", "辰", "坤", "霖", "航", "兵", "凡", "俊", "威",
    "春", "翔", "哲", "皓", "梓", "钧", "程", "煜", "希", "晗"
]

# 女性名字库
female_names = [
    "燕", "梅", "秀英", "婷", "桂英", "丽", "英", "华", "玲", "芳",
    "萍", "珍", "颖", "红", "玉", "冰", "琳", "云", "莉", "美",
    "蓉", "静", "秀兰", "淑珍", "秀荣", "丹", "艳", "霞", "秀华", "桂兰"
]


def get_random_gender():
    """随机生成性别"""
    return "M" if random.randint(0, 1) == 0 else "F"


def get_random_chinese_name(gender=None):
    """
    随机生成中文姓名
    :param gender: 性别 ('M' 表示男性, 'F' 表示女性, None 随机生成性别)
    :return: 随机生成的姓名
    """
    if gender is None:
        gender = get_random_gender()
    surname = random.choice(surnames)
    if gender == "M":
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)
    return surname + first_name

def generate_student_id():
    """生成8位随机学号"""
    return "20"+"".join(random.choices("0123456789", k=6))


# def generate_name():
#     """从姓名库中随机选择姓名"""
#     return random.choice(NAMES)


def generate_gender():
    """随机生成性别"""
    gender = random.choice(["男", "女"])
    return gender


def generate_age():
    """随机生成年龄"""
    return random.randint(18, 25)


def generate_score(mean=80, stddev=10):
    """生成符合正态分布的成绩，范围在40-100"""
    while True:
        score = int(np.random.normal(mean, stddev))
        if 40 <= score <= 100:
            return score


def generate_student_info(student_ids, delimiter):
    """生成学生信息数据"""
    data = []
    for student_id in student_ids:
        # name = generate_name()
        gender = generate_gender()
        name = get_random_chinese_name(gender)
        age = generate_age()
        data.append(delimiter.join([student_id, name, gender, str(age)]))
    return data


def generate_student_scores(student_ids, delimiter):
    """生成学生成绩数据"""
    data = []
    for student_id in student_ids:
        mysql_score = generate_score()
        dwh_score = generate_score()
        spark_score = generate_score()
        data.append(delimiter.join([student_id, str(mysql_score), str(dwh_score), str(spark_score)]))
    return data


def write_to_file(file_name, data):
    """写数据到文件"""
    with open(file_name, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")


def main():
    # 生成100个学生的学号
    student_ids = [generate_student_id() for _ in range(100)]

    # 随机选择分隔符
    delimiter_info = random.choice(MULTI_DELIMITERS)
    delimiter_scores = random.choice(DELIMITERS)

    # 生成学生信息和成绩数据
    student_info_data = generate_student_info(student_ids, delimiter_info)
    random.shuffle(student_ids)  # 打乱学号顺序
    student_scores_data = generate_student_scores(student_ids, delimiter_scores)

    # 写入文件
    write_to_file("student_info.txt", student_info_data)
    write_to_file("student_scores.txt", student_scores_data)

    print("文件生成完毕！")

if __name__ == "__main__":
    main()
