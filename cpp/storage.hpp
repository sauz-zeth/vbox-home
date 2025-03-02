#include <iostream>
#include <memory>
#include <utility>

template<typename T = float, typename U = size_t>
class Storage {
    U cap;
    std::allocator<T> al;
    T *data;
    //TODO: спроектировать интерфейс класса Storage (нельзя менять Vec)
    //TODO: реализовать спроектированный функционал
};
