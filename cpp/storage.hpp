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

    const T& operator[](U i) const {
        return at(i);
    }

    T& operator[](U i) {
        return at(i);
    }

    T* begin() {
        return data;
    }

    T* end() {
        return data + cap;
    }

    const T* cbegin() const {
        return data;
    }

    const T* cend() const {
        return data + cap;
    }

    ~Storage() {
        cout << "Storage destructed at " << this << endl;

        al.deallocate(data, cap);
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
