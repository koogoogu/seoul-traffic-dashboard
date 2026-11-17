import streamlit as st

st.set_page_config(
    page_title="SEOUL TRAFFIC",
    page_icon="seoul traffic.jpg",
    layout="wide"
)

col1, col2 = st.columns([1, 5])
with col1:
    st.image("seoul traffic.jpg", width=140)
with col2:
    st.title("SEOUL TRAFFIC")
    st.subheader("서울시 주요 명소 실시간 혼잡도 및 대중교통 연관성 분석 플랫폼")

st.divider()
st.info("서울시 실시간 도시데이터 API를 연동하여 관광지·축제 혼잡도와 지하철·버스 이용 현황을 시각화하는 대시보드입니다.")
