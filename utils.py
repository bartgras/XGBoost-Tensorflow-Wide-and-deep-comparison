# import pandas as pd
# import numpy as np
from IPython.display import SVG
from keras.utils.visualize_util import model_to_dot

# Drawing helper
def draw_model_graph(model):
    return SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))    