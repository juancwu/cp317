#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class FileProcessor{
    // This are going to be global variables
    public:
        virtual fstream openFile(string file, string mode) = 0;
        virtual void closeFile(fstream file) = 0;

};