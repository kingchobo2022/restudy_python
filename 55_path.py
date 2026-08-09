import os
from pathlib import Path

# folder_path = "data_logs"

# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
#     print(f"[{folder_path}] 디렉토리를 생성했습니다.")

dir_path = Path("data_logs")
dir_path.mkdir(parents=True, exist_ok=True)

file_path = dir_path / "user_data.csv"
print(f"체크된 파일 경로 : {file_path}")

