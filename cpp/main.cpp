#include <iostream>
#include <cassert>
#include "number.hpp"
#include "vec.hpp"

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


    v16.at(0) = 1;
    v16.at(1) = 3;
    v16.at(2) = 5;
    v16.print("v16");

    v16.resize(4);
    v16.print("v16 resized from 3 to 4");

    v16.resize(2);
    v16.print("v16 resized from 4 to 2");

    v16.resize(3);
    v16.print("v16 resized from 2 to 3");

    v16.shrink();
    v16.print("v16 shrinked");

    Vec v17{4};
    v17.resize(2);
    v17.print("v17");
    v17.shrink();
    v17.print("v17");

    for(int i = 0; i < 3; i++) {
        cout << "block start \n";
        Vec<float, int> v3{4};
        v3.at(0) = 1;
        cout << "block end \n";
    }

    Vec<> *vv {new Vec<>[5]}; 
    cout << "vv allocated\n";

    delete[] vv;    // RAII!


    Vec<Number> v18{};
    v18[0] = 100.;

    cout << v18[0].value << ' ' << v18[1].value << endl;
//    v18.print("v18");
    
    assert(v18[0].value == 100);

    const Storage<float, int> st{10};
    for(int i = 0; i < 10; i++) {
        const_cast<float&>(st[i]) = i;
    }

    for(Storage<float, int>::iterator it = st.cbegin(); it != st.cend(); ++it) {
//        typename Storage<float, int>::iterator::value_type v = *it;
        typename std::iterator_traits<Storage<float, int>::iterator>::value_type v = *it;
        cout << v << ' ';
    }
    cout << endl;

    for(auto it = st.cbegin(); it != st.cend(); ++it) {
        cout << *it << ' ';
    } 
    cout << endl;

    cout << &*st.cbegin() << ' ' << &*++st.cbegin() << ' ' << &*st.cend() << endl;

    const_cast<float&>(st[0]) = 12;
    if(!st) cout << "st" << endl;

    Storage<float, int> st1{10};
    std::uninitialized_copy(st.cbegin(), st.cend(), st1.begin());

    for(auto it = st1.begin(); it != st1.end(); ++it) {
        cout << *it << ' ';
    }
    cout << endl;

    v16.print("v16");
    v17.assign(v16.begin(), v16.end());
    v17.print("v17");

    float a[] = {1, 2, 44, 56};

    v17.assign(a, a + 4);

    for (auto& it : st1) {
        cout << it << ' ';
    }
    cout << endl;

    auto it1 = st1.begin();
    auto it2 = st1.end();

    std::ptrdiff_t dist = it2 - it1;

    cout << dist << endl;

    Storage<Number> st2{10};
//    new(&*st2.begin()) Number{123};
    new(&st2[1]) Number{1111};
    std::uninitialized_fill(st2.begin(), st2.begin() + 1, Number{123});
    auto st2_it1 = st2.begin();
    cout << st2[0].value << endl;
    cout << st2_it1[0].value << endl;
    cout << st2_it1->value << endl;

    cout << st2[1].value << endl;
    auto st2_it2 = st2.begin() + 1;
    cout << st2_it2->value << endl;
    cout << (st2_it2 >= st2_it1) << endl;

    Vec<float, int> v20{};

    v20.push_back(10);
    v20.push_back(20);
    v20.push_back(30);

    v20.print("v20");

    Vec<float, int> v21{};

    v21.push_back(1);
    v21.push_back(2);
    v21.push_back(3);

    v20.insert(v20.begin() + 1, v21.begin() + 2, v21.end());
    v20.print("v20");

    // v20.print("v20");

    
//    v20.push_back(20);
//    v20.print("v20");
//    v20.push_back(30);
//    v20.print("v20");
//    v20.push_back(40);
//    v20.print("v20");

    int i = 10;
    const int *p = &i;
    p++;
    
    cout << sizeof(typename Storage<float, int>::iterator) << endl;
    cout << sizeof(std::iterator_traits<Storage<float, int>>) << endl;

}
