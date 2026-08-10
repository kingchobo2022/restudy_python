import json

user_dict = {"name":"김철수", "age": 28, "skills": ["Python", "MySQL"]}

json_str = json.dumps(user_dict, ensure_ascii=False, indent=2)
print(json_str)