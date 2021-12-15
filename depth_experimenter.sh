# This script runs through different depths for R and W and simulates games
MAX_DEPTH=3
MAX_ITER=2

for r in $(seq 1 $MAX_DEPTH)
do
for w in $(seq 1 $MAX_DEPTH)
do

RED=0
WHITE=0
DRAW=0
for i in $(seq 1 $MAX_ITER)
do

WINNER=$(python3 main.py $r $w)
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

echo "RED DEPTH:" $r
echo "WHITE DEPTH:" $w 
echo RED: $RED
echo WHITE: $WHITE
echo DRAW: $DRAW
echo ----------
echo

done
done
