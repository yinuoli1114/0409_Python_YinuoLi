#! /bin/bash
#
#$Authors$
#$Dates$
#$Revision: 69218 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e02/Lab01/finalize_grades.bash $
#$Id: finalize_grades.bash 69218 2014-09-18 00:58:51Z ee364e02 $
if [ $# != 1 ]
then
  echo "Usage: ./finalize_grades.bash <roster_file>"
exit 1
fi


assign_grades.bash $1
if [[ $? > 1 ]]
then
  echo "Error: assign_grades.bash"
exit 2
fi
if [ -e "$1".finalized ]
then
  echo "Output file "$1".finalized already exists"
exit 3
fi


touch "$1".finalized
fout="$1".finalized
while read line
do
  name=$(echo $line | cut -d' ' -f4 | cut -d'@' -f1)
  #echo "$name"
  score=$(echo $line | cut -d' ' -f5)
  #echo "$score"
  g=$(echo $line | cut -d' ' -f6)
  echo "$name $g" >> $fout



done < $1.grades




