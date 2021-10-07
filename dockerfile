FROM python:3.8-slim-buster

# docker내 기본 디렉토리 경로
WORKDIR /app

# docker내 필요한 패키지 내용 복사 및 설치
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]