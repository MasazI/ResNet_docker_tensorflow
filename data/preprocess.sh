#!/bin/bash


# Download 101 object categories data set
if [ ! -f "101_ObjectCategories.tar.gz" ]; then
    wget https://s3-us-west-2.amazonaws.com/deep-learning.datasection.co.jp/datasets/101_ObjectCategories.tar.gz
fi

if [ ! -d "./101_ObjectCategories/" ]; then
    tar zvxf 101_ObjectCategories.tar.gz
fi

# Generate .txt file
python3 create_examples_list.py
python3 relation_tag_to_id.py
