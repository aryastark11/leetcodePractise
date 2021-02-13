class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for (auto& it : nums) {
            // get index of current element.
            auto itr = find(nums.begin(), nums.end(), it);
            int index1 = itr - nums.begin();
            // get the difference of target and current element.
            auto diff = target - it;
            // cause we should consider each element only once.
            // start with next element after the current elements index.
            auto findDiff = find(itr+1, nums.end(), diff);
            if (findDiff != nums.end()) {
                // get the index of diff.
                int index2 = findDiff - nums.begin();
                result.push_back(index1);
                result.push_back(index2);
                return result; 
            }
        // required difference is not there in the array, continue to next element
            else {
                continue;
            }
        }
        return result;
    }
};