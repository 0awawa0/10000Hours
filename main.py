import os
import random
from datetime import date
from PyQt5 import QtWidgets, QtGui
import stop_watch
import mainWindow_UI


class mainWindowApp(QtWidgets.QMainWindow,
                    mainWindow_UI.Ui_MainWindow):
    """Main menu application represents the main window that appears when user
    runs the program
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Here I remember today's date. I will need it later
        self.today = str(date.today())

        # This variable stores time a user has exercised today
        self.timeToday = 0

        # Here the program changes its cwd to ./data and will work here till
        # closed
        path = os.getcwd()
        data_path = path + os.sep + "data"

        # This variable contains the summary time of all exercises. It is being
        # recalculated every time the program starts
        self.timeSummary = 0

        # Here I check if data directory exists
        try:
            # If it's not, it is being created
            os.mkdir(data_path)
            os.chdir(data_path)
            with open("TodayTime.txt", 'w') as f:
                f.write(f"{self.today}\n0")
        except FileExistsError:
            # Else, I just change the cwd to it
            os.chdir(data_path)

        # Here I make a list of IDs. It contains 56-bit length numbers. Each
        # ID matches some exercise. Each ID is actually a filename with
        # information about exercise it matches.
        self.list_id = [i for i in os.listdir(data_path) if os.path.isfile(i)
                        and i.isnumeric()]

        # Here I make a dictionary which contains IDs as keys and exercise name
        # as value. So it looks like this:
        # Programming: 37215948465462277
        # Also I read every file and sum time from them with the summary time
        self.dict_id = {}
        for i in self.list_id:
            with open(i, "r") as f:
                lines = f.readlines()
                text = lines[0].strip()
                self.timeSummary += float(lines[1])
            self.dict_id[text.strip()] = i

            # I also create a button for every exercise with its name on it.
            btn = QtWidgets.QPushButton(text.strip())
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            btn.setFont(font)
            # And every button takes the object's name as exercise's ID
            btn.setObjectName(i)
            btn.clicked.connect(self.initSW)
            self.exercisesLayout.addWidget(btn)

        # The directory except of files with exercises data files contains also
        # TodayTime.txt. This file contains time user has exercised today and
        # today's date, of course.
        try:
            with open("TodayTime.txt", "r") as f:
                # So I read TodayTime.txt data and compare date in the file with
                # today's date. If they are equal, I change lblTimeToday text
                # to the time from the file and remember this time. Else, this
                # value remains 0.
                lines = f.readlines()
                d = lines[0].strip()
                if self.today == d:
                    self.timeToday = float(lines[1])
                    self.lblTimeToday.setText(
                        f"{self.timeToday // 60 // 60:02.0f}:"
                        f"{(self.timeToday // 60) % 60:02.0f}:"
                        f"{self.timeToday % 60:02.03f}"
                    )
        except FileNotFoundError:
            return

        # Here I connect buttons 'Add' and 'Delete' to their functions
        self.btnAdd.clicked.connect(self.add)
        self.btnDelete.clicked.connect(self.delete)

        self.lblSummaryTime.setText(f"{self.timeSummary // 60 // 60:02.0f}:"
                                    f"{(self.timeSummary // 60) % 60:02.0f}:"
                                    f"{self.timeSummary % 60:02.03f}")

    def add(self):
        """This function performs adding new exercises to the list
        """
        try:
            to_add = self.lineEditAdd.text()

            if to_add in list(self.dict_id.keys()):
                error = QtWidgets.QErrorMessage(self)
                error.showMessage("This exercise is already exists")
                return

            id = str(random.getrandbits(56))
            while id in self.list_id:
                id = random.getrandbits(56)
            with open(id, "w") as f:
                f.write(f"{to_add}\n0\n")

            self.dict_id[to_add.strip()] = id

            new_button = QtWidgets.QPushButton(to_add)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            new_button.setFont(font)

            new_button.setObjectName(id)
            new_button.clicked.connect(self.initSW)
            self.exercisesLayout.addWidget(new_button)
        except Exception:
            return

    def initSW(self):
        """This function initiates stopwatch window after user clicks button of
        the exercise
        """
        file = self.sender().objectName()
        window = stop_watch.StopWatchApp(file, self)
        window.show()
        self.hide()

    def delete(self):
        """This function performs deleting exercise from the list
        """
        try:
            name = self.lineEditDelete.text()
            id = self.dict_id[name]
            self.dict_id.pop(name)

            os.remove(id)
            btn = self.findChild(QtWidgets.QPushButton, id)
            btn.setParent(None)
            btn.deleteLater()

            self.list_id.remove(id)
        except Exception:
            return


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindowApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
