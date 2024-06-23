#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

int N;
map<int, int> human_num;
map<int, vector<int>> node;
vector<int> visited;
bool flag = false;
int minVal = numeric_limits<int>::max();

void dfs(int x, const vector<int>& arr) {
    visited[x] = 1;

    if (count(visited.begin(), visited.end(), 1) == arr.size()) {
        flag = true;
        return;
    } else {
        for (int n : node[x]) {
            if (find(arr.begin(), arr.end(), n) != arr.end() && visited[n] == 0) {
                visited[n] = 1;
                dfs(n, arr);
            }
        }
    }
}

int main() {
    cin >> N;

    vector<int> area(N);
    for (int i = 0; i < N; ++i) {
        area[i] = i + 1;
    }

    for (int i = 1; i <= N; ++i) {
        int num;
        cin >> num;
        human_num[i] = num;
    }

    for (int i = 1; i <= N; ++i) {
        int num;
        cin >> num;
        vector<int> temp(num);
        for (int j = 0; j < num; ++j) {
            cin >> temp[j];
        }
        node[i] = temp;
    }

    for (int n = 1; n <= N; ++n) {
        vector<vector<int>> com;
        for (int i = 0; i < (1 << N); ++i) {
            vector<int> subset;
            for (int j = 0; j < N; ++j) {
                if (i & (1 << j)) {
                    subset.push_back(area[j]);
                }
            }
            if (subset.size() == n) {
                com.push_back(subset);
            }
        }

        for (const vector<int>& c : com) {
            vector<int> one, two;
            for (int i : c) {
                one.push_back(i);
            }
            for (int a : area) {
                if (find(one.begin(), one.end(), a) == one.end()) {
                    two.push_back(a);
                }
            }

            visited.assign(N + 1, 0);
            flag = false;
            dfs(one[0], one);

            if (flag) {
                visited.assign(N + 1, 0);
                flag = false;
                if (!two.empty()) {
                    dfs(two[0], two);
                }
            }

            if (flag) {
                int cnt1 = 0, cnt2 = 0;
                for (int o : one) {
                    cnt1 += human_num[o];
                }
                for (int t : two) {
                    cnt2 += human_num[t];
                }
                minVal = min(minVal, abs(cnt1 - cnt2));
            }
        }
    }

    if (minVal == numeric_limits<int>::max()) {
        cout << -1 << endl;
    } else {
        cout << minVal << endl;
    }

    return 0;
}