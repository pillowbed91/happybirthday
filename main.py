import streamlit as st
import base64
import os

# 1. 페이지 기본 설정 (넓은 레이아웃)
st.set_page_config(
    page_title="Happy 50th Birthday Mom!",
    page_icon="🎂",
    layout="wide"
)

# 이미지 인코딩 헬퍼 함수 (파일 확장자 대소문자 보완 및 로컬 이미지 안전 로딩)
def get_image_base64(file_name):
    # 실행 중인 파일 경로 기준으로 이미지 검색
    base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    file_path = os.path.join(base_dir, file_name)
    
    # 파일이 존재하지 않는 경우 대소문자 차이 등 확장자 교체 시도
    if not os.path.exists(file_path):
        name, ext = os.path.splitext(file_name)
        alt_ext = ".jpg" if ext.lower() in [".jpeg", ".jpg"] else ext
        file_path = os.path.join(base_dir, name + alt_ext)

    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            ext_type = os.path.splitext(file_path)[1].replace('.', '').lower()
            if ext_type == "jpg":
                ext_type = "jpeg"
            return f"data:image/{ext_type};base64,{base64.b64encode(f.read()).decode()}"
    return None

# 사진 파일 목록
IMAGE_FILES = [
    "IMG_2886.jpg",
    "IMG_2536.jpg",
    "IMG_1288.jpeg",
    "IMG_1289.jpeg",
    "D757D1CF-D980-4429-B4D0-D83D6E190D9F.jpeg"
]

# 2. 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경 - 따뜻하고 밝은 파스텔톤 */
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFF8DC 100%);
    }

    /* 선명한 상단 타이틀 */
    .birthday-title {
        text-align: center;
        color: #B22222;
        font-family: 'Arial Black', sans-serif;
        font-size: 3.2rem;
        font-weight: 900;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .birthday-subtitle {
        text-align: center;
        color: #3E2723; /* 선명하고 어두운 색상으로 변경 */
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* 인증 화면 영역 텍스트 색상 강화 (배경 박스 제거) */
    .auth-section-title {
        color: #8B0000;
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 15px;
    }

    /* Streamlit 입력 폼 라벨 색상 선명하게 조정 */
    .stTextInput > label {
        color: #2B1B17 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* 비스듬한 폴라로이드 액자 스타일 */
    .tilted-photo {
        background: white;
        padding: 12px 12px 20px 12px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
        border-radius: 8px;
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .tilted-photo:hover {
        transform: scale(1.03) rotate(0deg) !important;
        z-index: 10;
    }
    .tilted-photo img {
        width: 100%;
        height: auto;
        border-radius: 4px;
        display: block;
    }

    /* 편지 등장 애니메이션 */
    @keyframes letterOpenAnimation {
        0% {
            opacity: 0;
            transform: translateY(40px) scale(0.95);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* 편지지 스타일 */
    .letter-paper {
        background: #FFFDF9;
        border: 2px solid #E8DCC4;
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
        color: #2B2B2B;
        line-height: 1.8;
        font-size: 1.1rem;
        animation: letterOpenAnimation 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .letter-header {
        font-size: 1.3rem;
        font-weight: bold;
        color: #B22222;
        margin-bottom: 15px;
    }

    .letter-signature {
        text-align: right;
        font-weight: bold;
        margin-top: 20px;
        color: #B22222;
    }
    </style>
""", unsafe_allow_html=True)

# 폭죽 효과 함수
def fire_confetti():
    st.components.v1.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            count = 200;
            defaults = { origin: { y: 0.7 } };

            function fire(particleRatio, opts) {
              confetti(Object.assign({}, defaults, opts, {
                particleCount: Math.floor(count * particleRatio)
              }));
            }

            fire(0.25, { spread: 26, startVelocity: 55, });
            fire(0.2, { spread: 60, });
            fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
            fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
            fire(0.1, { spread: 120, startVelocity: 45, });
        </script>
    """, height=0)

# 세션 상태 초기화
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False

# ---------------------------------------------------------
# [화면 1] 비밀번호 인증 화면
# ---------------------------------------------------------
if not st.session_state.authenticated:
    st.markdown("<div class='birthday-title'>🎉 Happy Birthday! 🎂</div>", unsafe_allow_html=True)
    st.markdown("<div class='birthday-subtitle'>엄마의 50번째 생일을 축하합니다!</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("")
        st.markdown("<div class='auth-section-title'>🔒 비밀번호 인증</div>", unsafe_allow_html=True)
        
        password_input = st.text_input(
            label="비밀번호를 입력하세요 (힌트: koo's bd)",
            placeholder="(0000.00.00)",
            type="password"
        )
        
        if st.button("확인", use_container_width=True):
            if password_input == "1976.09.04":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("비밀번호가 올바르지 않습니다. 다시 시도하세요.")

# ---------------------------------------------------------
# [화면 2] 인증 후 (편지 & 양옆 비스듬한 사진 배치)
# ---------------------------------------------------------
else:
    st.markdown("<div class='birthday-title'>✨ Happy 50th Birthday Mom! ✨</div>", unsafe_allow_html=True)
    st.markdown("<div class='birthday-subtitle'>사랑하는 엄마에게 마음을 담아 전하는 편지</div>", unsafe_allow_html=True)

    # 3개 컬럼 레이아웃 (왼쪽 사진 2장 / 중앙 편지 / 오른쪽 사진 3장)
    col_left, col_center, col_right = st.columns([1, 2, 1])

    # --- [왼쪽 컬럼: 사진 2장 (비스듬히)] ---
    with col_left:
        # 사진 1
        img1_b64 = get_image_base64(IMAGE_FILES[0])
        if img1_b64:
            st.markdown(f"""
                <div class="tilted-photo" style="transform: rotate(-4deg);">
                    <img src="{img1_b64}">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.image(IMAGE_FILES[0], use_container_width=True)

        # 사진 2
        img2_b64 = get_image_base64(IMAGE_FILES[1])
        if img2_b64:
            st.markdown(f"""
                <div class="tilted-photo" style="transform: rotate(3deg);">
                    <img src="{img2_b64}">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.image(IMAGE_FILES[1], use_container_width=True)

    # --- [중앙 컬럼: 편지] ---
    with col_center:
        if not st.session_state.letter_opened:
            st.write("")
            st.write("")
            st.info("✉️ 아래 버튼을 누르면 편지 봉투가 열리며 편지가 나타납니다.")
            if st.button("✉️ [편지 봉투 열기]", use_container_width=True):
                st.session_state.letter_opened = True
                fire_confetti()
                st.rerun()
        else:
            letter_text = """Dear 엄마. Happy 50th's birthday.<br><br>
I can't believe that your already half a century old. But on the bright side, you look like your in your mid 40's.<br><br>
Anyway, I'm sorry for not writing you a letter sooner. And also not doing anything on your birthday. But I will make it up to you by getting good grades on my midterm. I'm also sorry my first semester grades.<br><br>
I also thank you everyday(even thought I don't really say it) for giving me such a good opportunity and environment to study. And also for you believing in me.<br><br>
I hope you had a great 50th's birthday and age well and not get sick as often.<br><br>
Thanks and happy birthday!"""

            st.markdown(f"""
                <div class="letter-paper">
                    <div class="letter-header">💌 To. My Beloved Mom</div>
                    <div>{letter_text}</div>
                    <div class="letter-signature">-Daniel-</div>
                </div>
            """, unsafe_allow_html=True)

            st.write("")
            if st.button("✉️ 편지 다시 접기", use_container_width=True):
                st.session_state.letter_opened = False
                st.rerun()

    # --- [오른쪽 컬럼: 사진 3장 (비스듬히)] ---
    with col_right:
        # 사진 3
        img3_b64 = get_image_base64(IMAGE_FILES[2])
        if img3_b64:
            st.markdown(f"""
                <div class="tilted-photo" style="transform: rotate(4deg);">
                    <img src="{img3_b64}">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.image(IMAGE_FILES[2], use_container_width=True)

        # 사진 4
        img4_b64 = get_image_base64(IMAGE_FILES[3])
        if img4_b64:
            st.markdown(f"""
                <div class="tilted-photo" style="transform: rotate(-3deg);">
                    <img src="{img4_b64}">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.image(IMAGE_FILES[3], use_container_width=True)

        # 사진 5
        img5_b64 = get_image_base64(IMAGE_FILES[4])
        if img5_b64:
            st.markdown(f"""
                <div class="tilted-photo" style="transform: rotate(2deg);">
                    <img src="{img5_b64}">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.image(IMAGE_FILES[4], use_container_width=True)
