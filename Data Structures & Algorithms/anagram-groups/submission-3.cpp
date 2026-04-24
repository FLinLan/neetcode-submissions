class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // sort the string for an anagram key? n = 100, shouldn't be too slow

        unordered_map<string, vector<string>> anagramMap;
        for (string & s : strs) {
            // vector<char> anagram(s.begin(), s.end());   
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end()); 
            anagramMap[sortedS].push_back(s);
        }
        
        vector<vector<string>> ans;

        for (const auto & [sKey, sList] : anagramMap) {
            vector<string> subList;
            for (string s : sList) {
                subList.push_back(s);
            }
            ans.push_back(subList);
        }

        return ans;
        
    }
};
