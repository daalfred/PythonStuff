#!/bin/bash
for i in {500..11500..500};
do
	python q-sequence.py $i
done
