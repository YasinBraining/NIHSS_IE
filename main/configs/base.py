import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pathlib import Path
BASE_DIR = Path('./main')
config = {
    'data_dir': BASE_DIR / 'dataset',
    'ann_data': BASE_DIR / 'ann_data',
    'log_dir': BASE_DIR / 'output/log',
    'checkpoint_dir': BASE_DIR / 'output/checkpoints',
    'result_dir' : BASE_DIR / 'output/result',
    'figure_dir' : BASE_DIR / 'output/figure'
}