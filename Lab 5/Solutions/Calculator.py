import tkinter as tk
from tkinter.ttk import Button, Label, Style
import Calculate


class Window:
    # setting up graphical interface
    def __init__(self):
        self.equation: str = ''
        self.tree = None
        self.root = tk.Tk()

        self.root.title('Calculator')
        self.root.resizable(True, True)
        self.root.geometry('270x200')

        self.entry_display = Label(self.root, width=20, background='white', relief='groove', anchor='e')
        self.entry_display.grid(row=0, columnspan=4, sticky='nsew')

        button_print = Button(self.root, text='Print', command=lambda: self.print_tree())
        button_print.grid(row=0, column=4, sticky='nsew')

        self.result_display = Label(self.root, background='white', relief='groove', anchor='e')
        self.result_display.grid(row=1, columnspan=2, sticky='nsew')

        button_sign = Button(self.root, text='+/-', command=lambda: self.change_sign())
        button_sign.grid(row=1, column=2, sticky='nsew')

        button_clear = Button(self.root, text='CE', command=lambda: self.clear())
        button_clear.grid(row=1, column=3, sticky='nsew')

        # setting up style for bold numbers
        bold_style = Style()
        bold_style.configure('Bold.TButton', font=('Sans', '10', 'bold'))

        # backspace icon in base64
        img = tk.PhotoImage(
            data=('iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAMAAAAMCGV4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxj'
                  'wv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAByUExURQAAAAAAAAAAAAAAAD8/PzMzMxgYGBkZGS'
                  'AgIB8fHx4eHhoaGh8fHx4eHhsbGxsbGx4eHhwcHB0dHRwcHBwcHB0dHRwcHBwcHB0dHR0dHRwcHB0'
                  'dHRwcHB0dHRwcHBwcHB0dHRwcHBwcHBwcHB0dHf///5LrNGMAAAAkdFJOUwABAgQEBRUeHyAiMDEz'
                  'QEFVWGBhf4CQn6Olqq/Fz9Tc6u75+iXEvawAAAABYktHRCXDAckPAAAAZUlEQVQI122OVw6AMAxDT'
                  'dmj7L0Lvf8ZSREglv9eLDsGvtJs95CjK27kpZ4wXsLTTyRgzTlYygAeICRuBxOeqBgXpeJ49SnDRU'
                  'cnxWO7/8jkZODPf+epv3j0UyK6/wfq577P/rs2N84LOf7EN/8AAAAASUVORK5CYII'))
        button_backspace = Button(self.root, image=img, command=lambda: self.backspace())
        button_backspace.grid(row=1, column=4, sticky='nsew')

        button_par_left = Button(self.root, text='(', command=lambda: self.append_sign('('))
        button_par_left.grid(row=2, column=0, sticky='nsew')

        button_par_right = Button(self.root, text=')', command=lambda: self.append_sign(')'))
        button_par_right.grid(row=2, column=1, sticky='nsew')

        button_fact = Button(self.root, text='n!', command=lambda: self.append_sign('!'))
        button_fact.grid(row=2, column=2, sticky='nsew')

        button_div = Button(self.root, text='/', command=lambda: self.append_sign('/'))
        button_div.grid(row=2, column=3, sticky='nsew')

        button_pow = Button(self.root, text='^', command=lambda: self.append_sign('^'))
        button_pow.grid(row=2, column=4, sticky='nsew')

        button_one = Button(self.root, text='1', command=lambda: self.append_sign('1'), style='Bold.TButton', )
        button_one.grid(row=3, column=0, sticky='nsew')

        button_two = Button(self.root, text='2', command=lambda: self.append_sign('2'), style='Bold.TButton')
        button_two.grid(row=3, column=1, sticky='nsew')

        button_three = Button(self.root, text='3', command=lambda: self.append_sign('3'), style='Bold.TButton')
        button_three.grid(row=3, column=2, sticky='nsew')

        button_mul = Button(self.root, text='*', command=lambda: self.append_sign('*'))
        button_mul.grid(row=3, column=3, sticky='nsew')

        button_sqrt = Button(self.root, text='sqrt', command=lambda: self.append_sign('sqrt'))
        button_sqrt.grid(row=3, column=4, sticky='nsew')

        button_four = Button(self.root, text='4', command=lambda: self.append_sign('4'), style='Bold.TButton')
        button_four.grid(row=4, column=0, sticky='nsew')

        button_five = Button(self.root, text='5', command=lambda: self.append_sign('5'), style='Bold.TButton')
        button_five.grid(row=4, column=1, sticky='nsew')

        button_six = Button(self.root, text='6', command=lambda: self.append_sign('6'), style='Bold.TButton')
        button_six.grid(row=4, column=2, sticky='nsew')

        button_minus = Button(self.root, text='-', command=lambda: self.append_sign('-'))
        button_minus.grid(row=4, column=3, sticky='nsew')

        button_abs = Button(self.root, text='|x|', command=lambda: self.append_sign('abs'))
        button_abs.grid(row=4, column=4, sticky='nsew')

        button_seven = Button(self.root, text='7', command=lambda: self.append_sign('7'), style='Bold.TButton')
        button_seven.grid(row=5, column=0, sticky='nsew')

        button_eight = Button(self.root, text='8', command=lambda: self.append_sign('8'), style='Bold.TButton')
        button_eight.grid(row=5, column=1, sticky='nsew')

        button_nine = Button(self.root, text='9', command=lambda: self.append_sign('9'), style='Bold.TButton')
        button_nine.grid(row=5, column=2, sticky='nsew')

        button_plus = Button(self.root, text='+', command=lambda: self.append_sign('+'))
        button_plus.grid(row=5, column=3, sticky='nsew')

        button_mod = Button(self.root, text='mod', command=lambda: self.append_sign('mod'))
        button_mod.grid(row=5, column=4, sticky='nsew')

        button_log = Button(self.root, text='log', command=lambda: self.append_sign('log'))
        button_log.grid(row=6, column=0, sticky='nsew')

        button_zero = Button(self.root, text='0', command=lambda: self.append_sign('0'), style='Bold.TButton')
        button_zero.grid(row=6, column=1, sticky='nsew')

        button_dot = Button(self.root, text='.', command=lambda: self.append_sign('.'))
        button_dot.grid(row=6, column=2, sticky='nsew')

        button_eq = Button(self.root, text='=', command=lambda: self.solve_equation())
        button_eq.grid(row=6, column=3, sticky='nsew')

        button_inv = Button(self.root, text='1/x', command=lambda: self.append_sign('1 /'))
        button_inv.grid(row=6, column=4, sticky='nsew')

        for x in range(5):
            self.root.columnconfigure(x, weight=1)

        for y in range(7):
            self.root.rowconfigure(y, weight=1)

        self.root.mainloop()

    def append_sign(self, sign):
        if sign != 'sqrt' and sign != 'log' and sign != 'abs' and sign != '1 /':
            if not sign.isnumeric() and sign != '.':
                sign = sign + ' '
                if len(self.equation) > 0 and self.equation[-1] != ' ':
                    sign = ' ' + sign

            self.equation += sign
            self.entry_display.configure(text=self.equation)
        elif not self.equation:
            self.entry_display.configure(text=sign + ' ')
        else:
            elements = self.equation.split()
            if elements[-1].isnumeric():
                elements.insert(-1, sign)
                elements.insert(-1, '(')
                elements.append(')')
                self.equation = " ".join(elements)
                self.entry_display.configure(text=self.equation)
            elif elements[-1] in ['+', '-', '*', '/', '!', '^', 'mod']:
                self.equation += sign + ' '
                self.entry_display.configure(text=self.equation)
            elif elements[-1] == ')':
                elements.reverse()
                stack = []
                index = None
                for i in range(0, elements.__len__()):
                    if elements[i] == ')':
                        stack.append(elements[i])
                    elif elements[i] == '(':
                        stack.pop()
                    if not stack:
                        index = i
                        break
                if index is not None:
                    elements.insert(index + 1, sign)
                    elements.reverse()
                    self.equation = " ".join(elements)
                    self.entry_display.configure(text=self.equation)

    def backspace(self):
        if self.equation and self.equation[-1] == ' ':
            self.equation = self.equation[:-1]
        self.equation = self.equation[:-1]
        self.entry_display.configure(text=self.equation)

    def clear(self):
        self.equation = ''
        self.entry_display.configure(text=self.equation)
        self.result_display.configure(text=self.equation)
        self.tree = None

    def solve_equation(self):
        if self.equation:
            try:
                self.tree = Calculate.equation_to_tree(self.equation)
                result = Calculate.evaluate(self.tree)
                self.result_display.configure(text=str(result))
            except ZeroDivisionError:
                self.result_display.configure(text='Error division by zero')

    def print_tree(self):
        if self.tree is not None:
            PopupWindow(self.root, Calculate.print_string_return(self.tree))
        else:
            PopupWindow(self.root, 'There is no tree to print')

    def change_sign(self):
        elements = self.equation.split()
        if elements[-1].isnumeric() or self.is_number(elements[-1]):
            elements.insert(-1, '(')
            elements[-1] = '-' + elements[-1]
            elements.append(')')
            self.equation = " ".join(elements)
            self.entry_display.configure(text=self.equation)

    @staticmethod
    def is_number(s: str):
        try:
            float(s)
            return True
        except ValueError:
            return False


class PopupWindow:

    def __init__(self, master, printed_tree):
        pop_window = tk.Toplevel(master)
        pop_window.title('Tree')
        pop_window.resizable(False, False)

        pop_window.columnconfigure(0, weight=1)
        pop_window.rowconfigure(0, weight=1)

        monospace_style = Style()
        monospace_style.configure('Monospace.TButton', font=('Consolas', '10'))

        label = Label(pop_window, text=printed_tree, style='Monospace.TButton')
        label.grid(row=0, column=0, columnspan=2, sticky='ew')

        button_close = tk.Button(pop_window, text='Close', command=pop_window.destroy)
        button_close.grid(row=1, column=0)


if __name__ == '__main__':
    window = Window()
