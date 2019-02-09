import random
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
import Notes_UI


class NotesApp(QtWidgets.QMainWindow,
               Notes_UI.Ui_MainWindow):
    """This class implements application that performs notes saving
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.filename = self.parent().filename
        with open(self.filename, "r") as f:
            lines = f.readlines()
            self.notes = lines[2:]

        self.list_id = []

        for i in self.notes:
            splited = i.split("|")
            note_ID = splited[0]
            self.list_id.append(note_ID)
            date = splited[1]
            text = splited[2]
            note_text = f"ID: {note_ID}|{date}\n{text}\n"

            new_note = QtWidgets.QLabel()
            new_note.setWordWrap(True)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            new_note.setFont(font)

            new_note.setText(f"{note_text}")
            new_note.setObjectName(note_ID)
            self.notesLayout.addWidget(new_note)

        self.btnAdd.clicked.connect(self.add)
        self.btnDelete.clicked.connect(self.delete)

    def add(self):
        """This function performs adding new notes
        """
        try:

            text = self.textEditAdd.toPlainText()

            id = str(random.getrandbits(32))
            while id in self.list_id:
                id = random.getrandbits(32)
            with open(self.filename, "a") as f:
                f.write(f"{id}|{datetime.now()}|{text}\n")

            new_note = QtWidgets.QLabel()
            new_note.setWordWrap(True)
            new_note.setText(f"ID: {id}|{datetime.now()}\n{text}\n")
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            new_note.setFont(font)

            new_note.setObjectName(id)
            self.notesLayout.addWidget(new_note)
        except Exception:
            return

    def delete(self):
        """This function performs deleting notes
        """
        try:
            id = self.lineEditDelete.text()
            with open(self.filename, "r") as f:
                text = f.readlines()
            notes = text[2:]
            data = text[:2]

            for i in range(len(notes)):
                if notes[i].split("|")[0] == id:
                    notes.pop(i)
                    break
            with open(self.filename, "w") as f:
                to_write = ''.join(data+notes)
                f.write(to_write)

            note = self.findChild(QtWidgets.QLabel, id)
            note.setParent(None)
            note.deleteLater()
            self.list_id.remove(id)
        except Exception:
            return


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = NotesApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
