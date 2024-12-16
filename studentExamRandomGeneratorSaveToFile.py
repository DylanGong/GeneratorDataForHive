import random


# 数据样本
names = [
    "Andy", "Jerome", "Delia", "Ben", "Carter", "Vivian", "Alice", "David",
    "Emma", "Jack", "Grace", "Olivia", "Ethan", "Sophia", "Liam", "Charlotte",
    "Noah", "Isabella", "James", "Ava", "Lucas", "Mia", "Henry", "Ella"
]
universities = [
    "Peking University",       # 北京大学
    "Tsinghua University",     # 清华大学
    "Fudan University",        # 复旦大学
    "Wuhan University",        # 武汉大学
    "Nanjing University",      # 南京大学
    "Nankai University",       # 南开大学
    "Tianjin University",      # 天津大学
    "Shanghai Jiao Tong University",  # 上海交通大学
    "Zhejiang University",     # 浙江大学
    "Sun Yat-sen University",  # 中山大学
    "Xiamen University",       # 厦门大学
    "Sichuan University",      # 四川大学
    "Shandong University",     # 山东大学
    "Beihang University",      # 北京航空航天大学
    "Xi'an Jiaotong University", # 西安交通大学
    "Harbin Institute of Technology", # 哈尔滨工业大学
    "East China Normal University",   # 华东师范大学
    "Northeastern University",        # 东北大学
    "Central South University"        # 中南大学
]
subjects = {
    "Science": ["Chemistry", "Physics", "Biology"],
    "Humanities": ["History", "Politics", "Geography"]
}


def generate_university_list():
    """随机生成一个包含3所大学的组合"""
    return "-".join(random.sample(universities, random.randint(2, 4)))


def generate_subject_scores(subject_list):
    """为给定的学科生成随机成绩"""
    return "-".join([f"{subject}:{random.randint(70, 100)}" for subject in subject_list])


def generate_random_scores():
    """生成随机分数列表"""
    return "-".join([str(random.randint(90, 150)) for _ in range(3)])


def generate_data_line():
    """生成一行数据"""
    name = random.choice(names)
    university_list = generate_university_list()
    if random.random() > 0.5:
        subject_scores = generate_subject_scores(subjects["Science"])
    else:
        subject_scores = generate_subject_scores(subjects["Humanities"])
    random_scores = generate_random_scores()
    return f"{name},{university_list},{subject_scores},{random_scores}"


def generate_data_file(filename, num_lines=10):
    """生成数据文件"""
    with open(filename, "w", encoding="utf-8") as file:
        for _ in range(num_lines-1):
            line = generate_data_line()
            file.write(line + "\n")
        file.write(generate_data_line())


if __name__ == "__main__":
    # 生成数据文件
    generate_data_file("student_examination_data.txt", num_lines=10)
    print("数据文件已生成：student_examination_data.txt")
