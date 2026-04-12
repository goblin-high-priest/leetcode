class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] a, b;
        
        if (nums1.length < nums2.length) {
            a = nums1;
            b = nums2;
        } else {
            a = nums2;
            b = nums1;
        }

        int length = a.length + b.length;
        int half = length / 2;
        int left = 0, right = a.length - 1;

        while (true) {
            int i = Math.floorDiv(left + right, 2);
            int j = half - i - 2;

            int aLeft = (i >= 0) ? a[i] : Integer.MIN_VALUE;
            int aRight = (i + 1 < a.length) ? a[i+1] : Integer.MAX_VALUE;
            int bLeft = (j >= 0) ? b[j] : Integer.MIN_VALUE;
            int bRight = (j + 1 < b.length) ? b[j+1] : Integer.MAX_VALUE;

            if (aLeft <= bRight && bLeft <= aRight) {
                if (length % 2 == 1) {
                    return Math.min(aRight, bRight);
                } else {
                    return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2.0;
                }
            } else if (aLeft > bRight) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }
    }
}