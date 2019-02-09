from PyQt5 import QtWidgets, Qt
import StopWatch_UI
import notes

TICK_TIME = 2**6


class StopWatchApp(QtWidgets.QMainWindow,
                   StopWatch_UI.Ui_MainWindow):
    """This class implements stopwatch application that performs time counting
    """
    def __init__(self, filename, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # This variable stores the filename of the exercise. The filename
        # application gets from the parent window.
        # The program reads file contains and initiate window's title and
        # stopwatch initial time
        self.filename = filename
        with open(filename, "r") as f:
            text = f.readlines()
            self.setWindowTitle(text[0].strip())
            self.time = float(text[1].strip())

        # This variable stores initial time to calculate time user has exercised
        # this time
        self.timeStart = self.time

        self.timer = Qt.QTimer()
        self.timer.setInterval(TICK_TIME)
        self.timer.timeout.connect(self.tick)

        self.btnStop.setEnabled(False)

        self.btnStart.clicked.connect(self.start)
        self.btnStop.clicked.connect(self.stop)
        self.btnNotes.clicked.connect(self.notes)

        self.seconds = self.time % 60
        self.minutes = (self.time // 60) % 60
        self.hours = self.time // 60 // 60
        self.lblHours.setText(f"{self.hours:02.0f}")
        self.lblMinutes.setText(f"{self.minutes:02.0f}")
        self.lblSeconds.setText(f"{self.seconds:02.03f}")

    def tick(self):
        """This function refreshes stopwatch time
        """
        self.time += TICK_TIME / 1000
        self.seconds = self.time % 60
        self.minutes = (self.time // 60) % 60
        self.hours = self.time // 60 // 60
        self.lblHours.setText(f"{self.hours:02.0f}")
        self.lblMinutes.setText(f"{self.minutes:02.0f}")
        self.lblSeconds.setText(f"{self.seconds:02.03f}")

    def start(self):
        """This function performs stopwatch start
        """
        self.timer.start()
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(True)

    def stop(self):
        """This function performs stopwatch stop
        """
        self.timer.stop()
        with open(self.filename, 'w') as f:
            f.write(f"{self.windowTitle()}\n{self.time}")
        with open("TodayTime.txt", 'w') as f:
            self.parent().timeToday += self.time - self.timeStart
            f.write(f"{self.parent().today}\n{self.parent().timeToday}")
            self.parent().lblTimeToday.setText(
                f"{self.parent().timeToday // 60 // 60:02.0f}:"
                f"{(self.parent().timeToday // 60) % 60:02.0f}:"
                f"{self.parent().timeToday % 60:02.03f}"
            )
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(False)

    def closeEvent(self, e):
        self.parent().show()

    def notes(self):
        """This function initiates notes window
        """
        notes.NotesApp(self).show()


def main():
    print("Couldn't be run as autonomous script")
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # window = StopWatchApp()
    # window.show()
    # app.exec_()


if __name__ == "__main__":
    main()
