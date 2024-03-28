import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import wavio
import threading
import time

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder")
        self.master.geometry("300x200")

        self.start_button = tk.Button(master, text="Start", command=self.start_recording, bg="#4CAF50", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_recording, state=tk.DISABLED, bg="#f44336", fg="white")
        self.stop_button.pack(pady=5)

        self.timer_label = tk.Label(master, text="00:00", font=("Helvetica", 18))
        self.timer_label.pack(pady=5)

        self.recording = False
        self.start_time = None

    def start_recording(self):
        self.recording = True
        self.start_time = time.time()

        # Update button states
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start timer
        threading.Thread(target=self.update_timer).start()

        # Start recording
        threading.Thread(target=self.record_audio).start()

    def stop_recording(self):
        self.recording = False

        # Update button states
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def record_audio(self):
        fs = 44100  # Sampling frequency
        duration = 10  # Recording duration (in seconds)
        
        frames = int(duration * fs)
        recording = sd.rec(frames, samplerate=fs, channels=2, dtype='int16')
        sd.wait()

        filename = "recording.wav"
        wavio.write(filename, recording, fs, sampwidth=2)
        messagebox.showinfo("Success", "Recording saved successfully!")

    def update_timer(self):
        while self.recording:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            time.sleep(1)

def main():
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
