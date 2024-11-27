import numpy as np
import matplotlib.pyplot as plt

class XBarChart:
    def __init__(self, samples, A2):
        self.samples = samples
        self.A2 = A2
        self.means = []  # Médias das amostras
        self.amplitudes = []  # Amplitudes das amostras
        self.center_line = 0  # Média geral (CL)
        self.lsc = 0  # LSC
        self.lic = 0  # LIC
    
    def calculate_means_and_ranges(self):
        """Calcula as médias e as amplitudes das amostras."""
        for sample in self.samples:
            self.means.append(np.mean(sample))
            self.amplitudes.append(np.max(sample) - np.min(sample))
    
    def calculate_control_limits(self):
        """Calcula a linha central, LSC e LIC."""
        self.center_line = np.mean(self.means)  # Média geral
        mean_range = np.mean(self.amplitudes)  # Amplitude média
        self.lsc = self.center_line + self.A2 * mean_range
        self.lic = self.center_line - self.A2 * mean_range
    
    def plot(self):
        """Plota o gráfico X-barra."""
        if not self.means or not self.lsc or not self.lic:
            raise ValueError("É necessário calcular os limites antes de plotar.")
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.means, marker='o', label='Médias das Amostras')
        plt.axhline(self.center_line, color='green', linestyle='--', label='Linha Central (CL)')
        plt.axhline(self.lsc, color='red', linestyle='--', label='Limite Superior de Controle (LSC)')
        plt.axhline(self.lic, color='red', linestyle='--', label='Limite Inferior de Controle (LIC)')
        plt.title("Gráfico X-barra")
        plt.xlabel("Subgrupo")
        plt.ylabel("Média")
        plt.legend()
        plt.grid(True)
        plt.show()

class RChart:
    def __init__(self, samples, D3, D4):
        self.samples = samples
        self.D3 = D3
        self.D4 = D4
        self.ranges = []  # Armazena as amplitudes dos subgrupos
        self.center_line = 0  # LC
        self.lsc = 0  # LSC
        self.lic = 0  # LIC

    def calculate_ranges(self):
        """
        Calcula as amplitudes (máximo - mínimo) para cada subgrupo.
        """
        self.ranges = [max(sample) - min(sample) for sample in self.samples]

    def calculate_control_limits(self):
        """
        Calcula a linha central, LSC e LIC com base nas amplitudes e nos coeficientes D3 e D4.
        """
        self.center_line = np.mean(self.ranges)  # Amplitude média
        self.lsc = self.D4 * self.center_line
        self.lic = max(0, self.D3 * self.center_line)  # LIC não pode ser negativo

    def plot(self):
        """
        Plota o gráfico R com as amplitudes, linha central e limites de controle.
        """
        if not self.ranges or not self.center_line:
            raise ValueError("Certifique-se de calcular os limites antes de plotar.")

        # Plotando as amplitudes dos subgrupos
        plt.plot(self.ranges, marker='o', label='Amplitude dos Subgrupos', color='blue')

        # Linha central (amplitude média)
        plt.axhline(self.center_line, color='green', linestyle='--', label='Linha Central (CL)')

        # Limites de controle
        plt.axhline(self.lsc, color='red', linestyle='--', label='Limite Superior de Controle (LSC)')
        plt.axhline(self.lic, color='red', linestyle='--', label='Limite Inferior de Controle (LIC)')

        plt.title("Gráfico R")
        plt.xlabel("Subgrupo")
        plt.ylabel("Amplitude (R)")
        plt.legend()
        plt.grid(True)
        plt.show()