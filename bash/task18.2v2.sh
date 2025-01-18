read n
s=0
while((n > 0))
do
    ((s += n % 10))
    ((n /= 10))
done
echo $s
