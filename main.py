import cv2  # pip install opencv-python
from tkinter import *   # встроенный модуль
from PIL import Image, ImageTk # установка (pip install Pillow)


def show_frames():
    ret, image = cap.read()  # ret тип Boolean (True/False). Если image прочитан true
    img_color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # делаем правильные цвета
    # преобразовываем формат img для tkinter
    img = Image.fromarray(img_color)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(ms=20, func=show_frames)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # ,cv2.CAP_DSHOW открываем камеру
window = Tk()
label = Label(window)
label.pack()
label.after(ms=20, func=show_frames) # через ms вызывает функцию func, по этому получается видео из img



window.mainloop()
cap.release()
cv2.destroyAllWindows()
