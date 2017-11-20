import os
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from webview import WebviewWidget

_currentDir = os.path.dirname(os.path.realpath(__file__))
INDEX_HTML = os.path.join(_currentDir, 'static', 'app', 'index.html')
INDEX_URL = WebviewWidget.toFileURL(INDEX_HTML)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Example()
    webview = WebviewWidget(debug=True)
    webview.setUrl(INDEX_URL)
    webview.show()

    sys.exit(app.exec_())
