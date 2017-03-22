# Comparison of different models

* TFLearn based wide and deep model (code copied from https://www.tensorflow.org/tutorials/wide_and_deep and adapted to )

* TFLearn wide and deep re-implemented in Keras

* XGBoost implementation



# Results

* TFLearn wide and deep model - similarly to results from TF tutorial has accuracy is 84.5%

* XGBoost - best accuracy is 86.1%

* TFLearn wide and deep re-implemented in Keras - best accuracy is 85.1%


# Notes

* If you want to test it by yourself, download the data using TFLearn notebook

* Keras version skipped tf.contrib.layers.crossed_column features. Implementing them could further improve accuracy


# Summary

* This type of "tabular" based dataset is still easiest to implement using XGBoost

* Keras version was implemented using one-hot encoddings and separately embeddings. Surprisingly the one-hot encoding version achieved better accuracy 

* Probably when given more data, with more options in categorical columns ("workclass", "education", "marital_status" etc.) both TFLearn wide and deep and Keras embedding versions would perform better than XGBoost version.


**Check notebooks for details**
