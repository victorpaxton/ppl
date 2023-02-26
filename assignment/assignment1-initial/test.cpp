#include <iostream>

using namespace std;

int main()
{
    // /* Comment \n
    /*
    /*
    /* // */
    for (int i = 1; i < 101; i++)
    {
        cout << "def test_" << i << "(self):\n";
        cout << "\t input = \"\"\"\"\"\" \n";
        cout << "\t expect = \"\" \n";
        cout << "\t self.assertTrue(TestParser.test(input, expect, " << 200 + i << "))\n";
    }
    // string s = "\n ;

    int a = 1, b = 2;
    if (a == b)
        a = a + 1;
    b = b + 2;

    if (a == b)
        ;

    int count = 100;
    int count2 = 50;
    for (int i = 0; i < count && i > 50; i++)
    {
        /* code */
    }
}