from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFrame
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import base64
import sys

class MeraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mera")
        self.setStyleSheet("background-color: #121212; color: #ffffff;")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        title_font = QFont("Arial", 24, QFont.Bold)
        self.title_label = QLabel("Mera")
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.message_label = QLabel("Enter Message:")
        layout.addWidget(self.message_label)

        self.message_entry = QLineEdit()
        self.message_entry.setStyleSheet("""
            background-color: #333;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        layout.addWidget(self.message_entry)

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.setStyleSheet("""
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.setStyleSheet("""
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("Result:")
        layout.addWidget(self.result_label)

        self.result_entry = QLineEdit()
        self.result_entry.setStyleSheet("""
            background-color: #333;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        layout.addWidget(self.result_entry)

        self.setLayout(layout)

    def encrypt_message(self):
        message = self.message_entry.text()
        encrypted_message = base64.b64encode(message.encode()).decode()
        self.result_entry.setText(encrypted_message)

    def decrypt_message(self):
        encrypted_message = self.message_entry.text()
        decrypted_message = base64.b64decode(encrypted_message.encode()).decode()
        self.result_entry.setText(decrypted_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = MeraApp()
    window.show()

    sys.exit(app.exec_())
