//комментарий
#include <stdio.h>

int main() {
    printf("Hello! How are you?\n"); //комментарий
    printf("Result: %o, %x.\n", 10 + 5, 500 - 33);
//         <-               ->
//          форматная строка
    printf("String: %s.\n", "aaaaaa"); 
//                   ^
//              спецификатор
    printf("Hex->Oct: %o\n", 0x10);
    printf("Hex->Dec: %d\n", 0x10);
    printf("Oct->Dec: %d\n", 010);
//                           ^
//                 восьмеричный литерал
    
    int a;      //definition (определение)
//      ^
// идентификатор переменной
    a = 0x10;
    int b = 011;   //инициализация
    int d = 111, e = 222, f;
    printf("a: %d\n", a);
    printf("f: %d\n", f);
    a = 010;
    printf("a: %d\n", a);
    a = 3000000000;
    printf("a: %d\n", a);
    printf("sizeof a: %ld\n", sizeof a);
    long c = 3000000000;
    printf("c: %ld\n", c);
    printf("sizeof c: %ld\n", sizeof c);

    for(int i = 0; i < 5; i++) {
        printf("i: %d\n", i);
    }



    printf("\n");

    int N = 100;
    int s = 0;
    for(int i = 1; i <= N; i++) {
        s += i;
    }
    printf("%d\n", s);

    printf("\n");
    printf("%d\n", 5 / 3);
    printf("%d\n", -5 / 3);
    printf("%d\n", 5 % 3);
    printf("%d\n", -5 % 3);
    printf("%d\n", -9 % 8);
}
