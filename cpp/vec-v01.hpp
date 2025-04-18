#include <iostream>
#include <memory>
#include <utility>
#include <cmath>

#include "storage.hpp"

using std::cout;
using std::endl;
// hhi!!!

//template<typename T, typename U>
//class Vec;
//
//template<typename T, typename U>
//bool less(const Vec<T, U>& v1, const Vec<T, U>& v2) {
//    for(U i {}; i < v1.dim; i++) {
//        if(i >= v2.dim) return false;
//        if(v1.coords[i] > v2.coords[i]) return false;
//        if(v1.coords[i] < v2.coords[i]) return true;
//    }
//    return v1.dim != v2.dim;
//}

template<typename T = float, typename U = size_t>
class Vec {
    U dim;
    Storage<T, U> coords;
    static constexpr U DIM_DEFAULT = 2;

public:

    U size() const {
        return dim;
    }

    U capacity() const {
        return coords.capacity();
    }

    const T& at(U i) const {
        return coords[i];
    }

    T& at(U i) {
        return coords[i];
    }

    
    // Vec(U ddim = DIM_DEFAULT) : dim{ddim}, cap{dim}, coords{new T[ddim]{}} {
    //     cout << "Vec constructed at " << this << endl;
    // }

    Vec(U ddim = DIM_DEFAULT) : dim{ddim}, coords{ddim} {
        cout << "Vec constructed at " << this << endl;

        for(U i {}; i < dim; i++) {
            new(&coords[i]) T{};
        }
    }

//    Vec(const Vec& v) : Vec{v.dim} {  // Делегирование конструктора

//    TODO: разделить аллокацию и инициализацию массива coords

//    TODO: использовать placement new инициализация отдельных элементов массива,
//          (сейчас все сначала инициализируется дефолтными значениями, а затем
//          через присваивание копируются новые значения T, это неэффективно)
//
    Vec(const Vec& v) : dim{v.dim}, coords{v.dim} {
        cout << "Vec copy constructed at " << this << " from " << &v << endl;

        for(U i {}; i < dim; i++) {
            new(&coords[i]) T{v.coords[i]};
        }

    }

    template<typename TT, typename UU>
    Vec(const Vec<TT, UU>& v) : dim{v.size()}, coords{v.size()} {
        cout << "Vec template copy constructed at " << this << " from " << &v << endl;

        for(U i {}; i < dim; i++) {
            new(&coords[i]) T{static_cast<T>(v.at(i))};
        }
    }

    Vec(Vec&& v) : dim{v.dim}, coords{std::move(v.coords)} {
        cout << "Vec move constructed at " << this << " from " << &v << endl;
        
        v.dim = 0;
    }

    Vec& operator=(const Vec& v) {
        cout << "Vec copy assignment at " << this << " from " << &v << endl;

        Vec vv = v;
        std::swap(vv, *this);

        return *this;
    }

// swap(a, b):
// T x = move(a)
// a = move(b)
// b = move(x)
    Vec& operator=(Vec&& v) {
        cout << "Vec move assignment at " << this << " from " << &v << endl;

        swap(v.coords, coords);
        std::swap(dim, v.dim);

        return *this;
    }
        
//> Vec<T, U> Declarations
    double length();
    void fill(T x);
    void zero();
    void one();
    void scale(T k);
    void neg();
    void add(const Vec& v);
    void sub(const Vec& v);
    void resize(U s);
    void reserve(U c);
    void recap(U c);
    void shrink();

    template<typename V>
    void add(const V x);

    template<typename V>
    void sub(const V x);

    template<typename V>
    void rsub(const V x);

    T dot(const Vec& v);

    Vec<T, U> operator-();

    void operator+=(const Vec& v);

    template<typename V>
    void operator+=(const V x);

    void operator-=(const Vec& v);

    template<typename V>
    void operator-=(const V x);

    template<typename V>
    void operator*=(const V x);

    const T& operator[](U i) const;
    T& operator[](U i);
//<
//    friend bool less<>(const Vec& v1, const Vec& v2);

    template<typename TT, typename UU>
    friend bool less(const Vec<TT, UU>& v1, const Vec<TT, UU>& v2);

    template<typename TT, typename UU>
    friend TT dot(const Vec<TT, UU>& v1, const Vec<TT, UU>& v2);

//    friend bool less(const Vec& v1, const Vec& v2) {
//        for(U i {}; i < v1.dim; i++) {
//            if(i >= v2.dim) return false;
//            if(v1.coords[i] > v2.coords[i]) return false;
//            if(v1.coords[i] < v2.coords[i]) return true;
//        }
//        return v1.dim != v2.dim;
//    }

    void print(const char* name = nullptr) {
        if(name) {
            cout << name << " at ";
        }
        cout << this << " {\n";

        cout << "\tsize: " << dim << endl;
        cout << "\tcapacity: " << capacity() << endl;
        
        cout << "\tcoords: ";
        for(U i {}; i < dim; i++) {
            cout << coords[i] << '\t';
        }

        cout << "\n}\n";
    }

    ~Vec() {
        for(T *p = &coords[0]; p != &coords[0] + dim; ++p) {
            p->~T();
        }

        cout << "Vec destructed at " << this << endl;
    }
};

//TODO: .clear очишает вектор не меняя хранилище
// применить clear к имеющимся операциям
//> Vec<T, U>::METHODS

template<typename T, typename U>
inline void Vec<T, U>::resize(U s) {
    reserve(s);

    if(s < dim) {
        for(U i = s; i < dim; i++) {
            coords[i].~T();
        }
        dim = s;
    }
    else {
        for(U i = dim; i < s; i++) {
            new(&coords[i]) T{};
        }
        dim = s;
    }
}

template<typename T, typename U>
inline void Vec<T, U>::recap(U c) {
    if(c < dim) return;
        
    Storage<T, U> coords1{c};
    
    for(U i {}; i < dim; i++) {
        new(&coords1[i]) T{std::move(coords[i])};
    }

    for(T *p = &coords[0]; p != &coords[0] + dim; ++p) {
        p->~T();
    }

    swap(coords, coords1);
}

template<typename T, typename U>
inline void Vec<T, U>::reserve(U c) {
    if(c <= capacity()) return;

    recap(c);
}

template<typename T, typename U>
inline void Vec<T, U>::shrink() {
    recap(dim);
}

template<typename T, typename U>
double Vec<T, U>::length() {
    double l = 0;
    for(U i {}; i < dim; i++) {
        l += coords[i] * coords[i];
    }
    return sqrt(l);
}

template<typename T, typename U>
void Vec<T, U>::fill(T x) {
    for(U i {}; i < dim; i++) {
        coords[i] = x;
    }
}

template<typename T, typename U>
void Vec<T, U>::zero() {
    fill(T{});    
}


template<typename T, typename U>
void Vec<T, U>::one() {
    fill(T{1});    
}

template<typename T, typename U>
const T& Vec<T, U>::operator[](U i) const {
    return at(i);
}

template<typename T, typename U>
T& Vec<T, U>::operator[](U i) {
    return at(i);
}

//> Vec<T, U>::neg

template<typename T, typename U>
void Vec<T, U>::neg() {
    for(U i {}; i < dim; i++) {
        coords[i] = -coords[i];
    }
}

template<typename T, typename U>
Vec<T, U> Vec<T, U>::operator-() {
    Vec<T, U> v = *this;

    v.neg();
    return v;
}

//<
//> Vec<T, U>::add

template<typename T, typename U>
inline void Vec<T, U>::add(const Vec<T, U>& v) {
    for(U i {}; i < dim; i++) {
        coords[i] += v.coords[i];
    }
}

template<typename T, typename U>
template<typename V>
inline void Vec<T, U>::add(const V x) {
    for(U i {}; i < dim; i++) {
        coords[i] += x;
    }
}

template<typename T, typename U>
void Vec<T, U>::operator+=(const Vec<T, U>& v) {
    add(v);
}

template<typename T, typename U>
template<typename V>
void Vec<T, U>::operator+=(const V x) {
    add(x);
}

//<
//> Vec<T, U>::sub 

template<typename T, typename U>
inline void Vec<T, U>::sub(const Vec<T, U>& v) {
    for(U i {}; i < dim; i++) {
        coords[i] -= v.coords[i];
    }
}

template<typename T, typename U>
template<typename V>
inline void Vec<T, U>::sub(const V x) {
    for(U i {}; i < dim; i++) {
        coords[i] -= x;
    }
}

template<typename T, typename U>
template<typename V>
inline void Vec<T, U>::rsub(const V x) {
    for(U i {}; i < dim; i++) {
        coords[i] = x - coords[i];
    }
}

template<typename T, typename U>
void Vec<T, U>::operator-=(const Vec<T, U>& v) {
    sub(v);
}

template<typename T, typename U>
template<typename V>
void Vec<T, U>::operator-=(const V x) {
    sub(x);
}

//<
//> Vec<T, U>::scale

template<typename T, typename U>
inline void Vec<T, U>::scale(T k) {
    for(U i {}; i < dim; i++) {
        coords[i] *= k;
    }
}

template<typename T, typename U>
template<typename V>
void Vec<T, U>::operator*=(const V x) {
    scale(x);
}

//<
//<
//> Vec<T, U> HELPERS

template<typename T, typename U>
bool less(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    for(U i {}; i < v1.dim && i < v2.dim; i++) {
        T x1 {v1.coords[i]};
        T x2 {v2.coords[i]};
        if(x1 != x2) return x1 < x2;
    }
    return v1.dim < v2.dim;
}

template<typename T, typename U>
Vec<T, U> scale(Vec<T, U> v, T k) {
    int a;
    cout << &a << endl;
    v.scale(k);
    return v;   //NRVO
}

//> Vec<T, U> helper add()

template<typename T, typename U>
inline Vec<T, U> add(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    Vec<T, U> v = v1;

    v.add(v2);
    return v;
}

template<typename T, typename U, typename V>
inline Vec<T, U> add(const Vec<T, U>& v, const V x) {
    Vec<T, U> vv = v;

    vv.add(x);
    return vv;
}

template<typename T, typename U, typename V>
inline Vec<T, U> add(const V x, const Vec<T, U>& v) {
    Vec<T, U> vv = v;

    vv.add(x);
    return vv;
}

template<typename T, typename U, typename V>
Vec<T, U> operator+(const Vec<T, U>& v, const V x) {
    return add(v, x);
}

template<typename T, typename U, typename V>
Vec<T, U> operator+(const V x, const Vec<T, U>& v) {
    return add(x, v);
}

template<typename T, typename U>
Vec<T, U> operator+(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    return add(v1, v2);
}

//<
//> Vec<T, U> helper sub()

template<typename T, typename U>
Vec<T, U> sub(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    Vec<T, U> v = v1;

    v.sub(v2);
    return v;
}

template<typename T, typename U, typename V>
Vec<T, U> operator-(const Vec<T, U>& v, const V x) {
    Vec<T, U> vv = v;

    vv.sub(x);
    return vv;
}

template<typename T, typename U, typename V>
Vec<T, U> operator-(const V x, const Vec<T, U>& v) {
    Vec<T, U> vv = v;

    vv.rsub(x);
    return vv;
}

template<typename T, typename U>
Vec<T, U> operator-(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    return sub(v1, v2);
}

//<
//> Vec<T, U> helper scale/dot()

template<typename T, typename U>
T dot(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    T sp {};
    for(U i {}; i < v1.dim; i++) {
        sp += v1.coords[i] * v2.coords[i];
    }
    return sp;
}

template<typename T, typename U, typename V>
Vec<T, U> operator*(const Vec<T, U>& v, const V x) {
    Vec<T, U> vv = v;

    vv.scale(x);
    return vv;
}

template<typename T, typename U, typename V>
Vec<T, U> operator*(const V x, const Vec<T, U>& v) {
    Vec<T, U> vv = v;

    vv.scale(x);
    return vv;
}

template<typename T, typename U>
T operator*(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    return dot(v1, v2);
}

//<
//<

