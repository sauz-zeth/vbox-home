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
    static constexpr int N_DEFAULT = 2;

public:

    int size() {
        return dim;
    }

    float& at(int i) {
        return coords[i];
    }

    Vec(U ddim = N_DEFAULT) : dim{ddim}, coords{new T[ddim]{}} {
        cout << "constructed at " << this << endl;
    }

    Vec(const Vec& v) : Vec{v.dim} {  // Делегирование конструктора
        cout << "copy constructed at " << this << " from " << &v << endl;
        for(int i = 0; i < dim; i++) {
            coords[i] = v.coords[i];
        }
    }

    Vec(Vec&& v) : dim{v.dim}, coords{v.coords} {
        cout << "move constructed at " << this << " from " << &v << endl;
        v.coords = nullptr;
    }

    double length();
    void fill(T x);
    void zero();
    void one();
    void scale(T k);
    void add(const Vec& v);

//    friend bool less<>(const Vec& v1, const Vec& v2);

    template<typename TT, typename UU>
    friend bool less(const Vec<TT, UU>& v1, const Vec<TT, UU>& v2);

//    friend bool less(const Vec& v1, const Vec& v2) {
//        for(U i {}; i < v1.dim; i++) {
//            if(i >= v2.dim) return false;
//            if(v1.coords[i] > v2.coords[i]) return false;
//            if(v1.coords[i] < v2.coords[i]) return true;
//        }
//        return v1.dim != v2.dim;
//    }
//
//
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
bool less(const Vec<T, U>& v1, const Vec<T, U>& v2) {
    for(U i {}; i < v1.dim && i < v2.dim; i++) {
        T x1 {v1.coords[i]};
        T x2 {v2.coords[i]};
        if(x1 != x2) return x1 < x2;
    }
    return v1.dim < v2.dim;
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
void Vec<T, U>::scale(T k) {
    for(U i {}; i < dim; i++) {
        coords[i] *= k;
    }
}

template<typename T, typename U>
void Vec<T, U>::add(const Vec<T, U>& v) {
    for(U i {}; i < dim; i++) {
        coords[i] += v.coords[i];
    }
}

template<typename T, typename U>
Vec<T, U> scale(Vec<T, U> v, T k) {
    int a;
    cout << &a << endl;
    v.scale(k);
    return v;   //NRVO
}



//template<typename U, typename T>
//Vec add(const Vec<U, T>& v1, const Vec<U, T>& v2) {
//    Vec<int, float> va{v1.size()};
//
//    for(int i = 0; i < v1.size(); i++) {
//        va.at(i) = v1.at(i) + v2.at(i)
//    }
//
//    return va;
//}

// .length() 
// .zero() (заполнение нулями)
// .one() (заполнение единицами)
// .scale(k) (умножение на число)
// .add(v) (сложение с вектором +=)
// scale(v, k)
// TODO:
// .dot(v) (скалярное произведение)
// .sub(v) (разность)
// add(v1, v2)
// sub(v1, v2)
// dot(v1, v2)

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

    cout << less(v5, v3) << endl;

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
