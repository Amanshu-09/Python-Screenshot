import sys
from PyQt5.QtWidgets import *
from cls_SS import cls_SS

app = QApplication([])
mw = cls_SS()
mw.show()
sys.exit(app.exec_())