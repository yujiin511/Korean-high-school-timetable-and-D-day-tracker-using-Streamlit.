import streamlit as st
import pandas as pd
import datetime

st.title('📅 시간표 & D‑Day 관리')

days = ['월','화','수','목','금']
periods = [f"{i+1}교시" for i in range(7)]
timetable = {day: ['']*7 for day in days}

for day in days:
    st.header(f"{day}요일 시간표")
    for i, p in enumerate(periods):
        timetable[day][i] = st.text_input(f"{day} {p}", key=f"{day}{p}")

st.header("⏳ D‑Day 추가하기")
dday_name = st.text_input("이름 (예: 수능)")
dday_date = st.date_input("날짜", value=datetime.date.today())
if st.button("🔖 추가"):
    delta = (dday_date - datetime.date.today()).days
    sign = "D+" if delta < 0 else "D-"
    st.success(f"✅ {dday_name} 등록됨: {sign}{abs(delta)}")

st.header("📋 내 시간표")
df = pd.DataFrame.from_dict(timetable, orient='index', columns=periods)
st.dataframe(df)

st.header("📅 등록된 D‑Day")
if 'dday_date' in locals():
    st.write(f"{dday_name}: {dday_date} → **{sign}{abs(delta)}**")
else:
    st.write("➖ 아직 등록된 D‑Day 없음")
