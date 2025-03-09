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

    T& at(U i) const {
        return data[i];
    }

    Storage(U cap = U{}) : cap{cap}, data{al.allocate(cap)} {
        cout << "Storage constructed at " << this << endl;
    }

    Storage(const Storage& st) = delete;

    Storage(Storage&& st) : cap{st.cap}, data{st.data} {
        cout << "Storage move constructed at " << this << " from " << &st << endl;

        st.data = nullptr;
        st.cap = 0;
    }

    void fill(const T& value, U begin, U end) {
        for(U i = begin; i < end; i++) {
            new(data + i) T{value};
        }
    }

    void copy(const Storage& st, U begin, U end) {
        for(U i = begin; i < end; i++) {
            new(data + i) T{st.at(i)};
        }
    }

    template<typename TT, typename UU>
    void copy(const Storage<TT, UU>& st, U begin, U end) {
        for(U i = begin; i < cap && i < st.capacity(); i++) {
            new(data + i) T{static_cast<T>(st.at(i))};
        }
    }

    void destruct(U begin, U end) {
        if (!data) return;

        for(T* p = data + begin; p != data + end; ++p) {
            p->~T();
        }
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

    ~Storage() {
        cout << "Storage destructed at " << this << endl;

        if (!data) return;

        al.deallocate(data, cap);
    }
};
