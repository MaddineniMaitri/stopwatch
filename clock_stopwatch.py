import tkinter as tk
from datetime import datetime
import time

class ClockStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock & Stopwatch")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Clock Label
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.clock_label.pack(pady=10)

        # Stopwatch Label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
        self.stopwatch_label.pack(pady=10)

        # Stopwatch control buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", width=8, command=self.start_stopwatch)
        self.start_btn.pack(side="left", padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=8, command=self.stop_stopwatch)
        self.stop_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=self.reset_stopwatch)
        self.reset_btn.pack(side="left", padx=5)

        # Stopwatch variables
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Start the clock update loop
        self.update_clock()

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Time: " + current_time)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            now = time.time()
            elapsed = now - self.start_time + self.elapsed_time
            minutes, seconds = divmod(int(elapsed), 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.stopwatch_label.config(text=time_str)
            self.root.after(1000, self.update_stopwatch)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_stopwatch()

    def stop_stopwatch(self):
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

    def reset_stopwatch(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockStopwatchApp(root)
    root.mainloop()
