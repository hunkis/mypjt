import streamlit as st
import pandas as pd

#텍스트 출력
st.title('')
st.header('st.header()에 대한 첫번째 내용입니다.')
st.subheader('1.이것은 첫번째 st.subheader()입니다.')
st.write('asdas')
st.text('asdasd')


## 1. 서버접속 (접속용 터미널)
# cloud-sql-proxy.exe slidigital:us-central1:slidigital

## 2. 원래 터미널
# set GOOGLE_CLOUD_PROJECT=slidigital
# set USE_CLOUD_SQL_AUTH_PROXY=true

## 3. django설정
# python manage.py makemigrations
# python manage.py makemigrations polls
# python manage.py migrate
# python manage.py collectstatic

## 4. 웹서버 실행
# python manage.py runserver 8080

## 5. 앱 배포
# gcloud app deploy

## 6. 배포 앱 실행
# gcloud app browse

## sql 서버 로그인 (x)
# gcloud auth application-default login

## django 업데이트  
# python manage.py makemigrations polls
# python manage.py migrate

## django db테이블 마이그
# python manage.py sqlmigrate polls 0001

## user id/pass : slidigital