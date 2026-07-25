print("=== 파이썬 간이 단어장 ===")

dictionary = {
    "apple": "사과",
    "banana": "바나나",
    "cherry": "체리"
}

dictionary["dragonfruit"] = "용과"

#검색 기능
search_word = input("뜻을 찾을 영단어를 입력하세요:").lower()

if search_word in dictionary:
    meaning = dictionary[search_word]
    print(f" '{search_word}'의 뜻 : {meaning}")
else:
    print(f"{search_word}는 단어장에 없는 단어입니다.")    
    