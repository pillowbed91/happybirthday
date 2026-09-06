import streamlit as st
import time

# 1. 페이지 기본 설정 (밝은 생일 테마 모드)
st.set_page_config(
    page_title="Happy 50th Birthday Mom! 🎉",
    page_icon="🎂",
    layout="centered"
)

# 2. 커스텀 CSS (밝은 파스텔톤 테마 & 편지 봉투 스타일링)
st.markdown("""
    <style>
    /* 전체 배경을 밝은 분홍/크림톤으로 설정 */
    .stApp {
        background-color: #FFF5F5;
    }
    
    /* 타이틀 및 텍스트 중앙 정렬 & 색상 설정 */
    .main-title {
        text-align: center;
        color: #D9381E;
        font-family: 'Arial', sans-serif;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    
    /* 편지 상자 디자인 */
    .letter-box {
        background-color: #FFFFFF;
        border: 2px solid #FFD1DC;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        color: #333333;
        font-size: 1.1rem;
        line-height: 1.8;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Session State 초기화 (인증 상태 및 편지 열림 상태)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

# ---------------------------------------------------------
# [화면 1] 비밀번호 인증 전 화면
# ---------------------------------------------------------
if not st.session_state.authenticated:
    st.markdown("<h1 class='main-title'>🎉 Happy Birthday! 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>엄마의 50번째 생일을 축하합니다!</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("🔒 비밀번호 인증")
    
    # 비밀번호 입력 폼 (힌트 및 예시 placeholder 설정)
    password_input = st.text_input(
        label="비밀번호를 입력하세요 (힌트: koo's bd)",
        placeholder="0000.00.00",
        type="password"
    )
    
    if st.button("확인", use_container_width=True):
        if password_input == "1976.09.04":
            st.session_state.authenticated = True
            st.success("인증에 성공했습니다!")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("비밀번호가 올바르지 않습니다. 다시 시도해주세요.")

# ---------------------------------------------------------
# [화면 2] 비밀번호 인증 후 (편지 봉투 & 편지 공개 화면)
# ---------------------------------------------------------
else:
    # 축하 꽃가루 효과 실행
    st.balloons()
    
    st.markdown("<h1 class='main-title'>💌 Happy 50th Birthday!</h1>", unsafe_allow_html=True)
    st.write("")

    # 편지 봉투 인터랙션 버튼
    if not st.session_state.letter_open:
        st.info("👇 아래 편지 봉투를 눌러 편지를 열어보세요!")
        if st.button("✉️ [편지 봉투 열기]", use_container_width=True):
            st.session_state.letter_open = True
            st.rerun()
    else:
        # 작성해주신 편지 내용 출력
        letter_content = """Dear 엄마. Happy 50th's birthday. 

I can't believe that your already half a century old. But on the bright side, you look like your in your mid 40's. 

Anyway, I'm sorry for not writing you a letter sooner. And also not doing anything on your birthday. But I will make it up to you by getting good grades on my midterm. I'm also sorry my first semester grades. 

I also thank you everyday(even thought I don't really say it) for giving me such a good opportunity and environment to study. And also for you believing in me. 

I hope you had a great 50th's birthday and age well and not get sick as often. 

Thanks and happy birthday! 

-Daniel-"""

        st.markdown(f"""
            <div class='letter-box'>
                {letter_content.replace('\n', '<br>')}
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("✉️ 편지 접기", use_container_width=True):
            st.session_state.letter_open = False
            st.rerun()
