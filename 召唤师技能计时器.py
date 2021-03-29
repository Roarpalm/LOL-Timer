import pyperclip, re
from time import time, sleep
from threading import Thread
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

class GUI():
    def __init__(self):
        self.isstop = False
        self.now = None
        self.window = QUiLoader().load("Timer.ui")
        self.window.setWindowIcon(QIcon("icon.ico"))
        self.window.start.clicked.connect(self.timer)
        self.window.stop.clicked.connect(self.reset_timer)
        self.window.min.display("00:00")
        self.window.Btn1.clicked.connect(self.btn1)
        self.window.Btn2.clicked.connect(self.btn2)
        self.window.Btn3.clicked.connect(self.btn3)
        self.window.Btn4.clicked.connect(self.btn4)
        self.window.Btn5.clicked.connect(self.btn5)
        self.window.Btn6.clicked.connect(self.btn6)
        self.window.Btn7.clicked.connect(self.btn7)
        self.window.Btn8.clicked.connect(self.btn8)
        self.window.Btn9.clicked.connect(self.btn9)
        self.window.Btn10.clicked.connect(self.btn10)
        self.window.Btn11.clicked.connect(self.btn11)
        self.window.Btn12.clicked.connect(self.btn12)
        self.window.Btn13.clicked.connect(self.btn13)
        self.window.Btn14.clicked.connect(self.btn14)
        self.window.Btn15.clicked.connect(self.btn15)

    def btn1(self):
        s = "上单闪现" + self.time_to_str(int(self.now) + 300)
        t = self.window.top_txt.text()
        if "上单闪现" in t:
            self.window.top_txt.setText(re.sub("上单闪现[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.top_txt.setText(s + " " + t)
        self.copy_txt()
    def btn2(self):
        s = "上单点燃" + self.time_to_str(int(self.now) + 210)
        t = self.window.top_txt.text()
        if "上单点燃" in t:
            self.window.top_txt.setText(re.sub("上单点燃[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.top_txt.setText(s + " " + t)
        self.copy_txt()
    def btn3(self):
        s = "上单传送" + self.time_to_str(int(self.now) + 360)
        t = self.window.top_txt.text()
        if "上单传送" in t:
            self.window.top_txt.setText(re.sub("上单传送[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.top_txt.setText(s + " " + t)
        self.copy_txt()
    def btn4(self):
        s = "打野闪现" + self.time_to_str(int(self.now) + 300)
        t = self.window.jug_txt.text()
        if "打野闪现" in t:
            self.window.jug_txt.setText(re.sub("打野闪现[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.jug_txt.setText(s + " " + t)
        self.copy_txt()
    def btn5(self):
        s = "打野疾跑" + self.time_to_str(int(self.now) + 180)
        t = self.window.jug_txt.text()
        if "打野疾跑" in t:
            self.window.jug_txt.setText(re.sub("打野疾跑[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.jug_txt.setText(s + " " + t)
        self.copy_txt()
    def btn6(self):
        s = "打野点燃" + self.time_to_str(int(self.now) + 210)
        t = self.window.jug_txt.text()
        if "打野点燃" in t:
            self.window.jug_txt.setText(re.sub("打野点燃[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.jug_txt.setText(s + " " + t)
        self.copy_txt()
    def btn7(self):
        s = "中单闪现" + self.time_to_str(int(self.now) + 300)
        t = self.window.mid_txt.text()
        if "中单闪现" in t:
            self.window.mid_txt.setText(re.sub("中单闪现[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.mid_txt.setText(s + " " + t)
        self.copy_txt()
    def btn8(self):
        s = "中单点燃" + self.time_to_str(int(self.now) + 210)
        t = self.window.mid_txt.text()
        if "中单点燃" in t:
            self.window.mid_txt.setText(re.sub("中单点燃[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.mid_txt.setText(s + " " + t)
        self.copy_txt()
    def btn9(self):
        s = "中单传送" + self.time_to_str(int(self.now) + 360)
        t = self.window.mid_txt.text()
        if "中单传送" in t:
            self.window.mid_txt.setText(re.sub("中单传送[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.mid_txt.setText(s + " " + t)
        self.copy_txt()
    def btn10(self):
        s = "ADC闪现" + self.time_to_str(int(self.now) + 300)
        t = self.window.adc_txt.text()
        if "ADC闪现" in t:
            self.window.adc_txt.setText(re.sub("ADC闪现[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.adc_txt.setText(s + " " + t)
        self.copy_txt()
    def btn11(self):
        s = "ADC治疗" + self.time_to_str(int(self.now) + 270)
        t = self.window.adc_txt.text()
        if "ADC治疗" in t:
            self.window.adc_txt.setText(re.sub("ADC治疗[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.adc_txt.setText(s + " " + t)
        self.copy_txt()
    def btn12(self):
        s = "ADC净化" + self.time_to_str(int(self.now) + 210)
        t = self.window.adc_txt.text()
        if "ADC净化" in t:
            self.window.adc_txt.setText(re.sub("ADC净化[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.adc_txt.setText(s + " " + t)
        self.copy_txt()
    def btn13(self):
        s = "辅助闪现" + self.time_to_str(int(self.now) + 300)
        t = self.window.sup_txt.text()
        if "辅助闪现" in t:
            self.window.sup_txt.setText(re.sub("辅助闪现[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.sup_txt.setText(s + " " + t)
        self.copy_txt()
    def btn14(self):
        s = "辅助点燃" + self.time_to_str(int(self.now) + 210)
        t = self.window.sup_txt.text()
        if "辅助点燃" in t:
            self.window.sup_txt.setText(re.sub("辅助点燃[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.sup_txt.setText(s + " " + t)
        self.copy_txt()
    def btn15(self):
        s = "辅助虚弱" + self.time_to_str(int(self.now) + 210)
        t = self.window.sup_txt.text()
        if "辅助虚弱" in t:
            self.window.sup_txt.setText(re.sub("辅助虚弱[0-9]{2}:[0-9]{2}", s, t))
        else:
            self.window.sup_txt.setText(s + " " + t)
        self.copy_txt()

    def time_to_str(self, t):
        """时间转文字"""
        min = int(t) // 60
        sss = int(t) % 60
        if min < 10:
            min = "0" + str(min)
        if sss < 10:
            sss = "0" + str(sss)
        return str(min) + ":" + str(sss)

    def timer(self):
        def run_main():
            self.isstop = False
            start = time()
            while not self.isstop:
                sleep(1)
                self.now = time() - start
                self.window.min.display(self.time_to_str(self.now))
            self.window.min.display("00:00")
        t = Thread(target=run_main)
        t.start()

    def copy_txt(self):
        """复制文本到windows剪贴板"""
        txt = self.window.top_txt.text() + self.window.jug_txt.text() + self.window.mid_txt.text() + self.window.adc_txt.text() + self.window.sup_txt.text()
        pyperclip.copy(txt)

    def reset_timer(self):
        """重置计时器"""
        def run_main():
            self.isstop = True
            self.window.top_txt.setText("")
            self.window.jug_txt.setText("")
            self.window.mid_txt.setText("")
            self.window.adc_txt.setText("")
            self.window.sup_txt.setText("")
            pyperclip.copy("")
        t = Thread(target=run_main)
        t.start()

if __name__ == "__main__":
    app = QApplication([])
    stats = GUI()
    stats.window.show()
    app.exec_()