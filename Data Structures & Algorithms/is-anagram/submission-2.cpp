class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        int n = s.size();
        vector<int> mapT(26, 0);
        vector<int> mapS(26, 0);

        for (int i = 0; i < n; i ++) {
            char chT = t[i];
            char chS = s[i];
            mapT[chT - 'a']++;
            mapS[chS - 'a']++;
        }

        return mapT == mapS;
    }
};
