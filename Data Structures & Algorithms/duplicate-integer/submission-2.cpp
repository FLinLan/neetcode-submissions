class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> st;
        
        for (auto n : nums) {
            st.insert(n);
        }

        return st.size() != nums.size();
    }
};
