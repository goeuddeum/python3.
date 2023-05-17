import cv2

title = 'mouse event'  
img = cv2.imread('../img/blank_500.jpg')
cv2.imshow(title, img) 


def onMouse(event, x, y, flags, param): # 아무스 콜백 함수 구현 ---①
    cv2.rectangle(img, (495, 230), (90, 150), (0,50,100) )   
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누름인 경우 ---②
        cv2.putText(img, "goeuddeum", (97, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,102,153)) # 검정
        # 컨트롤키와 쉬프트 키를 모두 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY : 
            cv2.putText(img, "goeuddeum", (97, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (204,0,0)) #파랑
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : # 쉬프트 키를 누른 경우
            cv2.putText(img, "goeuddeum", (97, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,200,0)) #초록
        elif flags & cv2.EVENT_FLAG_CTRLKEY : # 컨트롤 키를 누른 경우
            cv2.putText(img, "goeuddeum", (97, 200), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,102)) #빨강
        cv2.imshow(title, img)          # 그려진 이미지를 다시 표시 ---③

cv2.setMouseCallback(title, onMouse)    # 마우스 콜백 함수를 GUI 윈도우에 등록 ---④
while True:
    if cv2.waitKey(0) & 0xFF == 27:     # esc로 종료
        break
cv2.destroyAllWindows()