#include <bits/stdc++.h>
#define LL  long long
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<n;i++)
#define REV(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define pri(a) cout<<a<<endl
#define prii(a,b) cout<<a<<" "<<b<<endl
#define priii(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl
#define hi printf("Hello World\n");
using namespace std;

const int INF = 1<<29;
const int MX  = 1e5+10;

string div(string s, LL n)
{
    LL rem = 0, fl = false;
    string an = "";
    REP(i,SZ(s))
    {
        rem = s[i]-48 + 10*rem;
        if(rem/n) fl=true;
        if(fl) an+=(rem/n + 48);
        rem %= n;
    }
    if(!fl) an+="0";
    return an;
}

LL rem(string s, LL n)
{
    LL r = 0;
    REP(i,SZ(s))
    {
        r = s[i]-48 + 10*r;
        r %= n;
    }
    return r;
}

int main()
{
    string s;
    LL n;
    char ch;

    while(cin>>s>>ch>>n)
    {
        if(ch=='/')
        {
            pri(div(s,n));
        }else
        {
            pri(rem(s,n));
        }
    }
    return 0;
}
