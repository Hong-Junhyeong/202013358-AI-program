import tkinter as tk
import time


# 전역 변수
running = False
seconds = 0
current_mode = ""
frame = None


def show_message(msg):
    label.config(text=msg)
    global current_mode, frame, running, seconds
    
    if msg == "현재 시간":
        current_mode = "Clock" # 시 계  모 드 라 고  컴 퓨 터 에 게  알 려 주 기
        running = False        # 시계 켰으니 타이머는 정지하기
        if frame:              # 화 면 에  타 이 머  버 튼 이  있 다 면  지 우 기
            frame.destroy()
            frame = None

        def update_time():
            if current_mode == "Clock":
                current = time.strftime("%H:%M:%S")
                label.config(text=current)
                root.after(1000, update_time)
#여기 적지 않으면 바로 실행 된다.
        update_time()

    else:
        current_mode = "Timer" # 타이머라고 컴튜터에게 알려주기
        if frame:              # 화면에 타이머 버튼이 있다면 지우기
            frame.destroy()
            frame = None

        def update_timer():
            global seconds
            if running:
                mins, secs = divmod(seconds, 60)
                label.config(text=f"{mins:02d}:{secs:02d}")
                seconds += 1
                root.after(1000, update_timer)

        def start():
            global running
            if not running: running = True; update_timer()

        def stop():
            global running
            running = False

        def reset():
            global running, seconds
            running = False; seconds = 0; label.config(text="00:00")

        frame = tk.Frame(root)
        frame.pack()
        tk.Button(frame, text="시 작 ", command=start).pack(side="left")
        tk.Button(frame, text="정 지 ", command=stop).pack(side="left")
        tk.Button(frame, text="초 기 화 ", command=reset).pack(side="left")


root = tk.Tk()


menu = tk.Menu(root)
Menu_menu = tk.Menu(menu, tearoff=0)
Menu_menu.add_command(label="Clock", command=lambda: show_message("현재 시간"))
Menu_menu.add_command(label="Timer", command=lambda: show_message("타이머"))
menu.add_cascade(label="Menu", menu=Menu_menu)
root.config(menu=menu)
label = tk.Label(root, text="")
label.pack()


label = tk.Label(root, font=("Arial", 24))
label.pack()


root.mainloop()
