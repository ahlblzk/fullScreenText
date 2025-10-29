# -*- coding: utf-8 -*-
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QPalette, QFont

# 50条不同的祝福语句
messages = [
   "心怀希望，今天也要加油！", "愿你拥有宁静而美好的心情。", "每天都是新的开始，拥抱阳光。",
"笑容是最美的装饰。", "用心生活，幸福自来。", "愿你心情像花儿一样绽放。",
"今天也要温柔以待自己。", "努力的你最可爱。", "幸福就在身边，不要错过。",
"相信未来，保持热爱。", "愿你每一步都坚定而从容。", "生活因善良而美丽。",
"感受微风，享受阳光。", "每天都值得期待。", "心有梦想，路就在脚下。",
"温柔对待自己，也温柔对待世界。", "用笑容感染周围的人。", "愿你每一天都充满正能量。",
"心怀感恩，生活更加甜美。", "阳光总会驱散阴霾。", "你值得被爱与珍惜。",
"每一天都是成长的机会。", "保持好奇心，发现生活的美好。", "微笑面对困难，勇敢前行。",
"愿你每天都有小确幸。", "温暖的心，温暖的世界。", "今天也要保持好心情。",
"生活因你而精彩。", "愿你收获满满的喜悦。", "心中有爱，眼中有光。",
"每天都是新奇的冒险。", "相信自己，你很棒。", "快乐是最简单的幸福。",
"用心感受每一刻。", "努力不负青春。", "愿你平安喜乐，幸福长久。",
"每一个微笑都是力量。", "心怀希望，步履坚定。", "今天也要热爱生活。",
"温柔而坚定，幸福自来。", "愿你被生活温柔相待。", "笑对人生，心怀感恩。",
"坚持梦想，不惧风雨。", "阳光下的你最美丽。", "保持微笑，迎接挑战。",
"每一天都是礼物，珍惜它。", "勇敢追梦，收获精彩。", "愿你每天都充满好心情。",
"心怀善意，世界更美好。", "温柔是最强的力量。", "今天也要努力做自己喜欢的事。",
"感恩每一个小幸福。", "愿你遇见美好的人和事。", "生活因你而温暖。",
"保持好心态，幸福随之而来。", "每天都值得庆祝。", "愿你每天都有小惊喜。",
"心怀梦想，脚踏实地。", "温暖自己，也温暖他人。", "笑容是生活的魔法。",
"今天也要善待自己。", "生活充满可能性，勇敢尝试。", "心中有光，前路明亮。",
"相信努力的力量。", "愿你每天都被幸运拥抱。", "微笑面对生活的挑战。",
"温柔且坚定地前行。", "保持热爱，世界会回应。", "每天都是新的希望。",
"心怀感恩，生活美好。", "愿你每一天都被阳光照亮。", "用心感受生活的美妙。",
"笑容如花，心情如歌。", "努力不问回报，幸福自然来。", "今天也要勇敢地做自己。",
"保持微笑，迎接每一个清晨。", "愿你每天都能收获小幸福。", "心中有爱，世界温柔。",
"生活因善意而美丽。", "用笑容温暖他人，也温暖自己。", "每天都是新的奇迹。",
"坚持梦想，心怀希望。", "今天也要活得精彩。", "愿你每天都感受到爱的力量。",
"心中有光，世界就亮。", "微笑面对困难，勇敢前行。", "保持善良，生活更美好。",
"每天都是礼物，拥抱它。", "愿你收获满满的喜悦与幸福。", "温暖自己，温暖世界。",
"用心感受生活的温柔与美好。", "每天都是成长的机会。", "坚持热爱，勇敢追梦。",
"笑容是最好的疗愈。", "心怀希望，生活因你而精彩。", "今天也要保持好心情。",
"愿你被世界温柔以待。", "温暖的阳光照亮前路。", "每天都值得用心生活。",
"用心对待每一个今天。", "保持乐观，未来可期。", "努力的你最可爱。",
"心怀感恩，快乐随之而来。", "微笑是生活最美的语言。", "愿你每天都有小幸运。",
"坚持梦想，不惧风雨。", "温柔以待自己，也温柔对待他人。", "今天也要加油哦！",
"心中有爱，生活因你而温暖。", "每天都是新的开始，勇敢前行。", "阳光总在风雨后。",
"感受生活的美好与温暖。", "愿你笑容常在，心怀希望。", "生活因努力而精彩。",
"微笑面对每一个挑战。", "保持热爱，追逐梦想。", "温柔是生活最美的力量。",
"今天也要善待自己，快乐每一天。", "心怀感恩，幸福自然来。", "每天都是礼物，珍惜它。",
"勇敢追梦，收获美好人生。", "愿你每天都能遇见小确幸。", "用心感受每一份温暖。",
"笑容如阳光，心情如春天。", "坚持努力，梦想成真。", "温柔以待生活，也温柔以待自己。",
"每天都是新的奇迹与希望。", "愿你收获满满的喜悦与幸福。", "心怀善意，世界更美好。",
"微笑面对生活，勇敢前行。", "保持乐观，幸福随之而来。", "今天也要活得精彩。"
]

# 柔和温暖色 + 浅蓝浅紫色列表（80个RGB）
warm_colors = [
    # 奶油色 / 淡米色
    (255, 245, 230), (255, 250, 240), (255, 248, 235), (255, 243, 220),
    (255, 240, 215), (255, 238, 220), (255, 235, 200), (255, 230, 210),
    (255, 225, 205), (255, 223, 200), (255, 220, 195), (255, 218, 190),
    
    # 柔粉色 / 桃色 / 淡紫色
    (255, 215, 220), (255, 220, 225), (255, 228, 230), (245, 230, 240),
    (240, 225, 240), (235, 220, 235), (230, 215, 230), (225, 210, 225),
    (220, 205, 220), (215, 200, 215), (210, 195, 210), (205, 190, 205),
    
    # 浅棕色 / 奶茶色 / 杏色
    (222, 184, 160), (210, 180, 165), (244, 164, 140), (238, 203, 173),
    (220, 190, 160), (210, 175, 145), (205, 165, 135), (200, 160, 130),
    (195, 155, 125), (190, 150, 120), (185, 145, 115), (180, 140, 110),
    
    # 浅蓝色
    (230, 240, 255), (220, 235, 255), (210, 230, 255), (200, 225, 255),
    (190, 220, 255), (180, 215, 255), (170, 210, 255), (160, 205, 255),
    (150, 200, 255), (140, 195, 255), (130, 190, 255), (120, 185, 255),
    
    # 浅紫色 / 薰衣草色
    (235, 230, 255), (230, 225, 255), (225, 220, 255), (220, 215, 255),
    (215, 210, 255), (210, 205, 255), (205, 200, 255), (200, 195, 255),
    (195, 190, 255), (190, 185, 255), (185, 180, 255), (180, 175, 255),
    
    # 淡金色 / 柔黄色
    (255, 245, 200), (255, 240, 190), (255, 235, 185), (255, 230, 180),
    (255, 225, 175), (255, 220, 170), (255, 215, 165), (255, 210, 160),
    (255, 205, 155), (255, 200, 150), (255, 195, 145), (255, 190, 140),
    
    # 过渡色 / 柔和混色
    (250, 240, 235), (245, 235, 230), (240, 230, 225), (235, 225, 220),
    (230, 220, 215), (225, 215, 210), (220, 210, 205), (215, 205, 200)
]




class Popup(QWidget):
    def __init__(self, message, color):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setFixedSize(300, 100)
        self.setWindowTitle("温馨提示")

        label = QLabel(message, self)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        label.setStyleSheet("color: #333; letter-spacing: 1px;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.addWidget(label)

        # 背景色及圆角效果
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(*color))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
        # 添加圆角阴影样式
        r, g, b = color
        self.setStyleSheet("""
            QWidget {{
                border-radius: 10px;
                background: rgba({}, {}, {}, 240);
            }}
        """.format(r, g, b))

        # 淡入动画
        self.setWindowOpacity(0)
        fade_in = QPropertyAnimation(self, b"windowOpacity")
        fade_in.setDuration(300)
        fade_in.setStartValue(0)
        fade_in.setEndValue(0.95)
        fade_in.setEasingCurve(QEasingCurve.InOutQuad)
        fade_in.start()
        self.fade_in = fade_in

        # 注：消失时间由 PopupGenerator 统一控制
        self.auto_close_timer = None

    def fade_out(self):
        """淡出动画"""
        fade_out = QPropertyAnimation(self, b"windowOpacity")
        fade_out.setDuration(500)
        fade_out.setStartValue(0.95)
        fade_out.setEndValue(0)
        fade_out.setEasingCurve(QEasingCurve.InOutQuad)
        fade_out.finished.connect(self.close)
        fade_out.start()
        self.fade_out = fade_out

    def closeEvent(self, event):
        if self in QApplication.instance().activePopups:
            QApplication.instance().activePopups.remove(self)
        super().closeEvent(event)

class PopupGenerator:
    def __init__(self):
        self.count = 0
        self.max_count = 150
        self.popups = []  # 保存所有弹框
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_popup)
        self.timer.start(200)  # 每 400ms 弹一个
        self.all_shown = False  # 标记是否全部显示完毕

    def show_popup(self):
        if self.count < self.max_count:
            msg = random.choice(messages)
            color = random.choice(warm_colors)
            popup = Popup(msg, color)
            self.popups.append(popup)

            # 获取屏幕大小，防止超出范围
            screen_rect = QApplication.desktop().availableGeometry()
            x = random.randint(0, max(0, screen_rect.width() - popup.width()))
            y = random.randint(0, max(0, screen_rect.height() - popup.height()))
            popup.move(x, y)
            popup.show()

            # 强制窗口置顶 macOS 
            popup.raise_()
            popup.activateWindow()

            QApplication.instance().activePopups.append(popup)
            self.count += 1
        else:
            self.timer.stop()
            self.all_shown = True
            QTimer.singleShot(5000, self.close_all_popups)

    def close_all_popups(self):
        for popup in self.popups:
            popup.fade_out()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.activePopups = []
    generator = PopupGenerator()
    sys.exit(app.exec_())
