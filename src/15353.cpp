// 큰 수 A+B (2)
#include <iostream>
using namespace std;

int main()
{
   string a, b;
   cin >> a >> b;
   int al, bl, minl, maxl;
   al = a.size();
   bl = b.size();
   string r;

   minl = al > bl ? bl : al;
   maxl = al > bl ? al : bl;
   int of = 0;
   int i;
   for(i = 0; i < minl; i++) {
       int num = a[al - i - 1] - '0' + b[bl - i - 1] - '0' + of;
       of = 0;
       if (num >= 10) {
           r = to_string(num - 10) + r;
           of = 1;
       } else {
        r = to_string(num) + r;
       }
   }
   for(int j = i; j < maxl; j++) {
       int num;
       if(j >= al) {
            num = b[bl - j - 1] - '0' + of;
       } else {
           num = a[al - j - 1] - '0' + of;
       }
       of = 0;
        if(num >= 10) {
            r = to_string(num - 10) + r;
            of = 1;
        } else {
            r = to_string(num) + r;
        }
   }
   if(of) r = to_string(of) + r;
   cout << r;
   return 0;
}