#include <iostream>

using namespace std;

int main()
{
    // /* Comment \n
    /*
    /*
    /* //
    */ * /
        for (int i = 5; i < 101; i++)
    {
        cout << "def test_" << i << "(self):\n";
        cout << "\t input = \"\"\" \"\"\" \n";
        cout << "\t expect = \" \" \n";
        cout << "\t self.assertTrue(TestLexer.test(input, expect, " << 100 + i << "))\n";
    }
}