#! /bin/bash
#
#$Authors$
#$Dates$
#$Revision: 69619 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e02/Lab02/sorting.bash $
#$Id: sorting.bash 69619 2014-10-02 00:17:56Z ee364e02 $

if [ $# != 1 ]
then
  echo "Usage: ./sorting.bash <input file>"
exit 1
fi
if [ ! -e "$1" ]
then 
  echo ""$1" is not a readable file."
exit 2
fi
echo "./sorting.bash "$1""
echo "Your choice are:"
echo "1) First 10 people"
echo "2) Last 5 names by highest zipcode"
echo "3) Address of 6th-10th by reverse e-mail"
echo "4) First 12 companies"
echo "5) Pick a number of people"
echo "6) Exit"
read -p "Your choice: " ch
touch fout.txt
fout=fout.txt
if [[ $ch == "1" ]]
then 
   i=0
   while read line
   do
     if [[ $i > 0 ]]
     then
        echo $line >> $fout
     fi
    let i=$i+1
    done < $1     
     
   sort -t "," -k7,7 -k5,5 -k2,2 -k1,1 $1 | head -n 10
fi


if [[ $ch == "2" ]]
then
  sort -t "," -nk8,8 $1 | cut -d"," -f1,2 | tail -n 5
fi

if [[ $ch == "3" ]]
then
  sort -t "," -rk11,11 $1 | cut -d"," -f4 | head -n 10 | tail -n 5
fi

if [[ $ch == "4" ]]
then
   sort -t "," -k3,3 $1 | cut -d"," -f3 | head -n 12
fi

if [[ $ch == "5" ]]
then
   read -p "Enter a number: " num
   sort -t "," -k2,2 -k 1,1 $1 | head -n $num
fi

if [[ $ch == "6" ]]
then
  echo "Have a nice day!"
fi
exit 0
