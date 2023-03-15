import numpy as np
from logging import Logger

class NumberLogger(Logger):
	def __init__(self, file):
		self.file = file
	def log_nb(self, nb):
		self.log("INFO", np.format_float_scientific(nb))
		
if __name__ == "__main__":
	lg = NumberLogger()
	lg.log_nb(1.245)
