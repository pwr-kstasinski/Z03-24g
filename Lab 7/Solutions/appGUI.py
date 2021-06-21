import json.decoder
import numpy
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Frame
import datetime
from datetime import date
import pullData
import matplotlib.pyplot as plt


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = numpy.frombuffer(fig.canvas.tostring_argb(), dtype=numpy.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll(buf, 3, axis=2)
    return buf


def fig2img(fig):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data(fig)
    w, h, d = buf.shape
    return Image.frombuffer("RGBA", (w, h), buf.tobytes())


class Interface:
    root = tk.Tk()
    city_name: Entry
    loaded: bool = False
    plot_lab: Label
    data: (list, list, str)

    def __init__(self):
        self.root.geometry('570x500')
        self.root.resizable(False, False)
        self.interface()

    def interface(self):
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.root.title('WeatherApp')
        self.root.bind('<Return>', lambda event: self.display_for3days())
        title = Frame(self.root)
        title.grid(row=0, column=0, columnspan=3)

        prompt_lab = Label(title, text='Enter city name: ', font=('Arial', 12), padx=30)
        prompt_lab.grid(row=0, column=0)

        self.city_name = Entry(title, font=('Arial', 12), width=33)
        self.city_name.grid(row=0, column=1)

        button_search = Button(title, text='Search', font=('Arial', 12),
                               command=lambda: self.display_for3days())
        button_search.grid(row=0, column=2)

        today_button = Button(self.root, text='Today', font=('Arial', 12), width=20,
                              command=lambda: self.make_plot(date.today()))
        today_button.grid(row=1, column=0)

        tomorrow = date.today() + datetime.timedelta(days=1)
        tomorrow_button = Button(self.root, text=week_days[tomorrow.weekday()] + ' ' + str(tomorrow.day),
                                 font=('Arial', 12), width=20, command=lambda: self.make_plot(tomorrow))
        tomorrow_button.grid(row=1, column=1)

        third_day = date.today() + datetime.timedelta(days=2)
        third_day_button = Button(self.root, text=week_days[third_day.weekday()] + ' ' + str(third_day.day),
                                  font=('Arial', 12), width=20,
                                  command=lambda: self.make_plot(third_day))
        third_day_button.grid(row=1, column=2)

        self.plot_lab = Label(self.root)
        self.plot_lab.grid(row=3, columnspan=3)

        tk.mainloop()

    def display_for3days(self):
        self.plot_lab.configure(image=None)
        self.plot_lab.image = None
        self.loaded = True
        try:
            self.data = pullData.load_data(self.city_name.get())
            daily = self.data[0]
        except json.decoder.JSONDecodeError:
            self.city_name.insert(tk.END, ' : city not found')
            self.loaded = False
            return
        frames = [Frame(self.root), Frame(self.root), Frame(self.root)]
        frames[0].grid(row=2, column=0)
        frames[1].grid(row=2, column=1)
        frames[2].grid(row=2, column=2)
        self.city_name.delete(0, tk.END)
        self.city_name.insert(0, self.data[2])

        for day, f in zip(daily, frames):
            lab_max = Label(f, font=("Calibri bold", 18), text=str(day['max_temp']) + '°')
            lab_min = Label(f, font=("Calibri", 14), text=str(day['min_temp']) + '°')
            lab_max.grid(row=0, column=0)
            lab_min.grid(row=1, column=0)

            file = '.\\icons\\' + day['weather']['icon'] + '.png'
            icon = PhotoImage(file=file)
            label = Label(f, image=icon)
            label.image = icon
            label.grid(row=2, column=0)

            lab_name = Label(f, font=("Calibri", 14), text=str(day['weather']['description']))
            lab_name.grid(row=3, column=0)

    def make_plot(self, day):
        if self.loaded:
            week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            hourly = self.data[1]
            hours = []
            temps = []
            for x in hourly:
                if x['datetime'].day == day.day:
                    hours.append(x['datetime'].hour)
                    temps.append(x['temp'])
            fig, ax = plt.subplots()
            width = 0.75  # the width of the bars
            ax.bar(hours, temps, width, color="orange")
            plt.title('Hourly temperatures'+' for '+week_days[day.weekday()]+' '+str(day.day))
            im = fig2img(fig)
            base = 300
            wpercent = (base / float(im.size[0]))
            hsize = int((float(im.size[1]) * float(wpercent)))
            im = im.resize((base, hsize), Image.ANTIALIAS)
            plot = ImageTk.PhotoImage(im)
            self.plot_lab.configure(image=plot)
            self.plot_lab.image = plot


if __name__ == '__main__':
    window = Interface()
