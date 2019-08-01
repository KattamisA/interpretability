from functions.dip import *
from functions.generate_results import *

import os
import numpy as np
import torch as ch
import matplotlib.pyplot as plt

data_path = "data/robust_CIFAR"

train_labels = ch.cat(ch.load(os.path.join(data_path, "CIFAR_lab")))
num_iter = 5000
for i in range(10):
    image = cv2.imread(data_path + '/' + str(i) + '.png')[..., ::-1]
    save_path = 'results/Features/robust'
    output = dip(image, 'depth3', num_iter=num_iter, save=True, save_path=save_path, name=str(i))
    # generate_result_files(save_path, output, image, num_iter, str(i))
