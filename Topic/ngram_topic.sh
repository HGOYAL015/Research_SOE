read  file
echo $file > input.txt
python3 stam_let.py < input.txt > stammed_input.txt

python3 word.py > ngram.txt
python3 ../BXB.py > dekhi.txt 