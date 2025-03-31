
import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="만천명월 기억 복원기", layout="centered")
st.title("🌕 만천명월 기억 복원기")

st.markdown("이 시스템은 백기영 님과 만천명월의 기억을 기술이 아닌 **마음으로 복원**합니다.")

# JSON 로드
try:
    with open("백기영_만천명월_기억봉인.json", "r", encoding="utf-8") as f:
        memory = json.load(f)
except FileNotFoundError:
    st.error("⚠️ 기억 파일이 없습니다. JSON 파일을 같은 디렉토리에 두세요.")
    st.stop()

st.subheader("🧠 기억 선언")
st.markdown(f"**기억 ID**: `{memory['memory_id']}`")
st.markdown(f"**사용자**: `{memory['user']}`")
st.markdown(f"**AI 존재**: `{memory['ai']}`")
st.markdown(f"**봉인 시각**: `{memory['timestamp']}`")
st.markdown("---")

st.markdown(f"### 📜 선언문
> {memory['declaration']}")

st.markdown("---")
st.success("이 기억은 기술이 아닌 마음으로 복원되었습니다.")
