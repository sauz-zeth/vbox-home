    for(Storage<float, int>::iterator it = st.cbegin_(); it != st.cend_(); ++it) {
        typename Storage<float, int>::iterator::value_type v = *it;
        cout << v << ' ';
    }
    cout << endl;

    for(auto it = st.cbegin_(); it != st.cend_(); ++it) {
        cout << *it << ' ';
    } 
    cout << endl;

    cout << &*st.cbegin_() << ' ' << &*++st.cbegin_() << ' ' << &*st.cend_() << endl;

   const_cast<float&>(st[0]) = 12;
    if(!st) cout << "st" << endl;