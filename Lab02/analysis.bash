#! /bin/bash
#
#$Authors$
#$Dates$
#$Revision: 69620 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e02/Lab02/analysis.bash $
#$Id: analysis.bash 69620 2014-10-02 01:06:08Z ee364e02 $

if [ $# != 1 ]
then
  echo "Usage: analysis.bash <input file>"
exit 1
fi
if [ ! -e "$1" ]
then 
  echo ""$1" is not a readable file."
exit 2
fi

while read -a a
do
  let i=0
  let sum=0
  let avg=0
  echo Read ${#a[*]} items
  
  echo ${#a[*]} 
  for ((k = 2; k <= ((${#a[*]}-2)); k++))
  do
    echo $k
    let sum=$sum+${a[$k]}
    echo "sum" $sum
  done
  echo $k
  avg=$(($sum / (($k-2))))
  echo "${a[0]} ${a[1]} scored an average of $avg"
done < $1
     
