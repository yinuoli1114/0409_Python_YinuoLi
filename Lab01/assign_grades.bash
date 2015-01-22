#! /bin/bash
#
#$Authors$
#$Dates$
#$Revision: 69212 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e02/Lab01/assign_grades.bash $
#$Id: assign_grades.bash 69212 2014-09-18 00:15:40Z ee364e02 $
#fout="roster.grades"

if [ $# != 1 ]
then
  echo "Usage: ./assign_grades.bash <roster_file>"
exit 1
fi
if [ ! -r "$1" ]
then
  echo ""$1" is not a readable file"
exit 2
fi
if [ ! -w . ]
then 
  echo "Current directory is not writable"
exit 2
fi

if [ -e "$1".grades ]
then
  echo "Output file "$1".grades already exists"
exit 2
fi

touch "$1".grades
fout="$1".grades

let avg=0
let vnum=0
while read line
do
  score=$(echo $line | cut -d' ' -f5)
  #echo "$score"
  if [[ $score>=90 ]]
  then
    echo "$score"
    g="A"
  elif [[ $score>=80 ]]
  then
    g="B"
  elif [[ $score>=70 ]]
  then
    g="C"
  elif [[ $score>=60 ]]
  then
    g="D"
  else
    g="F"
  fi
  #echo "$g"
  let avg=$avg+$score
  let vnum=$vnum+1 
  echo "$line $g" >> $fout

done < $1
let avg=$avg/$vnum
echo "Class average: $avg"

exit 0