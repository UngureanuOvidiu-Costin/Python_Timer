from tkinter import *
import pygame


#
numar_secunde = 61




audioFlip = 1
def audio():
    global audioFlip
    if audioFlip == 1:
        audioFlip = 0
        try:
            #############################
            pygame.mixer.init()
            pygame.mixer.music.load("TING.wav")
            pygame.mixer.music.play()
            return 'red'
            #############################
        except:
            print("Keep it going")


def reverse_audio():
    global audioFlip
    audioFlip = 1
    return 'white'


class NiceCounter:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("+0+0")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-alpha", 0.01)
        self.root.resizable(0, 0)

        self.seconds = numar_secunde
        self.bitLock = 0
        self.increaseTime = 0

        self.timer_display = Label(self.root, font=('Trebuchet MS', 30, 'bold'), bg='black')
        self.timer_display.pack()

    def countdown(self, seconds, increase=0):
        if seconds > 0:
            if self.increaseTime == 1:
                seconds = seconds + 60
                self.increaseTime = 0
            hours, minutes = 0, 0
            minutes, secs = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_display.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, secs),
                                      fg=audio() if seconds <= 60 else reverse_audio())
            self.root.after(1000, self.countdown, seconds - 1)
        else:
            self.root.wm_attributes('-alpha', 0.01)  # Fac sa dispara fereastra
            self.bitLock = 0
            # toast = ToastNotifier()
            # toast.show_toast("ATCTI Countdown", "S-a scurs timpul!", duration=10)

    def start_countdown(self, event):
        if self.bitLock == 0:
            self.bitLock = 1
            self.root.wm_attributes('-alpha', 0.9)  # Fac sa apara fereastra
            self.countdown(self.seconds)
        else:
            self.increaseTime = 1

    def Go(self):
        self.root.bind('x', self.start_countdown)
        self.root.bind('q', lambda e: self.root.destroy())  # Mod de inchidere fereastra
        self.root.mainloop()


obiect = NiceCounter()
obiect.Go()
