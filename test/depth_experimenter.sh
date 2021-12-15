# This script runs through different depths for R and W and simulates games

# clear output file
rm -f output.csv
OUTPUT=output.csv

RED_H=1
WHITE_H=0

MAX_DEPTH=3
MAX_ITER=20

for r in $(seq 1 $MAX_DEPTH)
do
for w in $(seq 1 $MAX_DEPTH)
do

RED=0
WHITE=0
DRAW=0
for i in $(seq 1 $MAX_ITER)
do
declare -i red_code=$RED_H*10+$r
declare -i white_code=$WHITE_H*10+$w

WINNER=$(python3 ../main.py $red_code $white_code 2 1 2 3 2)
WINNER=${WINNER: -2:1}

#echo $WINNER

if [ "$WINNER" == "d" ];
then
RED=$((RED+1))
elif [ "$WINNER" == "e" ];
then
WHITE=$((WHITE+1))
elif [ "$WINNER" == "w" ];
then
DRAW=$((DRAW+1))
fi

done

# write to file
echo $r, $RED_H, $w, $WHITE_H, $RED, $WHITE, $DRAW >> $OUTPUT

echo "RED DEPTH:" $r
echo "RED HEURISTIC:" $RED_H
echo "WHITE DEPTH:" $w
echo "WHITE HEURISTIC:" $WHITE_H
echo RED: $RED
echo WHITE: $WHITE
echo DRAW: $DRAW
echo ----------
echo

done
done
