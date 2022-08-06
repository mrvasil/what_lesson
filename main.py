import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
import datetime
import pandas as pd
from  kivy.core.window import Window
Window.size = (360  , 780)
Builder.load_file("test.kv")
link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSfwVsLoL3Q6qf9OS6LK4DLxh0BENiCQVxE54c4MVHFtCr3gPQFl-JmmDA9-7NoGfIFju41VeALR8dl/pub?gid=1500532275&single=true&output=csv'
table = pd.read_csv(link).values.tolist()
weekday = datetime.datetime.today().weekday()
lines_of_days = [0, 12, 24, 34, 46]
start_of_lesson = [544, 589, 634, 694, 739, 784, 847, 919]
finish_of_lesson = [586, 631, 677, 736, 781, 826, 916, 961]
number_of_lesson = ['1  Первый урок', '2  Второй урок', '3  Третий урок', '4  Четвёртый урок', '5  Пятый урок', '6  Шестой урок', '7  Седьмой урок', '8  Восьмой урок']
def lesson_number(dateq):
	datew = (int(dateq[:-3])*60)+int(dateq[4:])
	for i in range(8):
		if datew > start_of_lesson[i] and datew < finish_of_lesson[i]:
			return number_of_lesson[i]
	return '77 Урока нет'

def answer_to_the_button(self, qs, ws):
	dt_now = str(datetime.datetime.now())[10:-10]
	strq = ''
	if (weekday == 5) or (weekday == 6):
		return 'Сейчас:\n' + dt_now + '\n' + 'Выходной'
	line = int(lesson_number(dt_now)[:2]) - 1
	lessons = table[line+lines_of_days[weekday]][qs:ws]
	for i in range(len(lessons)):
		strq += str(lessons[i]) + '\n'
	strq = strq.replace('nan', '')
	strq = strq.replace('1', '')
	return 'Сейчас:\n' + dt_now + '\n' + strq + '\n' + lesson_number(dt_now)[2:]



class RootWidget(BoxLayout):
	def five(self):
		self.lbl.text = answer_to_the_button(self, 3, 7)
	def six(self):
		self.lbl.text = answer_to_the_button(self, 7, 9)
	def sevenc(self):
		self.lbl.text = answer_to_the_button(self, 9, 13)
	def sevent(self):
		self.lbl.text = answer_to_the_button(self, 9, 13)
	def eight(self):
		self.lbl.text = answer_to_the_button(self, 13, 15)
	def nine(self):
		self.lbl.text = answer_to_the_button(self, 15, 17)
	def ten(self):
		self.lbl.text = answer_to_the_button(self, 17, 19)
	def eleven(self):
		self.lbl.text = answer_to_the_button(self, 19, 21)


class What_lessonApp(App):

	def build(self):
		return RootWidget()



myApp = What_lessonApp()
myApp.run()
