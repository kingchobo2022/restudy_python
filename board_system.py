#===============================================
# 전역 데이터베이스 역할
#===============================================
posts_db = []
post_id_counter = 1 # 글 번호 자동 증가용 전역 변수

# 게시글 추가 함수 (*args, **kwargs활용)
def add_post(title, content, author, *tags, **options):
    global post_id_counter, posts_db

    post = {
        "id": post_id_counter,
        "title" : title,
        "content" : content,
        "author" : author,
        "tags": list(tags), # 가변 인자 튜플을 리스트로 변환
        "views": options.get("views", 0), #옵션 미지정 시 기본 조회 수 0
        "is_public" : options.get("is_public", True) # 기본 공개
    }
    posts_db.append(post)
    post_id_counter = post_id_counter + 1
    print(f" 글 [{title}] 이(가) 정상적으로 등록되었습니다.")

# 전체 게시글 목록 출력 (enumerate, zip, any활용)    
def list_posts():
    print("\n" + "=" * 50)
    print(" 전체 게시글 목록")
    print("=" * 50)

    # 공개글만 필터링 (lambda + filter)
    public_posts = list(filter(lambda p: p["is_public"], posts_db))

    if not public_posts:
        print("등록된 게시글이 없습니다.")
        return

    # enumerate를 활용한 순번 및 포맷팅 출력
    for idx, post in enumerate(public_posts, 1):
        tag_str = " ".join([f"#{tag}" for tag in post["tags"]] if post["tags"] else "태그 없음")    
        print(f"{idx}. [{post['id']}번] {post['title']} | 작성자: {post['author']} | 조회 수: {post['views']}")
        print(f"    - 내용 : {post['content']}")
        print(f"    - 태그: {tag_str}")
        print(f"-" * 50)

def search_posts(keyword):
    print(f" [검색어: '{keyword}] 검색 결과")
    print("-" * 50)

    results = list(filter(
        lambda p: (keyword.lower() in p['title'].lower()) or (keyword.lower() in p["content"].lower() ),
        posts_db
    ))

    if not results:
        print("검색 결과 없습니다")
        return

    for p in results:
        print(f"- [{p['id']}번] {p['title']} (작성자: {p['author']})")  

def print_statistics():
    if not posts_db:
        print("통계 데이터가 없습니다.")
        return
    total_count = len(posts_db)    

    views_list = list(map(lambda p: p["views"], posts_db))  # 
    total_views = sum(views_list)
    max_view = max(views_list)
    avg_views = round(total_views / total_count, 1)

    has_viral_post = any( v >= 100 for v in views_list)

    print("\n" + "=" * 50)

    print(" 게시판 통계 분석 리포트 ")
    print("=" * 50)

    print(f" - 총 게시글 수 : {total_count} 개")
    print(f" - 누적 총 조회 수 : {total_views} 회")
    print(f" - 평균 조회 수 : {avg_views} 회")
    print(f" - 최고 조회 : {max_view} 회")
    print(f" - 인기글(조회 수 100회 이상) 보유 여부 : {'있음' if has_viral_post else '없음'}")
    print("=" * 50)
          

if __name__ == "__main__":

    add_post("파이썬 초보 탈출기1", "함수 단원까지 끝냈습니다!", "김철수", "파이썬", "공부", "기초", views=20)
    add_post("초보 탈출기2", "함수 단원까지 끝냈습니다!", "김철수", "php", "공부", "기초", views=10)
    add_post("초보 탈출기3", "함수 단원까지 끝냈습니다!", "김철수", "자바", "파이썬", "기초", views=99, is_public=False)
    add_post("파이썬 초보 탈출기4", "함수 단원까지 끝냈습니다!", "김철수", "공부", "기초", views=99)

    list_posts()
    search_posts('파이썬')
    print_statistics()


