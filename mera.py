from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFrame, QHBoxLayout, QStatusBar, QMessageBox, QAction, QToolBar
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon
from PyQt5.QtCore import Qt
import base64
import sys
import pyperclip  # You'll need to install this package: pip install pyperclip

class MeraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mera - Message Encrypter and Decoder")
        self.setStyleSheet("background-color: #121212; color: #ffffff;")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()

        toolbar = QToolBar()
        help_action = QAction("Help", self)
        help_action.triggered.connect(self.show_help_dialog)
        toolbar.addAction(help_action)
        layout.addWidget(toolbar)

        title_font = QFont("Arial", 24, QFont.Bold)
        self.title_label = QLabel("Mera")
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setStyleSheet("color: #ffffff;")
        layout.addWidget(h_line)

        self.message_label = QLabel("Enter Message:")
        layout.addWidget(self.message_label)

        self.message_entry = QLineEdit()
        self.message_entry.setPlaceholderText("Enter your message here...")
        self.message_entry.setStyleSheet("""
            background-color: #333;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        layout.addWidget(self.message_entry)

        button_layout = QHBoxLayout()

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.setStyleSheet("""
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        button_layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.setStyleSheet("""
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        self.decrypt_button.clicked.connect(self.decrypt_message)
        button_layout.addWidget(self.decrypt_button)

        layout.addLayout(button_layout)

        self.result_label = QLabel("Result:")
        layout.addWidget(self.result_label)

        self.result_entry = QLineEdit()
        self.result_entry.setPlaceholderText("Result will appear here...")
        self.result_entry.setStyleSheet("""
            background-color: #333;
            color: #ffffff;
            padding: 10px;
            border-radius: 5px;
        """)
        layout.addWidget(self.result_entry)

        self.copy_button = QPushButton("Copy Result")
        self.copy_button.clicked.connect(self.copy_result)
        layout.addWidget(self.copy_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_fields)
        layout.addWidget(self.reset_button)

        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready")
        layout.addWidget(self.status_bar)

        self.setLayout(layout)

    def encrypt_message(self):
        message = self.message_entry.text()
        encrypted_message = base64.b64encode(message.encode()).decode()
        self.result_entry.setText(encrypted_message)
        self.status_bar.showMessage("Encryption Successful")

    def decrypt_message(self):
        encrypted_message = self.message_entry.text()
        try:
            decrypted_message = base64.b64decode(encrypted_message.encode()).decode()
            self.result_entry.setText(decrypted_message)
            self.status_bar.showMessage("Decryption Successful")
        except:
            self.status_bar.showMessage("Decryption Failed")

    def copy_result(self):
        pyperclip.copy(self.result_entry.text())
        self.status_bar.showMessage("Result Copied to Clipboard")

    def reset_fields(self):
        self.message_entry.clear()
        self.result_entry.clear()
        self.status_bar.showMessage("Fields Reset")

    def show_help_dialog(self):
        QMessageBox.information(self, "Help", "Hey Pika, you're going to be using this from now on most likely to communicate with me. Here's how to use it and how to stay safe: Simply enter the message you want to encrypt or decrypt in the 'Enter Message' field. Then, click the 'Encrypt' or 'Decrypt' button. The result will appear below. You can copy the result to your clipboard by clicking the 'Copy Result' button. To clear all fields, click the 'Reset' button. Stay safe!")

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
