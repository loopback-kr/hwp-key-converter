# 한글 2020, 2022 및 2024 제품키 자동 입력

* 한글 2020, 2022 및 2024 설치 시 제품키 입력을 자동화하기 위한 PIDKEY to ECDATA 변환 스크립트입니다.
* 변환된 ECDATA 키는 Install\InstallerConfig.ini의 [Install] 섹션에 ECDATA=XXXXXXXXXXXXXXX 포맷으로 저장합니다.

## Download

[HWP-KEY-CONVERTER.exe](https://github.com/loopback-kr/hwp-key-converter/blob/master/HWP-KEY-CONVERTER.exe)

## Convert to EXE

* `pyinstaller --onefile --icon=favicon.ico --name HWP-KEY-CONVERTER.exe main.py`
