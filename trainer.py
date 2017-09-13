# encoding: utf-8
import tensorflow as tf
import settings
FLAGS = settings.FLAGS

import os
import re
import copy
from datetime import datetime
import time
from datasets import DataSet
import datasets

import numpy as np

def train(verbose=False):
    with tf.Graph().as_default():
        # global step number
        global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)
        dataset = DataSet()

        # get training set
        print("The number of training images is: %d" % (dataset.cnt_samples(FLAGS.traincsv)))
        images, labels = dataset.csv_inputs(FLAGS.traincsv, FLAGS.batch_size, distorted=True)

        # get test set
        test_cnt = 100
        images_test, labels_test = dataset.test_inputs(FLAGS.testcsv, test_cnt)

        # TODO create iteration of training


def main(argv=None):
    if tf.gfile.Exists(FLAGS.train_dir) and not FLAGS.fine_tune:
        print("Caution: train dir is already exists.")
    if not tf.gfile.Exists(FLAGS.train_dir):
        tf.gfile.MakeDirs(FLAGS.train_dir)
    train()


if __name__ == '__main__':
    tf.app.run()
