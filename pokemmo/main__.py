from PySide6.QtCore import QObject, Signal, Slot, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QMainWindow, QGridLayout, QComboBox
from PySide6.QtGui import QPixmap, QMovie, QFont
from threading import Thread
from actions import pesca, checa_pokemon_e_contador_payday, checa_seta, checa_mapa_e_define_spot_payday, checa_mapa_e_define_spot_exp, checa_pokemon_e_contador_exp, sweet_scent
from time import sleep
from buttons import Button
import time


class Worker(QObject):  # Cria um worker para poder manter o codigo em loop , pausar e encerrar
    finished = Signal()
    media_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.is_running = True
        self.farm_mode = ""
        self.total_farm = 0
        self.tempo_decorrido = 0
        self.tempo_decorrido_min = 0

    @Slot()
    def run(self):  # Executa os scripts caso o worker esteja como True
        start_time = time.time()

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

            self.tempo_decorrido = time.time() - start_time
            self.tempo_decorrido_min = self.tempo_decorrido / 60
            self.media_changed.emit(self.calculate_media())

        self.finished.emit()

    def calculate_media(self):
        kph = (self.tempo_decorrido * 16) / 1000
        return f"Média: {kph:.2f}k/h \nTempo: {self.tempo_decorrido_min:.2f} minutos"


class MainWindow(QMainWindow):  # Define a Mainwindow
    def __init__(self):
        super().__init__()

        self.thread = None
        self.worker = None

        self.setup_ui()

    def setup_ui(self):  # Define as caracteristicas da Mainwindow
        gengar = QPixmap('pokemmo/files/gengar.png')
        pokemon_emerald = QMovie('pokemmo/files/pokemon_emerald.gif')
        lucario = QPixmap('pokemmo/files/lucario.png')
        font = QFont('Arial Black', 12, QFont.Bold)
        font2 = QFont('Arial Black', 10, QFont.Bold)

        self.setWindowTitle('Mini-Bot-PokeMMO')

        self.media_farm = QLabel("Média: 0 \nTempo: 0")
        self.media_farm.setFont(font2)
        self.label = QLabel("Clique em Iniciar para Farmar :")
        self.label.setFont(font)
        self.label2 = QLabel("Escolha sua farm :")
        self.label2.setFont(font)
        self.lucario = QLabel()
        self.lucario.setPixmap(lucario)
        self.gengar = QLabel()
        self.gengar.setPixmap(gengar)
        self.pokemon_emerald = QLabel()
        self.pokemon_emerald.setMovie(pokemon_emerald)
        pokemon_emerald.start()
        pokemon_emerald.setPaused(True)
        self.btn_start = Button("Iniciar")
        self.btn_pause = Button("Pausar")
        self.btn_stop = Button("Encerrar")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Exp Farm", "Payday Farm"])

        grid = QGridLayout()
        grid.addWidget(self.label2, 0, 0, 1, 2)
        grid.addWidget(self.gengar, 0, 2)
        grid.addWidget(self.combo_box, 1, 0, 1, 2)
        grid.addWidget(self.label, 2, 0, 1, 3)
        grid.addWidget(self.lucario, 2, 2)
        grid.addWidget(self.pokemon_emerald, 3, 0, 1, 2)
        grid.addWidget(self.media_farm, 3, 2)
        grid.addWidget(self.btn_start, 4, 0)
        grid.addWidget(self.btn_pause, 4, 1)
        grid.addWidget(self.btn_stop, 4, 2)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)

        self.adjustSize()
        self.setFixedSize(430, 500)

    def update_media_label(self, media):
        self.media_farm.setText(media)

    def start(self):  # Define o botão Iniciar
        self.btn_start.setEnabled(False)
        self.btn_pause.setEnabled(True)
        self.btn_stop.setEnabled(True)

        self.label.setText("Farm em execução...")

        self.worker = Worker()
        self.worker.farm_mode = self.combo_box.currentText()
        self.worker.media_changed.connect(self.update_media_label)
        self.thread = Thread(target=self.worker.run)
        self.thread.start()
        self.pokemon_emerald.movie().setPaused(False)

    def pause(self):  # Define o botão Pausar
        if self.worker.is_running:
            self.worker.is_running = False
            self.btn_pause.setText("Continuar")
            self.label.setText("Farm pausado!!")
            self.pokemon_emerald.movie().setPaused(True)
        else:
            self.worker.is_running = True
            self.btn_pause.setText("Pausar")
            self.label.setText("Farm em execução...")
            self.pokemon_emerald.movie().setPaused(False)

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
#aaaaaaaaaaaaaaaaa