# -*- coding: utf-8 -*-
"""HELPER_FUNCTIONS.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MuyA6TD9rKkeoNdHb5eVEu3fQfQxsbYC
"""

import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import random
import os
import matplotlib.image as mpimg 
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
    
    
def plot_curves(history):
  '''
  Args: history of model.fit
  function: plots the loss and accuracy curves for training and validation data
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


def random_img_plotter(dir,class_names):
  '''
  Args: name of the directory and list of class names
  function: plot a random image from the dataset
  returns: none
  '''
  c = random.choice(class_names)
  classdir = dir + "/" + c
  rand_img = random.choice(os.listdir(classdir))
  img = classdir + "/" + rand_img
  img = mpimg.imread(img)
  plt.imshow(img)
  plt.axis("off")
  plt.title(c)


def random_augumented_img_plotter(dir,class_names,aug_layer):
  '''
  Args: name of the directory, list of class names and aug_layer
  function: plot a random augumented image from the dataset
  returns: none
  '''
  c = random.choice(class_names)
  classdir = dir + "/" + c
  rand_img = random.choice(os.listdir(classdir))
  img = classdir + "/" + rand_img
  img = mpimg.imread(img)
  plt.imshow(img)
  plt.axis(False)
  plt.title(c)
  plt.figure()
  img = aug_layer(tf.expand_dims(img,axis=0))
  plt.imshow(tf.squeeze(img)/255.)
  plt.axis(False)
  plt.title(c)

    
def compare_history(historyo,historyl,initial_epochs = 5):
  '''
  Args: historyo-original history(eg: before fine tuning)
        history1-later history(eg: after fine tuning)
  function: plots the curves to compare histories
  returns: none
  '''
  import matplotlib.pyplot as plt
  #loss data
  original_training_loss = historyo.history["loss"]
  original_validation_loss = historyo.history["val_loss"]
  latest_training_loss = historyo.history["loss"] + historyl.history["loss"]
  latest_validation_loss = historyo.history["val_loss"] + historyl.history["val_loss"]
  #accuracy data
  original_training_acc = historyo.history["accuracy"]
  original_validation_acc = historyo.history["val_accuracy"]
  latest_training_acc = historyo.history["accuracy"] + historyl.history["accuracy"]
  latest_validation_acc = historyo.history["val_accuracy"] + historyl.history["val_accuracy"]
  #plotting
  plt.figure(figsize=(8,8))
  plt.subplot(2,1,1)
  plt.grid(True)
  plt.plot(latest_training_loss,label = "TRAINING LOSS")
  plt.plot(latest_validation_loss,label = "VALIDATION LOSS")
  plt.plot([initial_epochs-1,initial_epochs-1],plt.ylim(),label = "BEGGINGING OF FINE TUNING")
  plt.title("TRAINING LOSS VS VALIDATION LOSS ")
  plt.legend(loc = "upper right")
  plt.subplot(2,1,2)
  plt.grid(True)
  plt.plot(latest_training_acc,label = "TRAINING ACCURACY")
  plt.plot(latest_validation_acc,label = "VALIDATION ACCURACY")
  plt.plot([initial_epochs-1,initial_epochs-1],plt.ylim(),label = "BEGGINGING OF FINE TUNING")
  plt.title("TRAINING ACCURACY VS VALIDATION ACCURACY ")
  plt.legend(loc = "lower right")
