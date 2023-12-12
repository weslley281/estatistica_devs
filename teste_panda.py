try:
    import pandas as pd
    print("Pandas está instalado. Versão:", pd.__version__)
except ImportError:
    print("Pandas não está instalado. Por favor, instale usando 'pip install pandas'.")
