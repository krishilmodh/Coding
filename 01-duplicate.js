var containsDuplicate = function (nums) {
    for (let i = 1; i <= nums.length; i++) {
        let j = i;
        while (j < nums.length) {
            if (nums[i - 1] === nums[j]) {
                console.log(true);
                return true;
            }
            j++;
        }
    }
    console.log(false);
    return false;
};

containsDuplicate([1, 2, 3, 4,1]);
