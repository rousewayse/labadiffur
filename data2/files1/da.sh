#!/bin/bash

echo "99060004.ASC" >> file1 && ./99060004.py >> file1 &
echo "99060009.ASC" >> file2 && ./99060009.py >> file2 &
echo "99060010.ASC" >> file3 && ./99060010.py >> file3 &
echo "99060013.ASC" >> file4 && ./99060013.py >> file4 &
echo "99060019.ASC" >> file5 && ./99060019.py >> file5 &
echo DONE



