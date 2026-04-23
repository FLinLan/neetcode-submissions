class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> sumMap;

        // [3,4,5,6]
        // 7-4 = 3

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            if (sumMap.count(diff) > 0) {
                // vector<int> ans(2, 0) = {sumMap[diff], i}
                return {sumMap[diff], i};
            } else {
                sumMap[nums[i]] = i;
            }
        }

        return {-1, -1};
    }
};
