#!/bin/bash

echo "97100003.ASC" >> file1 && ./97100003.py >> file1 &
echo "98010008.ASC" >> file2 && ./98010008.py >> file2 &
echo "99060004.ASC" >> file3 && ./99060004.py >> file3 &
echo "99060013.ASC" >> file4 && ./99060013.py >> file4 &
echo "99060013.ASC" >> file5 && ./99060013.py >> file5 &
echo DONE



