# -*- coding: utf-8 -*-
"""HELPER_FUNCTIONS.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MuyA6TD9rKkeoNdHb5eVEu3fQfQxsbYC
"""

import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
def plot_curves(history):
  '''
  Args: history of .fit() operation
  function: plots the train loss vs val loss and train accuracy vs val accuracy
  returns: none
  '''
  train_loss = history.history["loss"]
  val_loss = history.history["val_loss"]
  train_accuracy = history.history["accuracy"]
  val_accuracy = history.history["val_accuracy"]
  epochs = range(len(history.history["loss"]))
  plt.plot(epochs,train_loss,val_loss)
  plt.grid(True)
  plt.title("TRAINING LOSS VS VALIDATION LOSS")
  plt.legend(["TRAINING LOSS","VALIDATION LOSS"])
  plt.figure()
  plt.plot(epochs,train_accuracy,val_accuracy)
  plt.grid(True)
  plt.title("TRAINING ACCURACY VS VALIDATION ACCURACY")
  plt.legend(["TRAINING ACCURACY","VALIDATION ACCURACY"])

def plot_confusion_matrix(cm,class_names,figsize=(12,12)):
  '''
  Args: confusion matrix, list of classes and a tuple of the size of plot
  function: plots a confusion matrix using seaborn heatmap
  returns: none
  '''
  import seaborn as sns
  plt.figure(figsize=figsize)
  sns.heatmap(cm/np.sum(cm),
              annot=True,
              fmt='.2%',
              linewidths = 0.5,
              square=True,
              cbar = True,
              cmap = "Blues_r",
              xticklabels=class_names,
              yticklabels=class_names
              )
  plt.xlabel("PREDICET LABEL")
  plt.ylabel("ACTUAL LABEL")

def tensor_board_callback(dirname,experimentname):
  '''
  Args: name of the directory and experiment
  function: creates a tensorboard callback with the given names
  returns: tensorboard callback
  '''
  import datetime
  log_dir = dirname + '/' + experimentname + datetime.datetime.now().strftime("%d%m%Y-%H%M%S")
  tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)
  return tensorboard_callback

def unzip_data(dirname):
  '''
  Args: name of the zipfile
  function: unzips the file
  returns: none
  '''
  import zipfile
  zf = zipfile.ZipFile(dirname)
  zf.extractall()
  zf.close()

def walk_through(dir):
  '''
  Args: name of the directory
  function: wlaks through the entire file structure
  returns: none
  '''
  import os
  for root,dirname,files in os.walk(dir):
    print(f'THERE ARE {len(dirname)} SUB DIRECTORIES AND {len(files)} FILES IN THIS DIRECTORY')

