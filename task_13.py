#7

from tkinter import *
import math


## 클래스 선언 부분 ##
class Constituent:
    """단일 조화 분조"""
    def __init__(self, name, amplitude, period_hr, phase_deg=0.0):
        self.name = name
        self.A = amplitude
        self.T = period_hr
        self.phi = math.radians(phase_deg)
        self.enabled = True

    def eta(self, t):
        if not self.enabled:
            return
        return self.A * math.cos(2*math.pi*t/self.T - self.phi)
        


class Tide:
    """여러 분조의 합으로 조위를 계산"""

    def __init__(self, constituents):
        self.constituents = constituents

    def eta(self, t):
        # TODO: 각 분조의 eta(t) 를 더해서 총 조위 반환
        return sum(c.eta(t) for c in self.constituents)

    def by_name(self, name):
        for c in self.constituents:
            if c.name == name:
                return c
        return None


## 함수 선언 부분 ##
def toggle(name):
    """체크박스로 분조 on/off"""
    c = tide.by_name(name)
    if c is None:
        return
    c.enabled = bool(check_vars[name].get())


def step():
    """다음 프레임을 그린다 (애니메이션)"""
    global current_t
    current_t += 0.25   # 0.25 시간씩 진행
    draw()
    window.after(50, step)   # 50 ms 마다 갱신


def draw():
    canvas.delete("all")
    W = canvas.winfo_width()
    H = canvas.winfo_height()
    if W < 50 or H < 50:
        return

    # 표시할 시간 창: [current_t - 24h, current_t + 12h]
    t_left  = current_t - 24
    t_right = current_t + 12
    t_span  = t_right - t_left

    pad = 40
    y_mid = H / 2

    # 진폭 자동 결정 (현재 enabled 인 분조의 진폭 합)
    A_total = sum(c.A for c in tide.constituents if c.enabled) + 0.1
    y_scale = (H / 2 - pad) / A_total

    def to_px(t, eta):
        x = pad + (t - t_left) / t_span * (W - 2 * pad)
        y = y_mid - eta * y_scale
        return x, y

    # 가로축 (해수면 0 m 기준선)
    canvas.create_line(pad, y_mid, W - pad, y_mid, fill="#888888", dash=(2, 2))

    # 곡선
    pts = []
    n = 300
    for i in range(n + 1):
        t = t_left + t_span * i / n
        pts.append(to_px(t, tide.eta(t)))
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        canvas.create_line(x1, y1, x2, y2, fill="navy", width=2)

    # 현재 시각 (수직선)
    x_now, _ = to_px(current_t, 0)
    canvas.create_line(x_now, pad, x_now, H - pad, fill="red", width=1, dash=(4, 2))
    eta_now = tide.eta(current_t)
    canvas.create_text(x_now + 10, pad + 10,
                       text=f"t = {current_t:6.2f} h\nη = {eta_now:+.3f} m",
                       anchor="w", font=("Consolas", 10))


## 메인 코드 부분 ##
tide = Tide([
    Constituent("M2", 0.80, 12.4206, 0),
    Constituent("S2", 0.30, 12.0000, 30),
    Constituent("K1", 0.25, 23.9345, 60),
    Constituent("O1", 0.18, 25.8193, 90),
])

current_t = 0.0

window = Tk()
window.title("연습 7 - 조석 시뮬레이터")
window.geometry("640x460")

# 분조 on/off 체크박스
top = Frame(window)
top.pack(fill=X)
check_vars = {}
for c in tide.constituents:
    v = IntVar(value=1)
    check_vars[c.name] = v
    Checkbutton(top, text=f"{c.name}  A={c.A:.2f}m T={c.T:.2f}h",
                variable=v, command=lambda n=c.name: toggle(n)).pack(side=LEFT, padx=5)

# 그래프
canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

step()        # 애니메이션 시작
window.mainloop()

#10
from tkinter import *
from tkinter import messagebox
import math

R_EARTH = 6371.0   # km


## 클래스 선언 부분 ##
class GeoPoint:
    def __init__(self, lat, lon, name=""):
        self.lat = lat
        self.lon = lon
        self.name = name

    def distance_to(self, other):
        phi1 = math.radians(self.lat)
        phi2 = math.radians(other.lat)
        dphi = math.radians(other.lat - self.lat)
        dlmb = math.radians(other.lon - self.lon)
        a = (math.sin(dphi / 2) ** 2
             + math.cos(phi1) * math.cos(phi2) * math.sin(dlmb / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R_EARTH * c

    def bearing_to(self, other):
        phi1 = math.radians(self.lat)
        phi2 = math.radians(other.lat)
        dlmb = math.radians(other.lon - self.lon)
        y = math.sin(dlmb) * math.cos(phi2)
        x = (math.cos(phi1) * math.sin(phi2)
             - math.sin(phi1) * math.cos(phi2) * math.cos(dlmb))
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

#12
from tkinter import *


## 클래스 선언 부분 ##
class Population:
    def __init__(self, N0=5.0, K=1000.0, r=0.5, dt=0.1):
        self.N = N0
        self.K = K
        self.r = r
        self.dt = dt
        self.history = [N0]

    def step(self):
        dN = self.r * self.N * (1 - self.N / self.K) * self.dt
        self.N += dN
        self.history.append(self.N)

    def reset(self, N0=5.0):
        self.N = N0
        self.history = [N0]


## 함수 선언 부분 ##
running = False
after_id = None


def tick():
    global after_id
    pop.r = scale_r.get()
    pop.step()
    draw()
    if running:
        after_id = window.after(60, tick)


def on_start():
    global running
    if running:
        return
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

    yK = pad
    canvas.create_line(pad, yK, W - pad, yK, fill="#e0a0a0", dash=(4, 2))
    canvas.create_text(W - pad, yK - 8, anchor="e",
                       text=f"K = {pop.K:.0f}", fill="#c06060", font=("맑은 고딕", 9))

    def to_px(i, N):
        x = pad + (i / max(n - 1, 1)) * (W - 2 * pad)
        y = (H - pad) - (N / pop.K) * (H - 2 * pad)
        return x, y

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
