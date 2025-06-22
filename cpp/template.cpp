#include <iostream>

using namespace std;

template<typename T = int, typename U = int, int N = 123>     //template class (primary template)
struct Point {
    T x, y, z;
    U index {N};

    void print();

};

template<typename T>     //template class (partial specialization)
struct Point<T*> {
    T *px, *py, *pz;

    void print();

};

template<>     //template class (complete specialization)
struct Point<char> {
    char x;

    void print();
//    void print() {
//        cout << this << " {\n";
//        cout << "\tx: " << (int)x << endl;
//        cout << "}\n";
//    }
};

template<typename T, typename U, int N>     //template method
void Point<T, U, N>::print() {
    cout << this << " {\n";
    cout << "\tx: " << x << "\n\ty: " << y << "\n\tz: " << z << endl;
    cout << "\tindex: " << index << endl;
    cout << "}\n";
}

template<typename T>     //template method
void Point<T*>::print() {
    cout << this << " {\n";
    cout << "\tx: " << *px << "\n\ty: " << *py << "\n\tz: " << *pz << endl;
    cout << "}\n";
}

void Point<char>::print() {
    cout << this << " {\n";
    cout << "\tx: " << (int)x << endl;
    cout << "}\n";
}

template<typename T>    //template function
void f(T n) {
    cout << sizeof(T) << endl;
    cout << n << endl;
}

template<typename T>    //template function
void f(T* p) {
    cout << "pointer: " << sizeof(T) << endl;
    cout << p << endl;
}

//template<>    //template function
void f(double p) {
    cout << "double: " << sizeof(double) << endl;
    cout << p << endl;
}

template<int N>     //template alias
using pfi_t = Point<float, int, N>;

template<typename... Args>
void g(Args... args) {
    cout << sizeof...(Args) << endl;
    cout << sizeof...(args) << endl;

    (cout << ... << args) << endl;
//  ((((cout << arg1) << arg2) << arg3) ... << argN)
}

template<typename... Args>
auto gs(Args... args) {
    return (... + args);    // fold expression (C++17)
//  return (((arg1 + arg2) + arg3) ... + argN);
}

template<typename T>
void print(T arg);

template<typename T, typename... Args>
void print(T firstArg, Args... args);

template<typename... Args>
void g1(Args... args) {
    print(args * args...);
}

template<typename T>
void print(T arg) {
    cout << arg << endl;
}

template<typename T, typename... Args>
void print(T firstArg, Args... args) {
    print(firstArg);
    print(args...);
}

//void print() {
//}
//
//template<typename T, typename... Args>
//void print(T firstArg, Args... args) {
//    cout << firstArg << endl;
//    print(args...);
//}
    
int main() {
    Point<double> pd {1, 2, 3};   
    cout << pd.x << endl;
    cout << pd.index << endl;
//    cout << typeid(p.x).name() << endl;

//    long l = 13;
    int l = 13;
    Point<int> pi {3, 4, 6, l};
    cout << pi.y << endl;
    cout << pi.index << endl;
    pi.print();

    Point<int, float> pif {1, 4, 12, 20.3};
    cout << pif.index << endl;

    using pfi44_t = Point<float, int, 44>;

    pfi_t<44> pfi44 {1, 2, 5};
    cout << pfi44.index << endl;
    
    Point<> p {3, 2, 4, 1};
    cout << p.y << endl;
    cout << p.index << endl;

    Point p2 = p; //CTAD

    short n {123};
    f<>(n);     // FTAD
    f(n);     // FTAD
    int *pl = &l;
    f(pl);
    f(123.);

    Point<int*> pp {pl, pl, pl};
    Point<char> pc {(char)12};
    pp.print();
    pc.print();

    g(12, 11., "abc"/*, Point<>{1, 2, 3}*/);
    cout << gs(12, 2., 34) << endl;
    print(12, 11., "123", "1");

    cout << "g1: " << endl;
    g1(1, 10, 100.);
}
