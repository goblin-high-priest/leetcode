class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] bucket = new List[nums.length+1];
        int[] res = new int[k];
        int index = 0;

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for (int num : count.keySet()) {
            int freq = count.get(num);

            if (bucket[freq] == null) {
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(num);
        }

        for (int i = bucket.length - 1; i >= 0; i--) {

            if (bucket[i] != null) {
                
                for (int num : bucket[i]) {
                    res[index++] = num;

                    if (index == k) {
                        return res;
                    }
                }
            }
        }

        return res;
    }
}