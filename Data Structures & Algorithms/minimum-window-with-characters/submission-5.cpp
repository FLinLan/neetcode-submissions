class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;
        for (char ch : t) {
            tMap[ch]++;
        }
        
        int seen = 0, matching = tMap.size();
        int L = 0, R = 0;
        int ans[3] = {INT_MAX, L, R}; 
        for (int R = 0; R < s.length(); R++) {
            char chR = s[R];
            sMap[chR]++;
            if (tMap.count(chR) && sMap[chR] == tMap[chR]) {
                seen++;
            }
            while (L <= R && seen == matching) {
                if (ans[0] > (R-L+1)) {
                    ans[0] = (R-L+1);
                    ans[1] = L;
                    ans[2] = R;
                }
                char chL = s[L];
                sMap[chL]--;
                if (tMap.count(chL) && sMap[chL] < tMap[chL]) {
                    seen--;
                }
                L++;
            }
        }
        L = ans[1], R = ans[2];
        return ans[0] != INT_MAX ? s.substr(L, (R-L+1)) : "";
    }
};
