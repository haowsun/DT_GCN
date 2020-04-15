#!/bin/bash
for repeat in $(seq 10)
do
    echo "repeat: $repeat"
    python train.py --dataset DD_combine
done