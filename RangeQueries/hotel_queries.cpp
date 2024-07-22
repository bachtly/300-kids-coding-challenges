#include<iostream>
#include<set>
#include<vector>
using namespace std;

#define i2 pair<int,int>
#define x first
#define y second

const int MAXN=2e5;
int n, m, t[4*MAXN];

int query(int v, int tl, int tr, int l, int r) {
    if (l > r) 
        return 0;
    if (l == tl && r == tr) 
        return t[v];
    int tm = (tl + tr) / 2;
    return max(query(v*2, tl, tm, l, min(r, tm)), 
                   query(v*2+1, tm+1, tr, max(l, tm+1), r));
}

void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = max(t[v*2], t[v*2+1]);
    }
}

int bin_search_segment_tree_max_prefix(int a) {
    if (t[1] < a) {
        return 0;
    }
    
    int l =1, r=n;
    while(l<r) {
        int mid = (l+r)/2;
        
        int max_1_mid = query(1,1,n,1,mid);
        // cout << "l r mid max1mid" << l << ' ' << r << ' ' << mid << " " << max_1_mid << endl;
        
        if (max_1_mid >= a) {
            r=mid;
        }
        else {
            l=mid+1;
        }
    }

    return l;
}

int main() {
    cin >> n >> m;

    // Build segment tree
    vector<int> arr(n+1);
    for (int i=1; i<=n; ++i) {
        cin >> arr[i];
        update(1, 1, n, i, arr[i]);
    }

    while(m--) {
        int a;
        cin>>a;

        int pos = bin_search_segment_tree_max_prefix(a);
        cout << pos << " ";

        if (pos > 0) {
            // update hotel rooms
            arr[pos]-=a;
            update(1,1,n,pos,arr[pos]);
        }
    }
    cout << endl;

    return 0;
}