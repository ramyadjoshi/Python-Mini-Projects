import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading
import time

class InvisibilityCloakApp:
    def __init__(self, master):
        self.master = master
        master.title("🪄 Invisibility Cloak (Tkinter)")
        self.stop_flag = False
        self.bg_captured = False

        # Video panel
        self.panel = tk.Label(master)
        self.panel.pack()

        # Buttons
        btn_frame = tk.Frame(master)
        btn_frame.pack(fill=tk.BOTH, pady=10)

        self.capture_bg_btn = tk.Button(btn_frame, text="Capture Background", command=self.capture_background, bg="#fff")
        self.capture_bg_btn.pack(side=tk.LEFT, padx=8)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop, bg="red", fg="white")
        self.stop_btn.pack(side=tk.RIGHT, padx=8)

        # OpenCV video capture
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Camera Error", "❌ Could not access the camera.")
            master.destroy()
            return

        # Background frame
        self.bg = None

        # Start the video stream
        self.thread = threading.Thread(target=self.video_loop, daemon=True)
        self.thread.start()

    def capture_background(self):
        if self.cap.isOpened():
            # Give camera time and grab 60 frames for safety
            time.sleep(1)
            for _ in range(60):
                ret, bg = self.cap.read()
                if ret:
                    self.bg = cv2.flip(bg, 1)
            self.bg_captured = True
            messagebox.showinfo("Background", "✅ Background captured.\nNow wear your cloak!")

    def video_loop(self):
        while not self.stop_flag:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            output = frame.copy()
            cloak_mask = None

            if self.bg_captured and self.bg is not None:
                # Main invisibility cloak logic
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                lower_red1 = np.array([0, 100, 50])
                upper_red1 = np.array([10, 255, 255])
                lower_red2 = np.array([170, 100, 50])
                upper_red2 = np.array([180, 255, 255])
                mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
                mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
                mask = mask1 + mask2

                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
                mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
                mask_inv = cv2.bitwise_not(mask)

                cloak_area = cv2.bitwise_and(self.bg, self.bg, mask=mask)
                non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
                output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

            # Convert for Tkinter display
            rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)

            # This keeps the GUI responsive
            if not self.stop_flag:
                self.master.update_idletasks()
                self.master.update()
        
        self.cap.release()
        self.master.quit()

    def stop(self):
        self.stop_flag = True

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = InvisibilityCloakApp(root)
    root.mainloop()
