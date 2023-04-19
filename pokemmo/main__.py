from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMainWindow, QGridLayout, QComboBox
from threading import Thread
from actions import pesca, checa_pokemon_e_contador_payday, checa_seta, checa_mapa_e_define_spot_payday, checa_mapa_e_define_spot_exp, checa_pokemon_e_contador_exp, sweet_scent
from time import sleep


class Worker(QObject):  # Cria um worker para poder manter o codigo em loop , pausar e encerrar
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.is_running = True
        self.farm_mode = "Exp Farm"

    @Slot()
    def run(self):  # Executa os scripts caso o worker esteja como True
        while self.is_running:
            if self.farm_mode == "Exp Farm":
                sleep(2)
                checa_mapa_e_define_spot_exp()
                sweet_scent()
                sleep(20)
                checa_pokemon_e_contador_exp()

            elif self.farm_mode == "Payday Farm":
                sleep(2)
                checa_mapa_e_define_spot_payday()
                pesca()
                checa_seta()
                checa_pokemon_e_contador_payday()

        self.finished.emit()


class MainWindow(QMainWindow):  # Define a Mainwindow
    def __init__(self):
        super().__init__()

        self.thread = None
        self.worker = None

        self.setup_ui()

    def setup_ui(self):  # Define as caracteristicas da Mainwindow
        self.setWindowTitle('Mini-Bot-PokeMMO')

        self.label = QLabel("Clique em Iniciar para Farmar :")
        self.label2 = QLabel("Escolha sua farm :")
        self.btn_start = QPushButton("Iniciar")
        self.btn_pause = QPushButton("Pausar")
        self.btn_stop = QPushButton("Encerrar")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Exp Farm", "Payday Farm"])

        grid = QGridLayout()
        grid.addWidget(self.label2, 0, 0, 1, 3)
        grid.addWidget(self.combo_box, 1, 0, 1, 3)
        grid.addWidget(self.label, 2, 0, 1, 3)
        grid.addWidget(self.btn_start, 3, 0)
        grid.addWidget(self.btn_pause, 3, 1)
        grid.addWidget(self.btn_stop, 3, 2)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)

        self.adjustSize()
        self.setFixedSize(280, 300)

    def start(self):  # Define o botão Iniciar
        self.btn_start.setEnabled(False)
        self.btn_pause.setEnabled(True)
        self.btn_stop.setEnabled(True)

        self.label.setText("Farm em execução...")

        self.worker = Worker()
        self.worker.farm_mode = self.combo_box.currentText()
        self.thread = Thread(target=self.worker.run)
        self.thread.start()

    def pause(self):  # Define o botão Pausar
        if self.worker.is_running:
            self.worker.is_running = False
            self.btn_pause.setText("Continuar")
            self.label.setText("Farm pausado")
        else:
            self.worker.is_running = True
            self.btn_pause.setText("Pausar")
            self.label.setText("Farm em execução...")

    def stop(self):  # Define o botão Encerrar
        try:
            self.worker.is_running = False
            self.thread.join()
            self.btn_start.setEnabled(True)
            self.btn_pause.setEnabled(False)
            self.btn_pause.setText("Pausar")
            self.btn_stop.setEnabled(False)
            self.label.setText("Encerrando...")
            sleep(3)
            self.close()
        except:
            self.close()
