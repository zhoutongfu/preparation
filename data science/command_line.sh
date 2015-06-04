# split all files in a given folder
cd /Users/zhoutongfu/Desktop/0
for ((i = 0 ; i < 10 ; i++))
do
	mkdir $file /Users/zhoutongfu/Desktop/others/$i 
	for file in $(ls -p | grep -v / | head -100)
	do
		mv $file /Users/zhoutongfu/Desktop/others/$i/
	done
done


grep -v symbol # inverse grep 

# OR multi pattern match
grep "pattern1\|pattern2\|..." file

# AND multi pattern match
awk '/pattern1/ && /pattern2/' file

# write alias in .bash_profile at main directory ~, for example, write the following shortcut
alias cd124='cd /Users/zhoutongfu/Desktop/2015\ winter/cs\ 124/homework\ sets'



# export values, call another .sh

# at grader.sh
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P )
export SCRIPTPATH
sh index.sh

# at index.sh
java -Xmx400M -cp "$SCRIPTPATH/../classes" cs276.assignments.Index Basic $1 $2

# display txt side by side
pr -m -t one.txt two.txt

# shuffle lines of a text
cat input.txt | gshuf > output.txt

# shuffle using python
cat file | python -c "import random, sys; 
  random.seed(100); print ''.join(random.sample(sys.stdin.readlines(), 200))," \
  > 200lines.txt

# To Display Those Lines That Are Common to File1 and File2
# Type the command as follows:
# -1 : suppress lines unique to FILE1
# -2 : suppress lines unique to FILE2
# -3 : suppress lines that appear in both files
comm /path/to/file1/ /path/to/file2
comm -1 /path/to/file1/ /path/to/file2
comm -2 /path/to/file1/ /path/to/file2
comm -3 /path/to/file1/ /path/to/file2


# merge pdf files
# use pdftk: pdftk old1.pdf old2.pdf old3.pdf cat output new.pdf
# do it recursively: pdf  folder*/*.pdf cat output new.pdf
# e.g.,
pdftk week*/* output new.pdf
