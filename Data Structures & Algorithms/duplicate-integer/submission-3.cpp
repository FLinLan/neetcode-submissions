class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numsSet;

        for (int n : nums) {
            numsSet.insert(n);
        }

        return numsSet.size() != nums.size();
    }
};