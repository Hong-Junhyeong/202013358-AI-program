#10_geopoint
from tkinter import *
from tkinter import messagebox
import math

R_EARTH = 6371.0   # km



## 클래스 선언 부분 ##
class GeoPoint:
    """위도(lat)·경도(lon) 한 지점"""

    def __init__(self, lat, lon, name=""):
        self.lat = lat
        self.lon = lon
        self.name = name

    def distance_to(self, other):
        # 1. 계산에 필요한 값을 함수가 시작되자마자 '미리' 정의합니다.
        phi1 = math.radians(self.lat)
        phi2 = math.radians(other.lat)
        dphi = math.radians(other.lat - self.lat)
        dlmb = math.radians(other.lon - self.lon)
        
        # 2. 미리 정의한 변수들로 간단하게 하버사인 공식을 계산합니다.
        a = (math.sin(dphi / 2) ** 2
             + math.cos(phi1) * math.cos(phi2) * math.sin(dlmb / 2) ** 2)
        c = 2 * math.asin(math.sqrt(a)) # 지난번에 줄인 공식 적용 예시
        return R_EARTH * c # 6371.0km * 중심각 = 실제 거리(km)            

    def bearing_to(self, other):
        """other 로 향하는 초기 방위각 [deg, 0~360]"""
        phi1 = math.radians(self.lat)
        phi2 = math.radians(other.lat)
        dlmb = math.radians(other.lon - self.lon)
    
        y = math.sin(dlmb) * math.cos(phi2)
        x = (math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlmb)) # (잘린 부분 추정)
         
        return (math.degrees(math.atan2(y, x)) + 360) % 360
        
    def __repr__(self):
        return f"GeoPoint({self.lat}, {self.lon}, {self.name!r})"


## 함수 선언 부분 ##
def on_calc():
    try:
        p1 = GeoPoint(float(e_lat1.get()), float(e_lon1.get()), "지점1")
        p2 = GeoPoint(float(e_lat2.get()), float(e_lon2.get()), "지점2")
    except ValueError:
        messagebox.showerror("입력 오류", "위도/경도는 숫자로 입력해 주세요.")
        return

    d = p1.distance_to(p2)
    b = p1.bearing_to(p2)
    result.config(text=f"거리   = {d:9.3f} km\n방위각 = {b:9.2f}°  (정북 기준)")


## 메인 코드 부분 ##
window = Tk()
window.title("연습 10 - 거리·방위 계산기 (Haversine)")
window.geometry("420x240")

Label(window, text="지점 1", font=("맑은 고딕", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 2))
Label(window, text="위도:").grid(row=1, column=0, sticky="e", padx=5)
e_lat1 = Entry(window, width=10); e_lat1.grid(row=1, column=1); e_lat1.insert(0, "35.18")
Label(window, text="경도:").grid(row=2, column=0, sticky="e", padx=5)
e_lon1 = Entry(window, width=10); e_lon1.grid(row=2, column=1); e_lon1.insert(0, "129.08")

Label(window, text="지점 2", font=("맑은 고딕", 10, "bold")).grid(row=0, column=2, columnspan=2, pady=(10, 2))
Label(window, text="위도:").grid(row=1, column=2, sticky="e", padx=5)
e_lat2 = Entry(window, width=10); e_lat2.grid(row=1, column=3); e_lat2.insert(0, "33.51")
Label(window, text="경도:").grid(row=2, column=2, sticky="e", padx=5)
e_lon2 = Entry(window, width=10); e_lon2.grid(row=2, column=3); e_lon2.insert(0, "126.53")

Button(window, text="계산", width=14, command=on_calc).grid(row=3, column=0, columnspan=4, pady=12)
result = Label(window, text="", font=("Consolas", 12), justify=LEFT)
result.grid(row=4, column=0, columnspan=4)

window.mainloop()





#12_plankton_growth
from tkinter import *
import math


## 클래스 선언 부분 ##
class Population:
    def __init__(self, N0=5.0, K=1000.0, r=0.5, dt=0.1):
        self.N = N0          # 현재 개체수
        self.K = K           # 환경수용력
        self.r = r           # 성장률
        self.dt = dt
        self.history = [N0]  # 시계열 기록

    def step(self):
        """한 시간 스텝 전진 (로지스틱)"""
        # TODO: dN = r*N*(1 - N/K)*dt 계산 후 self.N 갱신
        # TODO: self.history 에 새 N 추가
        dN = self.r*self.N*(1 - self.N/self.K)*self.dt
        self.N = self.N + dN
        self.history.append(self.N)

    def reset(self, N0=5.0):
        self.N = N0
        self.history = [N0]


## 함수 선언 부분 ##
running = False
after_id = None


def tick():
    global after_id
    pop.r = scale_r.get()          # 슬라이더에서 성장률 읽기
    pop.step()
    draw()
    if running:
        after_id = window.after(60, tick)


def on_start():
    global running
    if running:
        return                     # 중복 시작 방지
    running = True
    tick()


def on_pause():
    global running
    running = False


def on_reset():
    global running
    running = False
    pop.reset()
    draw()


def draw():
    canvas.delete("all")
    W = canvas.winfo_width()
    H = canvas.winfo_height()
    if W < 50 or H < 50:
        return
    pad = 40
    hist = pop.history
    n = len(hist)

    # K 수용력 선
    yK = pad
    canvas.create_line(pad, yK, W - pad, yK, fill="#e0a0a0", dash=(4, 2))
    canvas.create_text(W - pad, yK - 8, anchor="e",
                       text=f"K = {pop.K:.0f}", fill="#c06060", font=("맑은 고딕", 9))

    def to_px(i, N):
        x = pad + (i / max(n - 1, 1)) * (W - 2 * pad)
        y = (H - pad) - (N / pop.K) * (H - 2 * pad)
        return x, y

    # 곡선
    pts = [to_px(i, N) for i, N in enumerate(hist)]
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        canvas.create_line(x1, y1, x2, y2, fill="seagreen", width=2)

    canvas.create_text(pad + 4, pad - 20, anchor="w",
                       text=f"N = {pop.N:8.1f}    r = {pop.r:.2f}    step = {n-1}",
                       font=("Consolas", 10))


## 메인 코드 부분 ##
pop = Population()

window = Tk()
window.title("연습 12 - 플랑크톤 개체군 성장")
window.geometry("560x420")

top = Frame(window); top.pack(fill=X, pady=6)
Button(top, text="시작", width=7, command=on_start).pack(side=LEFT, padx=4)
Button(top, text="정지", width=7, command=on_pause).pack(side=LEFT, padx=4)
Button(top, text="리셋", width=7, command=on_reset).pack(side=LEFT, padx=4)

Label(top, text="성장률 r:").pack(side=LEFT, padx=(20, 2))
scale_r = Scale(top, from_=0.0, to=2.0, resolution=0.05,
                orient=HORIZONTAL, length=180)
scale_r.set(0.5)
scale_r.pack(side=LEFT)

canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True, padx=10, pady=8)

draw()
window.mainloop()
