# 한글 2020 및 2022 제품키 자동 입력

* 한글 2020 및 2022 설치 시 제품키 입력을 자동화하기 위한 PIDKEY to ECDATA 변환 스크립트입니다.
* 변환된 ECDATA 키는 Install\InstallerConfig.ini의 [Install] 섹션에 ECDATA=XXXXXXXXXXXXXXX 포맷으로 저장합니다.

## Convert to EXE

* `pyinstaller --onefile --icon=favicon.ico --name HWP-KEY-CONVERTER.exe main.py`
