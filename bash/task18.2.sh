N=334
s=0
n=$N
while((n > 0))
do
    ((s += n % 10))
    ((n /= 10))
done
echo $s
