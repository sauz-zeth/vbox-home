#include <iostream>
#include <memory>
#include <utility>
#include <cmath>
#include <algorithm>

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
    using iterator = typename Storage<T, U>::iterator;
    U dim;
    Storage<T, U> coords;
    static constexpr U DIM_DEFAULT = 2;

    void realloc_safe(U c);

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

    iterator begin() {
        return coords.begin();
    }

    iterator end() {
        iterator it = coords.begin();
        std::advance(it, dim);
        
        return it;
    }

    const iterator cbegin() const {
        return coords.cbegin();
    }

    const iterator cend() const {
        const iterator it = coords.cbegin();
        std::advance(it, dim);

        return it;
    }
    

    
    // Vec(U ddim = DIM_DEFAULT) : dim{ddim}, cap{dim}, coords{new T[ddim]{}} {
    //     cout << "Vec constructed at " << this << endl;
    // }

    Vec(U ddim = DIM_DEFAULT) : dim{ddim}, coords{ddim} {
        cout << "Vec constructed at " << this << endl;

        std::uninitialized_fill(begin(), end(), T{});
    }
    //TODO: конструктор с initializer_list (исправить main)

//    Vec(const Vec& v) : Vec{v.dim} {  // Делегирование конструктора

    Vec(const Vec& v) : dim{v.dim}, coords{v.dim} {
        cout << "Vec copy constructed at " << this << " from " << &v << endl;

        std::uninitialized_copy(v.cbegin(), v.cend(), begin());
    }

    template<typename TT, typename UU>
    Vec(const Vec<TT, UU>& v) : dim{v.size()}, coords{v.size()} {
        cout << "Vec template copy constructed at " << this << " from " << &v << endl;

        std::uninitialized_copy(v.cbegin(), v.cend(), begin());
    }

    Vec(Vec&& v) : dim{v.dim}, coords{std::move(v.coords)} {
        cout << "Vec move constructed at " << this << " from " << &v << endl;
        
        v.dim = 0;
    }

    template<typename TT>
    Vec(std::initializer_list<TT> lst) : dim{lst.size()}, coords{dim} {
        cout << "Vec initializer_list constructed at " << this << endl;

        std::uninitialized_copy(lst.begin(), lst.end(), begin());
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
    void shrink();
    void clear();

    template<typename It>
    void assign(It first, It last);

    void assign(U n, T& value);

    template<typename TT>
    void insert(const iterator pos, TT&& value);

    template<typename It>
    void insert(iterator pos, It first, It last);

    template<typename TT>
    void push_back(TT&& value);

    iterator erase(const iterator pos);

    template<typename It>
    iterator erase(const It first, const It last);

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
        std::destroy(begin(), end());

        cout << "Vec destructed at " << this << endl;
    }
};

//> Vec<T, U>::METHODS

template<typename T, typename U>
inline void Vec<T, U>::clear() {
    std::destroy(begin(), end());
    dim = 0;
}

template<typename T, typename U>
template<typename It>
inline void Vec<T, U>::assign(It first, It last) {
    clear();
    reserve(last - first);
    std::uninitialized_copy(first, last, begin());
    dim = last - first;
}

template<typename T, typename U>
inline void Vec<T, U>::assign(U n, T& value) {
    reserve(n);
    std::uninitialized_fill(begin(), begin() + n, value);
    dim = n;
}

template<typename T, typename U>
inline void Vec<T, U>::resize(U s) {
    reserve(s);

    if(s < dim) {
        std::destroy(begin() + s, end());
    } else {
        std::uninitialized_fill(begin() + dim, begin() + s, T{});
    }

    dim = s;
}

template<typename T, typename U>
inline void Vec<T, U>::realloc_safe(U c) {
    if(c < dim) return;

    coords.realloc(c, begin(), end());
}

template<typename T, typename U>
inline void Vec<T, U>::reserve(U c) {
    if(c <= capacity()) return;

    realloc_safe(c);
}

template<typename T, typename U>
inline void Vec<T, U>::shrink() {
    realloc_safe(dim);
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
    std::fill(begin(), end(), x);
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
    for(T& vx : *this) {
        vx += x;
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

//> Vec<T, U>::insert


template<typename T, typename U>
template<typename TT>
inline void Vec<T, U>::insert(const iterator pos, TT&& value) {
    auto diff = pos - begin();
    reserve(dim + 1);
    pos = begin() + diff;

    ++dim;

    if(pos < end()) {
        coords.move_construct(pos, end(), pos + 1);
    }
    coords.reconstruct_at(pos < end() ? pos : end(), std::forward<TT>(value));
}

// TODO: const iterator Vec<T, U>::emplace(const iterator pos, Args... args)

template<typename T, typename U>
template<typename It>
inline void Vec<T, U>::insert(iterator pos, It first, It last) {
    auto size = last - first;

    auto diff = pos - begin();
    reserve(dim + size);
    pos = begin() + diff;

    if(pos < end()) {
        coords.move_construct(pos, end(), pos + size);
    }

    for (auto d_first = pos < end() ? pos : end(); first != last; ++first, ++d_first) {
        coords.reconstruct_at(d_first, *first);
    }

    dim += size;
}


//<

//> Vec<T, U>::push_back

template<typename T, typename U>
template<typename TT>
inline void Vec<T, U>::push_back(TT&& value) {
    insert(cend(), std::forward<TT>(value));
}


//<

//> Vec<T, U>::erase

template<typename T, typename U>
inline typename Vec<T, U>::iterator Vec<T, U>::erase(const iterator pos) {
    if(pos >= end()) return end();

    std::destroy_at(&*pos);
    coords.move_construct(pos + 1, end(), pos);
    dim--;

    return pos;
}

template<typename T, typename U>
template<typename It>
inline typename Vec<T, U>::iterator Vec<T, U>::erase(const It first, const It last) {
    if(first >= end()) return end();
    if(last >= end()) last = end();

    auto size = last - first;

    std::destroy(first, last);
    coords.move_construct(last, end(), first);
    dim -= size;

    return last;
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

