class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        ROWS,COLS= len(matrix),len(matrix[0])
        correct_row=-1
        top_row,bottom_row=0,ROWS-1
        while top_row<=bottom_row:
            mid_row=(bottom_row+top_row)//2
            if target>matrix[mid_row][-1]:
                top_row=mid_row+1
            elif target<matrix[mid_row][0]:
                bottom_row=mid_row-1
            else:
                correct_row=mid_row
                break
        if correct_row==-1:
            return False
        row=matrix[correct_row]
        l,r=0,COLS
        while l<=r:
            mid=(l+r)//2
            if target==row[mid]:
                return True
            elif target<row[mid]:
                r=mid-1
            else:
                l=mid+1
        return False




