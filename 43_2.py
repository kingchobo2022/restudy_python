def print_user_info(**kwargs):
    
    for key, value in kwargs.items():
        print(f"- {key}: {value}")


#print_user_info(name="이영희", age=25, city="인천")        

di1 = {"name":"이영희", "age":25, "city":"인천"}
print_user_info(**di1)        
di2 = {"name":"김철수", "age":22}
print_user_info(**di2)        



