#include <iostream>
#include <fstream>
using namespace std;

int main() {
    cout << "Please enter a 5 character password: ";
    string s;
    cin >> s;
    if (s == "fakes") {
        cout << "You have now logged in. Welcome 'money'" << endl << endl;
        ofstream of("hint.txt");
        of << "money" << endl;
        of.close();
    }
    else cout << "Incorrect login" << endl;
}