# from dotenv import load_dotenv
# load_dotenv()  # .env의 OPENAI_API_KEY를 환경변수로 로드
import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI

# Complete 모드 = LLM 모드 = 텍스트 완성형
# llm = OpenAI()
# result = llm.invoke("내가 좋아하는 동물은")
# print(result)

# Chat 모드 = 대화형
# chat_model = ChatOpenAI()
# result = chat_model.invoke("hi!")
# print(result.content)

# llm = ChatOpenAI(model="gpt-4o-mini")  # 원하는 모델명으로 변경 가능
# response = llm.invoke("안녕하세요, 자기소개 해주세요.")
# print(response.content)

# 인공지능 시인
chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.", "")

if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중...", show_time=True):
        result = chat_model.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)


