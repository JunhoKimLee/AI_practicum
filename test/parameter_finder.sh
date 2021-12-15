# This script finds optimal parameters for the eval func

# clear output file
rm -f output.csv
OUTPUT=output.csv

RED_H=1
WHITE_H=0

MAX_DEPTH=2
MAX_ITER=10

PARAM_RANGE=3

declare -i best_score=-99
declare -i h_1=0
declare -i h_2=0
declare -i h_3=0
declare -i h_4=0
declare -i h_5=0

for h1 in $(seq 1 $PARAM_RANGE)
do
for h2 in $(seq 1 $PARAM_RANGE)
do
for h3 in $(seq 1 $PARAM_RANGE)
do
for h4 in $(seq 1 $PARAM_RANGE)
do
for h5 in $(seq 1 $PARAM_RANGE)
do

declare -i red_score=0

for d in $(seq 1 $MAX_DEPTH)
do

RED=0
WHITE=0
DRAW=0

for i in $(seq 1 $MAX_ITER)
do
declare -i red_code=$RED_H\*10+$d
declare -i white_code=$WHITE_H\*10+$d

WINNER=$(python3 ../main.py $red_code $white_code $h1 $h2 $h3 $h4 $h5)
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

declare -i red_score=$red_score+$RED-$WHITE

done

if [ $red_score -gt $best_score ];
then
declare -i best_score=$red_score
declare -i h_1=$h1
declare -i h_2=$h2
declare -i h_3=$h3
declare -i h_4=$h4
declare -i h_5=$h5
fi

# write to file
echo $h1, $h2, $h3, $h4, $h5, $red_score >> $OUTPUT

done
done
done
done
done

echo Best score: $best_score
echo H1: $h_1
echo H2: $h_2
echo H3: $h_3
echo H4: $h_4
echo H5: $h_5

echo $h_1, $h_2, $h_3, $h_4, $h_5, $best_score >> $OUTPUT