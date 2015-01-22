#! /bin/bash
#
#$Authors$
#$Dates$
#$Revision: 69587 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e02/Lab05/sort.bash $
#$Id: sort.bash 69587 2014-09-30 19:25:17Z ee364e02 $

while getopts f:b:-: thisopt
do
      case $thisopt in
       f)echo $OPTARG
       -)echo "${OPTARG}"
       *)echo "Invalid arg"
      esac
done
exit0
