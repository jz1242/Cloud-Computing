#! /bin/bash

cat mr.data | python ./01/map.py | sort | python ./01/reduce.py  | tee pr1.txt >> spam.txt
cat mr.data | python ./02/map_2.py | sort | python ./02/reduce_2.py  > pr2.txt
cat mr.data | python ./03/map_3.py | sort | python ./03/reduce_3.py | sort -n -r  > pr3.txt
cat mr.data | python ./04/map_4.py | sort | python ./04/reduce_4.py | sort -n -r  > pr4.txt
cat mr.data | python ./05/map_5.py | sort | python ./05/reduce_5.py | sort -n -r  > pr5.txt