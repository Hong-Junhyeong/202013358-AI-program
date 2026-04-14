import json
import os

file_path = "addressbook.json"

#시작 시 기존 데이터 불러오기
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        addressbook = json.load(f)

#데이터 변환 코드
    for name in addressbook:
        if isinstance(addressbook[name], str):
            old_phone = addressbook[name]
            addressbook[name] = {"phone": old_phone, "group": "미지정", "favorite": "N", "speed_dial":"없음"}


else:
    addressbook = {} 

#2. 메인 루프 (메뉴 선택)
while True:
    print("\n--[메뉴] 1.등록 2.검색 3.삭제 4.즐겨찾기 5.단축번호설정 6.그룹화  7.종료 ---")
    choice = input("작업할 번호를 선택하세요:")

    if choice == "1":
        # 이름에 '끝'을 입력할 때까지 무한 반복 등록
        print(">> 등록을 시작합니다. (그만하려면 이름에 '끝' 입력)")
        name = None
        while(True) :
            name = input("이름을 입력하세요: ")
            if(name == "끝"): 
                break

            phoneNum = input("전화번호를 입력하세요:")
            addressbook[name] = phoneNum
        print(">> 등록이 완료되었습니다.")

    elif choice == "2":
        search_name = input("검색할 이름: ")
        if search_name in addressbook:
            print(f">> {search_name}의 번호를 {addressbook[search_name]}입니다.")
        else:
            print(">> 주소록에 없는 이름입니다.")
    
    elif choice == "3":
        del_name = input("삭제할 이름:")
        if del_name in addressbook:
            del addressbook[del_name]
            print(f">> {del_name}님이 삭제되었습니다.")
        else:
            print(">> 삭제할 이름이 주소록에 없급니다.")

    elif choice == "4":
        name = input("즐겨찾기 등록/해제할 이름:")
        if name in addressbook:
            addressbook[name]["favorite"] = "Y" if addressbook[name]["favorite"] == "N" else "N"
            status = "등록" if addressbook[name]["favorite"] == "Y" else "해제"
            print(f">> {name}님이 즐겨찾기에 {status}되었습습니다.")

    elif choice == "5":
        name = input("단축전호를 설정/삭제할  이름:")
        if name in addressbook:
            print((f"현재 단축번호: {addressbook[name]['speed_dial']}"))
            sd_num = input("새 단축번호 (삭제하려면 그냥 엔터 또는 '없음' 입력):")
                
            if sd_num == "" or sd_num == "없음":
                addressbook[name]["speed_dial"] = "없음"
                print(f">> {name}님의 단축번호가 삭제되었습니다.")
            else:
                addressbook[name]["speed_dial"] = sd_num
                print(f">> {name}님에게 단축번호 {sd_num}번이 설정되었습니다.")


    elif choice == "6":
        group_name = input("그룹명 (예: 친구, 가족): ")
        target_name = input(f"'{group_name}' 그룹에 추가할 사람 이름: ")
        
        if target_name in addressbook:
            addressbook[target_name]["group"] = group_name
            print(f">> {target_name}님이 '{group_name}' 그룹에 배정되었습니다.")
        else:
            print(">> 주소록에 없는 사람입니다.")


    elif choice == "7":
        # 종료 시점에 파일 저장
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(addressbook, f, ensure_ascii=False, indent=4)
        print(">> 저장 완료! 종료합니다.")
        print("end of put")
        break


    else:
        print(">> 잘못된 입력입니다. 1~4번 중 골라주세요.")




'''
# 2. 파일에서 다시 불러오기
with open("addressbook.json", "r", encoding="utf-8") as f:
    addressbook = json.load(f)

print("불러온 주소록:", addressbook)
print("김영호 번호:", addressbook["김영호"])
'''
