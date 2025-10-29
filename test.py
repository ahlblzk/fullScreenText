from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
label = QLabel("你好，世界！")
label.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
label.resize(300, 100)
label.show()
sys.exit(app.exec_())
