import cv2
import numpy as np

dot_card_list = [6, 9, 16, 19, 61, 66, 68, 69, 86, 89, 91, 96, 99]
img = cv2.imread('result.jpg')
for i in range(1, 101):
    img = cv2.imread('result.jpg')
    text = str(i)
    image_height, image_width, _ = img.shape
    (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 5, 10)
    x = (image_width - text_width) // 2
    y = (image_height + text_height) // 2  # OpenCV는 텍스트의 기준선이 아래쪽에 있음
    color = (149, 218, 238)  # 초록색
    line_type = cv2.LINE_AA
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 5, color, 10, line_type)
    if i in dot_card_list:
        cv2.circle(img, (x+text_width,y), 1, color, 10)

    top_left_x = 30
    top_left_y = 50  # Y 값은 텍스트 높이만큼 여유

    # 우하단 텍스트 좌표 계산
    (bottom_text_width, bottom_text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    bottom_right_x = image_width - bottom_text_width - 30  # 우측 끝에서 여유
    bottom_right_y = image_height - 30  # 하단 끝에서 여유

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2

    cv2.putText(img, text, (top_left_x, top_left_y), font, font_scale, color, thickness, line_type)
    if i in dot_card_list:
        cv2.circle(img, (top_left_x+bottom_text_width,top_left_y), 1, color, 2)

    # 좌상단 텍스트를 잘라서 180도 회전 후 우하단에 덮어씌우기
    text_roi = img[2:101, 2:101]  # 좌상단 텍스트 영역
    rotated_text = cv2.rotate(text_roi, cv2.ROTATE_180)  # 180도 회전
    img[image_height - 99:image_height+1, image_width - 99:image_width+1] = rotated_text  # 우하단에 덮어씌우기
    cv2.imwrite('./card/card_{}.jpg'.format(text), img)