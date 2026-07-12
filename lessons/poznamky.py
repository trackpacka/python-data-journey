import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QTextEdit, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt

class NoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Poznámky (OneNote klon)")
        self.setGeometry(100, 100, 800, 500)
        self.notes_dir = "notes"
        os.makedirs(self.notes_dir, exist_ok=True)
        self.init_ui()
        self.load_notes()

    def init_ui(self):
        # Tmavý režim
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(30, 30, 30))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(60, 60, 60))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.Highlight, QColor(90, 90, 90))
        dark_palette.setColor(QPalette.HighlightedText, Qt.white)
        self.setPalette(dark_palette)

        layout = QHBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setFixedWidth(200)
        self.list_widget.itemClicked.connect(self.load_note)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Consolas", 12))

        button_layout = QVBoxLayout()
        self.new_button = QPushButton("➕ Nová poznámka")
        self.new_button.clicked.connect(self.new_note)
        self.save_button = QPushButton("💾 Uložit")
        self.save_button.clicked.connect(self.save_note)
        self.delete_button = QPushButton("🗑️ Smazat")
        self.delete_button.clicked.connect(self.delete_note)

        for btn in [self.new_button, self.save_button, self.delete_button]:
            btn.setMinimumHeight(40)
            button_layout.addWidget(btn)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.text_edit)
        right_layout.addLayout(button_layout)

        layout.addWidget(self.list_widget)
        layout.addLayout(right_layout)
        self.setLayout(layout)

    def load_notes(self):
        self.list_widget.clear()
        for filename in os.listdir(self.notes_dir):
            if filename.endswith(".txt"):
                self.list_widget.addItem(filename)

    def load_note(self, item):
        filepath = os.path.join(self.notes_dir, item.text())
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            self.text_edit.setPlainText(content)

    def new_note(self):
        name, ok = QFileDialog.getSaveFileName(self, "Nová poznámka", self.notes_dir, "Textové soubory (*.txt)")
        if ok and name:
            base = os.path.basename(name)
            open(name, "w", encoding="utf-8").close()
            self.list_widget.addItem(base)
            self.list_widget.setCurrentRow(self.list_widget.count() - 1)
            self.text_edit.clear()

    def save_note(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            filepath = os.path.join(self.notes_dir, current_item.text())
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.text_edit.toPlainText())
            QMessageBox.information(self, "Uloženo", "Poznámka byla uložena.")
        else:
            QMessageBox.warning(self, "Chyba", "Není vybrána žádná poznámka.")

    def delete_note(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            reply = QMessageBox.question(self, "Potvrzení", f"Opravdu smazat '{current_item.text()}'?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                filepath = os.path.join(self.notes_dir, current_item.text())
                os.remove(filepath)
                self.list_widget.takeItem(self.list_widget.row(current_item))
                self.text_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec())