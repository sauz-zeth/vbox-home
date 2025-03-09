#include <iostream>
#include <memory>
#include <utility>

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

    Storage(U cap) : cap{cap}, data{al.allocate(cap)} {}

    Storage(const Storage& coords) : cap{coords.cap}, data{al.allocate(coords.cap)} {}

    template<typename TT, typename UU>
    Storage(const Storage<TT, UU>& coords) : cap{coords.capacity()}, data{al.allocate(coords.capacity())} {}

    Storage(Storage&& coords) : cap{coords.cap}, data{coords.data} {
        coords.data = nullptr;
        coords.cap = 0;
    }

    void fillData(T defaultValue, U startPoint, U endPoint) {
        for(U i = startPoint; i < endPoint; i++) {
            new(data + i) T{defaultValue};
        }
    }

    void fillData(const Storage& coords, U startPoint, U endPoint) {
        for(U i = startPoint; i < endPoint; i++) {
            new(data + i) T{coords.at(i)};
        }
    }

    template<typename TT, typename UU>
    void fillData(const Storage<TT, UU>& coords, U startPoint, U endPoint) {
        for(U i = startPoint; i < cap && i < coords.capacity(); i++) {
            new(data + i) T{static_cast<T>(coords.at(i))};
        }
    }

    void fillData(Storage&& coords, U startPoint, U endPoint) {
        coords.data = nullptr;
        coords.cap = 0;
    }

    void destructData(U startPoint, U endPoint) {
        if (!data) return;

        for (T* p = data + startPoint; p != data + endPoint; ++p) {
            p->~T();
        }
    }

    T& operator[](U i) {
        return at(i);
    }

    T* operator+(U value) {
        return data + value;
    }

    T* operator-(U value) {
        return data - value;
    }

    ~Storage() {
        if (!data) return;

        al.deallocate(data, cap);
    }
};
