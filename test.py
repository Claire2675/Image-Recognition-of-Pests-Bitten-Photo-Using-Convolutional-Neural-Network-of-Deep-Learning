import tensorflow as tf
import pandas as pd

#from tensorflow.python.keras import backend as K
#Felix modify 20210417
import keras
from keras import backend as K

#from tensorflow.python.keras.models import load_model
#Felix modify 20210417
from keras.models import load_model

#from tensorflow.python.keras.preprocessing import image
#Felix modify 20210417
from keras.preprocessing import image


import sys
import numpy as np


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# 從參數讀取圖檔路徑
files = sys.argv[1:]

# 載入訓練好的模型
net = load_model('felix_new_model.h5')

cls_list = ['mos','pae','spider']

# 辨識每一張圖
for f in files:
    img = image.load_img(f, target_size=(160, 160))
    if img is None:
        continue
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    pred = net.predict(x)[0]
    top_inds = pred.argsort()[::-1][:5]
#print(f)
    for i in top_inds:
        print('    {:.3f};{}'.format(pred[i], cls_list[i]))
