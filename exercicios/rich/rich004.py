# Inspecionando objetos utilizando a biblioteca rich

from rich import print
from rich import inspect

inspect(int) # Para ver o resumo
inspect(int, all=True) # Para ver os detalhes