import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import os

# 1. 500x500 하늘색 배경 이미지 생성(BGR 순서 : 하늘색은 약(255, 230, 170))
# NumPy로 (높이, 너비, 채널) 배열 생성
width, height = 500, 500
background_color = (255, 230, 170)  # BGR : Sky Blue
img = np.full((height, width, 3), background_color, dtype=np.uint8)

# 2. OpenCV를 이용한 상단 중앙 빨간색 영어 테스트
text_en = "OpenCV Text Practice"
font_en = cv2.FONT_HERSHEY_TRIPLEX
font_scale = 1.0
color_red = (0, 0, 255) #BGR
thickness =2

# 텍스트 크기 계산 후 중앙 정렬 위치 잡기
text_size, _ = cv2.getTextSize(text_en, font_en, font_scale, thickness)
text_x =  (width - text_size[0]) // 2
text_y = 70 # 상단 여백

cv2.putText(img, text_en, (text_x, text_y), font_en, font_scale, color_red, thickness)

# 3. 소개글 작성 (Gemini 번역 포함)
# 원문 : "ㅎㅇㅎㅇ 곽씨입니다 반가워요"
# Gmini 번역 : "Hi hi, I'm Mr. Gwak. Nice to meet you"
intro_ko = "ㅎㅇㅎㅇ \n곽씨입니다~\n반가워요 ʕ๑•̀‿-ʔ"
intro_en = "Hi hi, \nI'm Mr. Gwak.\nNice to meet you"

# 4. Pillow를 이용한 하단 한글/영어 출력 함수
def draw_korean_text(image, text, position, font_size, color):
    # OpenCV(BGR) -> Pillow(RGB)
    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    
    # 맥북에서 특수 기호를 가장 잘 지원하는 폰트 경로
    # Arial Unicode는 거의 모든 특수 기호를 포함합니다.
    font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        # 만약 위 경로에 없다면 시스템 기본 폰트 사용
        font = ImageFont.load_default()
        
    # Pillow의 draw.text는 \n을 인식하여 줄바꿈을 해줍니다.
    draw.text(position, text, font=font, fill=color, spacing=10) # spacing으로 줄 간격 조절
    
    # 다시 OpenCV용 BGR로 변환
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# 소개글 출력 (이미지 하단부)
full_intro = f"{intro_ko}\n{intro_en}"
img = draw_korean_text(img, full_intro, (50, 150), 30, (50, 50, 50))

# 5. 결과 확인
cv2.imshow('OpenCV & Pillow Text Practice', img)
print("이미지 창이 떴습니다. 아무 키나 누르면 종료됩니다.")
cv2.waitKey(0)
cv2.destroyAllWindows()

# 업데이트
