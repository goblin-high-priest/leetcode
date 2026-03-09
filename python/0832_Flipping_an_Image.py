class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            l, r = 0, len(image[0]) - 1

            while l < r:
                image[i][l], image[i][r] = 1 - image[i][r], 1 - image[i][l]
                l += 1
                r -= 1
            
            if l == r: image[i][l] = 1 - image[i][l]
        
        return image