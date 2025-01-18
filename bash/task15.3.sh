N=99
s=0
for((i = 1; i <= N; i += 2)); do
#    s=$((s + i))
    ((s += i))
done
echo $s
