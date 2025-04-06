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
        mutable T* pos;
    public:
        using value_type = T;
        using pointer = T*;
        using reference = T&;
        using difference_type = std::ptrdiff_t;
        using iterator_category = std::forward_iterator_tag;

        explicit iterator(T* ppos) : pos{ppos} {}
        T& operator*() {return *pos;}
        const T& operator*() const {return *pos;}
        iterator& operator++() {pos++; return *this;}
        const iterator& operator++() const {pos++; return *this;}
        iterator operator++(int) {iterator it = *this; ++(*this); return it;}
        const iterator operator++(int) const {iterator it = *this; ++(*this); return it;}
        bool operator==(iterator it) const {return pos == it.pos;}
        bool operator!=(iterator it) const {return !(*this == it);}
        difference_type operator-(const iterator& other) const { return pos - other.pos; }
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
