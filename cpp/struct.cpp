#include <stdio.h>
#include <utility>

void f(double);

typedef
struct Point {
    double x, y, z;
    int index;
} Point;

//constexpr int N {1000};
class PrivatePoint {
    static constexpr int N {1000};
    inline static int index_max {0};
    
//    void indexIncrement() {
//        this->index = ++PrivatePoint::index_max;
//        this->index = ++this->index_max;
//        this->index = ++index_max;
//    }

public:
    
    int a[N] {};
    /*const*/ mutable int index = ++index_max;
    double x{2}, y, z;
    
    static int instanceCount();

    // constructors
    explicit PrivatePoint();
    /*explicit*/ PrivatePoint(double xx, double yy = 0, double zz = 0);
    PrivatePoint(int xx, int yy, int zz);
    PrivatePoint(const PrivatePoint& pp);   //copy constructor
//    PrivatePoint(const PrivatePoint& pp) = default; //copy constructor explicitly defaulted
    PrivatePoint(PrivatePoint&& pp);   //move constructor
//    PrivatePoint(PrivatePoint&& pp) = delete;   //move constructor explicitly deleted
    ~PrivatePoint();
    
    void print() const {
        printf("index: %d\n", index);
        printf("x: %g\n", x);
        printf("y: %g\n", y);
        printf("z: %g\n", z);

//        printa();
    }

    void printa();
};

int PrivatePoint::instanceCount() {
    return index_max;
}

inline PrivatePoint::PrivatePoint() : y{x}, x(1), z{1} {
    printf("default constructed at %p\n", this);
//    this->indexIncrement();

    f(x);
}

inline PrivatePoint::PrivatePoint(double xx, double yy, double zz)
        : x{xx}, y{yy}, z{zz} {
    printf("constructed at %p\n", this);
//    indexIncrement();
}

inline PrivatePoint::PrivatePoint(int xx, int yy, int zz)
        : x(xx), y(yy), z(zz) {
    printf("int constructed at %p\n", this);
//    indexIncrement();
}

inline PrivatePoint::PrivatePoint(const PrivatePoint& pp)
        : x{pp.x}, y{pp.y}, z{pp.z} {
    printf("copy constructed at %p\n", this);
}

inline PrivatePoint::PrivatePoint(PrivatePoint&& pp)
        : x{pp.x}, y{pp.y}, z{pp.z} {
    printf("move constructed at %p\n", this);
}

void PrivatePoint::printa() {
    printf("a: [");
    for(int i = 0; i < N; i++) {
        printf("%d", a[i]);
        if(i < N - 1) printf(", "); 
    }
    printf("]\n");
}

inline PrivatePoint::~PrivatePoint() {
    printf("destructed at %p\n", this);
}


//int PrivatePoint::index_max {0};

int i {5}; //static (static memory)

void f(double x) {
    int i {3}; //auto (stack)
    printf("f\n");
}

PrivatePoint g(PrivatePoint pp) {
    printf("g: pp.x = %g\n", pp.x);
    return PrivatePoint{}; //copy elision, URVO
}

int main() {
    Point q = {2.7, 4.6, 1.2, 7}; //unqualified brace-enclosed initializer list
    Point t = Point{2, 3, 4, 5}; //qualified brace-enclosed initializer list
    Point r {2, 1, 3.3, 2}; //aggregate i12n, uniform i12n
    Point s {}; //empty initializer list, default construction
    Point z; //default i12n, default construction
    printf("%g\n", z.z);
    int i {}; //default construction (default value = 0), direct i12n
    int i0(12); //direct i12n, direct constructor call
    printf("%d\n", i0);
    int i1 = {}; //default construction, indirect (copy) i12n
    int i2 = int{};
    int j; //default i12n, no construction
    int *k = nullptr;
    printf("%g\n", s.x);
//    Point Point;
    printf("%g\n", q.y); 
    Point* pq = &q;
    printf("%g\n", (*pq).y); 
    printf("%g\n", pq->y); 

    printf("pp: ");
    PrivatePoint ppp;
//    ppp.print();
    printf("ppp.index: %d\n", ppp.index);
    printf("%g\n", ppp.x);
    PrivatePoint ppq = PrivatePoint();
    printf("ppq.index: %d\n", ppq.index);
    PrivatePoint ppr = PrivatePoint{};
    printf("ppr.index: %d\n", ppr.index);
//    PrivatePoint pps();
//    printf("%g\n", pps.x);

    printf("%g\n", ppq.x);
    printf("ppg:\n");
    PrivatePoint ppg = g(PrivatePoint{});

    printf("new:\n");
    Point *pe {new Point{1, 2, 3, 4}}; //dynamic (heap)
    printf("%g\n", pe->x);
    delete pe;

    printf("ppp.index: %d\n", ppp.index);
    PrivatePoint ppc {ppp}; //copy construction, direct i12n
    printf("ppc.index: %d\n", ppc.index);
    PrivatePoint ppd = ppp; //copy construction, indirect i12n
    printf("ppd.index: %d\n", ppd.index);
//    ppc = PrivatePoint{}; //assignment, prvalue materialization -> xvalue

    const int i3 {123}; //constant variable
    constexpr int i4 {321}; //constant expression

    PrivatePoint ppt {};
    ppt.print();

    PrivatePoint ppy {1, 2, 5};
    ppy.print();
    PrivatePoint ppy2 {1., 2., 5.};
    ppy2.print();

//    PrivatePoint ppy3 {1., 2, 5.};  //ambiguous
//    ppy3.print();
    
    PrivatePoint ppy4 {1., 2.};
    ppy4.print();

    PrivatePoint ppy5 = 1;  //implicit type cast
    ppy5.print();

    PrivatePoint ppy6 = (PrivatePoint)1;  //explicit type cast
    ppy6.print();

    PrivatePoint ppy7 = static_cast<PrivatePoint>(1);  //explicit type cast
    ppy7.print();

    printf("ppy8:\n");
    PrivatePoint ppy8 = PrivatePoint(14);   //explicit type cast
    ppy8.print();

    static PrivatePoint ppy9 = PrivatePoint{14};   //explicit type cast
    ppy9.print();

    const PrivatePoint ppy10 = PrivatePoint{14};    //const
    ppy10.index = 44;
//    ppy10.printa();

    printf("ppy11:\n");
//    PrivatePoint ppy11 = (const PrivatePoint&)PrivatePoint(14);
    PrivatePoint ppy11 = static_cast<const PrivatePoint&>(PrivatePoint(14));
    ppy11.print();

    printf("ppy12:\n");
//    PrivatePoint ppy12 = (PrivatePoint&&)PrivatePoint(14);
    PrivatePoint ppy12 = std::move(PrivatePoint(14));
    ppy12.print();

    printf("ppy13:\n");
    PrivatePoint ppy13 = std::move(ppp);
    ppy13.print();

    double dd = 1;  //implicit type cast 
    double dd0 = (double)1;

    double dd1 = double(1); //explicit type cast (conversion)
    double dd2 = double{1};
    
    printf("%d\n", ppy9.instanceCount());
    printf("%d\n", PrivatePoint::instanceCount());

    PrivatePoint&& rpp = PrivatePoint{20};
    PrivatePoint& rrpp = rpp;

    rpp.x = 32;
    rpp.print();

    const PrivatePoint& crpp = PrivatePoint{20};
//    crpp.x = 123;
    
    ((PrivatePoint&)crpp).x = 44;
    crpp.print();
//    crpp.printa();
}

