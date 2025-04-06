#include <iostream>
#include <memory>
#include <utility>

using std::cout;
using std::endl;

template<typename T = float, typename U = size_t>
class Storage {
    U cap;
    std::allocator<T> al;
    T *data;

public:
    U capacity() const {
        return cap;
    }

    const T& at(U i) const {
        return data[i];
    }

    T& at(U i) {
        return data[i];
    }

    Storage(U cap = U{}) : cap{cap}, data{al.allocate(cap)} {
        cout << "Storage constructed at " << this;
        cout << " with capacity " << cap << endl;
    }

    Storage(const Storage& st) = delete;
    Storage& operator=(const Storage& st) = delete;
    Storage& operator=(Storage&& st) = delete;

    Storage(Storage&& st) : cap{st.cap}, data{st.data} {
        cout << "Storage move constructed at " << this << " from " << &st << endl;

        st.data = al.allocate(U{});
        st.cap = 0;
    }

    ~Storage() {
        cout << "Storage destructed at " << this << endl;

        al.deallocate(data, cap);
    }

    const T& operator[](U i) const {
        return at(i);
    }

    T& operator[](U i) {
        return at(i);
    }

    class iterator {
        mutable T* ptr;
    public:
        using value_type = T;
        using pointer = T*;
        using reference = T&;
        using iterator_category = std::random_access_iterator_tag;
        using difference_type = std::ptrdiff_t;

        explicit iterator(T* pptr) : ptr{pptr} {}

        T& operator*() {return *ptr;}
        const T& operator*() const {return *ptr;}

        iterator& operator++() {ptr++; return *this;}
        const iterator& operator++() const {ptr++; return *this;}

        iterator operator++(int) {iterator it = *this; ++(*this); return it;}
        const iterator operator++(int) const {iterator it = *this; ++(*this); return it;}

        iterator& operator--() {ptr--; return *this;}
        const iterator& operator--() const {ptr--; return *this;}

        iterator operator--(int) {iterator it = *this; --(*this); return it;}
        const iterator operator--(int) const {iterator it = *this; --(*this); return it;}

        bool operator==(iterator it) const {return ptr == it.ptr;}
        bool operator!=(iterator it) const {return !(*this == it);}

        T* operator->() {return ptr;} 
        const T* operator->() const {return ptr;} 

        difference_type operator-(const iterator& other) const {return ptr - other.ptr;}

        iterator& operator+=(difference_type n) {ptr += n; return *this;}
        const iterator& operator+=(difference_type n) const {ptr += n; return *this;}

        iterator& operator-=(difference_type n) {ptr -= n; return *this;}
        const iterator& operator-=(difference_type n) const {ptr -= n; return *this;}

        iterator operator+(difference_type n) {iterator it = *this; return it+=n;}
        const iterator operator+(difference_type n) const {iterator it = *this; return it+=n;}

        iterator operator-(difference_type n) {iterator it = *this; return it-=n;}
        const iterator operator-(difference_type n) const {iterator it = *this; return it-=n;}

        T& operator[](difference_type n) {return *(*this + n);}
        const T& operator[](difference_type n) const {return *(*this + n);}

        bool operator<(iterator it) const {return *this - it < 0;}
        bool operator>(iterator it) const {return it < *this;}

        bool operator<=(iterator it) const {return !(*this > it);}
        bool operator>=(iterator it) const {return !(*this < it);}

    };
    //TODO: оператор- begin_ -> begin ...
    //TODO: range for в main

    iterator begin() {
        return iterator{data};
    }

    iterator end() {
        return iterator{data + cap};
    }

    const iterator cbegin() const {
        return iterator{data};
    }

    const iterator cend() const {
        return iterator{data + cap};
    }

    T* begin_() {
        return data;
    }

    T* end_() {
        return data + cap;
    }

    const T* cbegin_() const {
        return data;
    }

    const T* cend_() const {
        return data + cap;
    }

    operator bool() const {
        return bool(cap);
    }

    template<typename TT, typename UU>
    friend void swap(Storage<TT, UU>& st1, Storage<TT, UU>& st2);
};

template<typename T, typename U>
void swap(Storage<T, U>& st1, Storage<T, U>& st2) {
    std::swap(st1.data, st2.data);
    std::swap(st1.cap, st2.cap);
}

/*
template<>
struct std::iterator_traits<Storage<float, int>::iterator> {
    using value_type = float;
    using pointer = float*;
    using reference = float&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};

template<>
struct std::iterator_traits<const Storage<float, int>::iterator> {
    using value_type = float;
    using pointer = float*;
    using reference = float&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};

template<>
struct std::iterator_traits<Storage<float, size_t>::iterator> {
    using value_type = float;
    using pointer = float*;
    using reference = float&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};

template<>
struct std::iterator_traits<Storage<int, int>::iterator> {
    using value_type = int;
    using pointer = int*;
    using reference = int&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};

template<>
struct std::iterator_traits<const Storage<int, int>::iterator> {
    using value_type = int;
    using pointer = int*;
    using reference = int&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};

template<>
struct std::iterator_traits<Storage<Number>::iterator> {
    using value_type = Number;
    using pointer = Number*;
    using reference = Number&;
    using difference_type = std::ptrdiff_t;
    using iterator_category = std::random_access_iterator_tag;
};
*/
