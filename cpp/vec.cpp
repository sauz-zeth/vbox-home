#include <iostream>
#include <utility>
#include <cmath>

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
    T* coords; 
    static constexpr U DIM_DEFAULT = 2;

public:

    U size() const {
        return dim;
    }

    T& at(U i) const {
        return coords[i];
    }

    
    Vec(U ddim = DIM_DEFAULT) : dim{ddim}, coords{new T[ddim]{}} {
        cout << "constructed at " << this << endl;
    }

//    Vec(const Vec& v) : Vec{v.dim} {  // Делегирование конструктора
    Vec(const Vec& v) : dim{v.dim}, coords{new T[dim]} {
        cout << "copy constructed at " << this << " from " << &v << endl;
        for(int i = 0; i < dim; i++) {
            coords[i] = v.coords[i];
        }
    }

    template<typename TT, typename UU>
    Vec(const Vec<TT, UU>& v) : dim{v.size()}, coords{new T[dim]} {
        cout << "template copy constructed at " << this << " from " << &v << endl;
        for(int i = 0; i < dim; i++) {
            coords[i] = v.at(i);
        }
    }

    Vec(Vec&& v) : dim{v.dim}, coords{v.coords} {
        cout << "move constructed at " << this << " from " << &v << endl;
        v.coords = nullptr;
    }

    Vec& operator=(const Vec& v) {
        cout << "copy assignment at " << this << " from " << &v << endl;

        Vec vv = v;
        std::swap(vv, *this);

        return *this;
    }

// swap(a, b):
// T x = move(a)
// a = move(b)
// b = move(x)
    Vec& operator=(Vec&& v) {
        cout << "move assignment at " << this << " from " << &v << endl;

        std::swap(v.coords, coords);
        dim = v.dim;

        return *this;
    }
        

    double length();
    void fill(T x);
    void zero();
    void one();
    void scale(T k);
    void neg();
    void add(const Vec& v);
    void sub(const Vec& v);

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

    T& operator[](U i);

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
        
        cout << "\tcoords: ";
        for(int i = 0; i < dim; i++) {
            cout << coords[i] << '\t';
        }

        cout << "\n}\n";
    }

    ~Vec() {
        cout << "destructed at " << this << endl;
        delete[] coords;
    }
};

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
T& Vec<T, U>::operator[](U i) {
    return at(i);
}

/******************** Vec<T, U>::neg ********************/

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

/******************** Vec<T, U>::add ********************/

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

/******************** Vec<T, U>::sub ********************/

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

/******************** Vec<T, U>::scale ********************/

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

/******************** Vec<T, U> HELPERS ********************/

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

/******************** Vec<T, U> helper add() ********************/

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

/******************** Vec<T, U> helper sub() ********************/

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

/******************** Vec<T, U> helper scale/dot() ********************/

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

// TODO: .resize (указываю ему размер, если размер меньше, то массив обрезается, если размер больше, то массив увелчается и заполняется нулями)

int main() {
    Vec<float, int> v1{3};
    v1.at(0) = 23.3;
    v1.at(1) = 2.2;
    v1.print("v1");
    cout << v1.length() << endl;
    v1.zero();
    v1.print("v1");

    Vec v2 = v1;
    v2.print("v2");
    v2.at(1) = 3.3;
    v1.print("v1");

    Vec v3 = std::move(v1);
    v3.print("v3");
    v3.at(0) = 10;
    v2.print("v2");

    v3.one();
    v3.print("v3");

    v2.print("v2");
    v2.add(v2);
    v2.print("v2");
    v2.scale(10);
    v2.print("v2");

    v2.print("v2");
//    Vec v4 {scale(v2, float{23})};
    Vec v4 {scale<float>(v2, 23)};
    v4.print("v4");

    v2.at(0) = 1;
    v2.print("v2");
    v3.print("v3");

    Vec v5 {2};
    v5.one();
    v5.print("v5");

    Vec v6 = sub(v3, v2);
    v6.print("v3 sub v2");

    cout << "v3 dot v2: " << dot(v3, v2) << endl;
    
    v3.print("v3");
    v3 += v2;
    v3.print("v3 += v2");

    cout << less(v5, v3) << endl;

    v2.print("v2");
    
    Vec v7 = v3 + v2;
    v7.print("v3 + v2");

    Vec v8 = operator+<float>(v3, v2);
    v8.print("v3 + v2");

    v8 += 5;
    v8.print("v8 += 5");

    Vec v9 = v8 + 20;
    v9.print("v8 + 20");

    Vec v10 = 20 + v9;
    v10.print("20 + v9");

    v10 -= 20;
    v10.print("v10 = v9 - 20");

    Vec v11 = v8 - v10;
    v11.print("V8 - v10");

    Vec v12 = 20 - v10;
    v12.print("20 - v10");
    Vec v13 = -v12;
    v13.print("v13");

    Vec<int, int> v14 {};
    v14.at(0) = 4;
    v14.at(1) = 8;

    v14.print("v14");

    Vec<float, int> v15 = v14;
    v15.print("v15");

    Vec v16 = v15 * 3;
    v16.print("v16");

    cout << "v16 * v15: " << v16 * v15 << endl;

    v16 *= 0.5f;
    v16.print("v16");
    
    v16[0] = 20;
    cout << "v16[0] = 20: " << v16[0] << endl;
    cout << "v16[1]: " << v16[1] << endl;

    v15.print("v15");
    v16 = v15;
    v16.print("v16 = v15");

    v14.print("v14");
    v15 = std::move(v14);
    v15.print("v15 = move(v14)");

    v15 = Vec{3};
    v15.print("v15");

    v16 = v14 = v15;
    v16.print("v16");
    v16.print("v14");

    for(int i = 0; i < 3; i++) {
        cout << "block start \n";
        Vec<float, int> v3{4};
        v3.at(0) = 1;
        cout << "block end \n";
    }

    Vec<> *vv {new Vec<>[5]}; 
    cout << "vv allocated\n";

    delete[] vv;    // RAII!
}
