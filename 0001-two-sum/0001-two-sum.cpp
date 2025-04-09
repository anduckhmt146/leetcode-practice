class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashMap;
        vector<int> res;
        int size = nums.size();
        for(int i = 0; i < size; i++){
            int complement = target - nums[i];
            if(hashMap.count(complement) > 0){
                res.push_back(hashMap[complement]);
                res.push_back(i);
                return res;
            }
            hashMap.insert(make_pair(nums[i], i));
        }
        return res;
    }
};