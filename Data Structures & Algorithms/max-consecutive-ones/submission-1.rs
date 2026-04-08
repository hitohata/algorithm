impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut count: i32 = 0;
        let mut ans: i32 = 0;

        for num in nums.iter() {
            if *num != 1 {
                count = 0;
                continue;
            }
            count += 1;
            ans = max(count, ans);
        }

        ans
    }
}
