import math
import tkinter as tk
from tkinter import ttk


def to_radians(deg: float) -> float:
    return math.radians(deg)


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0
    dlat = to_radians(lat2 - lat1)
    dlon = to_radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(to_radians(lat1)) * math.cos(to_radians(lat2)) * math.sin(dlon / 2) ** 2
    )
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)


class DistanceCalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("แอพคำนวณระยะทาง Python")
        self.geometry("520x380")
        self.resizable(False, False)
        self.configure(padx=16, pady=16)
        self.create_widgets()

    def create_widgets(self) -> None:
        header = ttk.Label(self, text="แอพคำนวณระยะทาง", font=(None, 18, "bold"))
        header.pack(pady=(0, 12))

        frame_geo = ttk.Labelframe(self, text="Haversine (ระหว่างพิกัด)")
        frame_geo.pack(fill="x", pady=8)
        self.build_geo_inputs(frame_geo)

        frame_plane = ttk.Labelframe(self, text="Euclidean (ระหว่างจุดในระนาบ)")
        frame_plane.pack(fill="x", pady=8)
        self.build_plane_inputs(frame_plane)

        self.result_label = ttk.Label(self, text="ผลลัพธ์จะแสดงที่นี่", font=(None, 12, "bold"))
        self.result_label.pack(pady=(12, 0))

    def build_geo_inputs(self, parent: ttk.Labelframe) -> None:
        labels = ["ละติจูด 1", "ลองจิจูด 1", "ละติจูด 2", "ลองจิจูด 2"]
        defaults = [13.7563, 100.5018, 13.7367, 100.5231]
        self.geo_vars = [tk.StringVar(value=str(value)) for value in defaults]












































    app.mainloop()    app = DistanceCalculatorApp()if __name__ == "__main__":            self.result_label.config(text="กรุณาใส่ตัวเลขที่ถูกต้อง")        except ValueError:            self.result_label.config(text=f"ระยะทางระหว่างจุด = {distance:.3f}")            distance = euclidean_distance(x1, y1, x2, y2)            x1, y1, x2, y2 = [float(var.get()) for var in self.plane_vars]        try:    def on_plane_calculate(self) -> None:            self.result_label.config(text="กรุณาใส่ตัวเลขที่ถูกต้อง")        except ValueError:            self.result_label.config(text=f"ระยะทางประมาณ {distance:.3f} กิโลเมตร")            distance = haversine_distance(lat1, lon1, lat2, lon2)            lat1, lon1, lat2, lon2 = [float(var.get()) for var in self.geo_vars]        try:    def on_geo_calculate(self) -> None:        button.grid(row=2, column=0, columnspan=4, pady=8)        button = ttk.Button(parent, text="คำนวณระยะทาง", command=self.on_plane_calculate)            entry.grid(row=index // 2, column=(index % 2) * 2 + 1, padx=8, pady=6)            entry = ttk.Entry(parent, textvariable=self.plane_vars[index], width=18)            label.grid(row=index // 2, column=(index % 2) * 2, padx=8, pady=6, sticky="w")            label = ttk.Label(parent, text=label_text)        for index, label_text in enumerate(labels):        self.plane_vars = [tk.StringVar(value=str(value)) for value in defaults]        defaults = [0.0, 0.0, 3.0, 4.0]        labels = ["X1", "Y1", "X2", "Y2"]    def build_plane_inputs(self, parent: ttk.Labelframe) -> None:        button.grid(row=2, column=0, columnspan=4, pady=8)        button = ttk.Button(parent, text="คำนวณ Haversine", command=self.on_geo_calculate)            entry.grid(row=index // 2, column=(index % 2) * 2 + 1, padx=8, pady=6)            entry = ttk.Entry(parent, textvariable=self.geo_vars[index], width=18)            label.grid(row=index // 2, column=(index % 2) * 2, padx=8, pady=6, sticky="w")            label = ttk.Label(parent, text=label_text)n        for index, label_text in enumerate(labels):