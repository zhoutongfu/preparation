#valid parenthesis
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        if len(s) < 2:
            return False
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' and (len(stack) == 0 or stack.pop() != '('):
                return False
            elif ch == ']' and (len(stack) == 0 or stack.pop() != '['):
                return False
            elif ch == '}' and (len(stack) == 0 or stack.pop() != '{'):
                return False
                
        return len(stack) == 0
 

# count and say
class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return str(1)
        str_seq = self.countAndSay(n-1)
        str_ans = ""
        last = str_seq[0]
        current = last
        count = 1
        for i in range(0,len(str_seq)-1):
            current = str_seq[i+1]
            if current == last:
                count += 1
            else:
                str_ans += str(count) + last
                last = current
                count = 1
                
        if current == last:
            str_ans += str(count) + last
        else:
            str_ans += str(1) + current
            
        return str_ans

# Excel Sheet Column Number
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        value = 0
        for i in range(len(s)):
            value += self.charValue(s[i]) * (26**(len(s)-i-1))
        return value
    
    
    def charValue(self,ch):
        return ord(ch) - ord('A') + 1
        

#Majority Element
class Solution:
    # @param num, a list of integers
    # @return an integer
    # def majorityElement(self, num):
    #     new_num = sorted(num)
    #     return new_num[len(num)/2]
    def majorityElement(self,num):
        return self.majorityHelper(num,None)
    
    def majorityHelper(self,num,tieBk):
        if len(num) == 0:
            return tieBk
        else:
            if  len(num)%2 == 1:
                tieBk = num[-1]
            else:
                tieBk = None
            candidate = []
            for i in range(0,len(num)-1,2):
                if num[i] == num[i+1]:
                    candidate.append(num[i])
        
            major = self.majorityHelper(candidate,tieBk)
            
            if major == None:
                return tieBk
            elif (num.count(major)*2 > len(num)) or (major == tieBk and 2*(num.count(major)+1) > len(num)):
                return major
            else:
                return None
            
        
#Excel Sheet Column Title
class Solution:
    # @return a string
    def convertToTitle(self, num):
        value = ''
        while num != 0:
            num -= 1
            d = num %26
            value = self.numToChar(d) + value
            num /= 26
        return value
    
    # the given number is between 0 and 25, inclusively
    def numToChar(self,num):
        return chr(num+ord('A'))
        

#Reverse Integer
class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            return -1*self.reverse(-x)
        return int(str(x)[::-1]) if int(str(x)[::-1]) < 2**31-1 else 0 

class Solution2:
    # @return an integer
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        result = 0
        while x > 0:
            result = 10* result + x%10
            x /= 10
         
        result *= flag   
        if result > 2**31 -1 or result < -2**31:
            result = 0
            
        return result
        
        

#compare version number
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        while len(v1) < len(v2):
            v1.append('0')
        
        while len(v2) < len(v1):
            v2.append('0')
        
        for i in range(0,len(v1))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0        



# Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        a_len = self.listLen(headA)
        b_len = self.listLen(headB)
        if a_len > b_len:
            for i in range(0,a_len-b_len):
                headA = headA.next
        elif a_len < b_len:
            for i in range(0,b_len - a_len):
                headB = headB.next
        
        while headA is not None:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
        
        

    def listLen(self,head):
        count = 0
        while head != None:
            count += 1
            head = head.next
            
        return count



#ZigZag Conversion
class Solution:
    # @return a string
    def convert(self, s, nRows):
        # init dict/map
        r_dict = {}
        for i in range(nRows):
            r_dict[i] = []
        
        i = 0
        s_len = len(s)
        while True:
            for l in range(nRows):
                if i >= s_len:
                    return self.getNewVersion(r_dict)
                r_dict[l].append(s[i])
                i += 1
            
            for m in range(nRows-2,0,-1):
                if i >= s_len:
                    return self.getNewVersion(r_dict)
                r_dict[m].append(s[i])
                i += 1
        
        
    def getNewVersion(self,dict):
        result = ''
        for i in range(len(dict)):
            result += ''.join(dict[i])
        
        return result   



# Palindrome Number 
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_len = 0
        y = x
        while y!= 0:
            x_len += 1
            y /= 10
        
        for i in range(0,x_len/2):
            if x%10 != x/(10**(x_len-1-2*i)):
                return False
            x %= 10**(x_len-1-2*i)
            x /= 10
            
        return True


# String to Integer (atoi)            
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        flag = 1
        if len(str) == 0:
            return 0
        if str[0] == '+':
            str = str[1::]
        elif str[0] == '-':
            str = str[1::]
            flag = -1
            
        result = 0
        for ch in str:
            if ch > '9' or ch < '0':
                break
            else:
                result = result*10 + int(ch)
        result *= flag
        if result > 2**31-1: 
            return 2**31-1
        elif result < -1*2**31: # max 2^31-1, min -2^31
            return -1*2**31
        return result
                
            
# Merge Two Sorted Lists        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val < l2.val:
            small = l1
            big = l2
        else:
            small = l2
            big = l1
        
        preSmall = small
        result = small
        
        while small != None and big != None:
            while small != None and small.val <= big.val:
                preSmall = small
                small = small.next
                
            preSmall.next = big
            temp = small
            small = big
            big = temp
            
        return result            
        
        

# Remove Duplicates from Sorted List 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        result = head
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return result
            
    

# Remove Nth Node From End of List   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        fast = head
        slow = head
        for i in range(n):
            if fast == None:
                return fast
            fast = fast.next
            
        if fast == None:
            return slow.next
            
        # now fast is n ahead of slow
        while fast.next != None:
            fast = fastself.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
 
# another approach, use two pointers 
class Solution2:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        pre = head
        cur = head.next
        while cur != None:
            if cur.val == pre.val:
                cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return head






 # Remove Duplicates from Sorted List II
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        
        cur = head
        d_set = set()
        # check if duplicates are at the front
        while cur.next != None:
            if cur.val in d_set:
                cur = cur.next
            elif cur.val == cur.next.val:
                d_set.add(cur.val)
                cur = cur.next
            else:
                break
        if cur.next == None:
            if cur.val in d_set:
                return None
            return cur
        
        result = cur
        preDup = cur
        
        while cur.next != None:
            if cur.val in d_set:
                cur = preDup
                cur.next = cur.next.next
            elif cur.val == cur.next.val:
                d_set.add(cur.val)
                cur = preDup
                cur.next = cur.next.next
            else:
                preDup = cur
                cur = cur.next
        if cur.val in d_set:
            preDup.next = None
            
        return result
        
        
                
# Linked List Cycle       
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head
        if head == None or head.next == None or head.next.next == None:
            return False
            
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        
        return False        
                   




# Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        result = head.next
        head.next = head.next.next
        result.next = head
        cur = head
        
        while cur.next != None and cur.next.next != None:
            temp = cur.next
            cur.next = temp.next
            temp.next = temp.next.next
            cur.next.next = temp
            cur = cur.next.next
            
        
        return result



# Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow






# Partition List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return head
            
        first = None
        first_head = None
        second = None
        second_tail = None
        
        while head != None:
            if head.val < x:
                if first == None:
                    first = ListNode(head.val)
                    first_head = first
                else:
                    first.next = ListNode(head.val)
                    first = first.next
            else:
                if second == None:
                    second = ListNode(head.val)
                    second_tail = second
                else:
                    second_tail.next = ListNode(head.val)
                    second_tail = second_tail.next
            head = head.next
        
        if first_head == None:
            return second
        else:
            first.next = second
            return first_head
        


class Solution2:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return head
            
        first = None
        first_head = None
        second = None
        second_tail = None
        
        while head != None:
            cur = head
            head = head.next
            cur.next = None
            
            if cur.val < x:
                if first == None:
                    first = cur
                    first_head = first
                else:
                    first.next = cur
                    first = first.next
            else:
                if second == None:
                    second = cur
                    second_tail = second
                else:
                    second_tail.next = cur
                    second_tail = second_tail.next
        
        if first_head == None:
            return second
        else:
            first.next = second
            return first_head
        




# Best Time to Buy and Sell Stock
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        cur_profit = 0
        
        for i in range(1,len(prices)):
            min_price = min(min_price,prices[i])
            cur_profit = max(cur_profit, prices[i]-min_price)
            
        return cur_profit

import sys
class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min_price = sys.maxint
        cur_profit = 0
        
        for price in prices:
            min_price = min(min_price,price)
            cur_profit = max(cur_profit, price-min_price)
            
        return cur_profit





# Best Time to Buy and Sell Stock II
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if len(prices) == 0:
            return profit
            
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]- prices[i-1]
        
        return profit
        
   
# Best Time to Buy and Sell Stock III
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
            
        min_price = prices[0]
        profit1 = 0
        profit1_list = []
        
        for price in prices:
            profit1 = max(profit1, price- min_price)
            profit1_list.append(profit1)
            min_price = min(min_price, price)
        
        profit2 = 0   
        max_price = prices[-1]
        profit2_list = []
        for price in prices[::-1]:
            profit2 = max(profit2, max_price-price)
            max_price = max(max_price,price)
            profit2_list.append(profit2)
            
        
        profit2_list = profit2_list[::-1]
        
        sum_profit = 0
        for i in range(len(prices)):
            sum_profit = max(sum_profit,profit1_list[i]+profit2_list[i])
        
        return sum_profit  



# Two Sum
class Solution1:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) == 0:
            return None
        
        num_dict = {}
        for i in range(len(num)):
            if (target - num[i]) in num_dict:
                return (num_dict[target-num[i]]+1,i+1)
            else:
                num_dict[num[i]] = i
        
        return None   


class Solution2:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) == 0:
            return None
        
        copy = sorted(num,reverse=False)
        i = 0
        j = len(num)-1
        while i < len(num) and j > 0:
            num_sum = copy[i] + copy[j]
            if target == num_sum:
                value1 = copy[i]
                value2 = copy[j]
                break
            elif num_sum > target:
                j -= 1
            else:
                i += 1
        else:
            return None
            
        index1 = -1
        index2 = -1
        for i in range(len(num)):
            if num[i] == value1 and index1 < 0:
                index1 = i
            elif num[i] == value2 and index2 < 0:
                index2 = i
        
        return tuple(sorted([index1+1,index2+1]))
                


# Find Peak Element
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        return self.findPeakHelper(0,len(num)-1,num)
        
    def findPeakHelper(self,start,end,num):
        if start == end:
            return start
        else:
            mid = (start+end)/2
            if num[mid] > num[mid + 1]:
                return self.findPeakHelper(start,mid,num)
            else:
                return self.findPeakHelper(mid+1,end,num)  



# plus one
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
                    break
                
        return digits                     


# Merge Sorted Array
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        j = 0
                
        while j < n and i < m:
            if A[i] > B[j]: 
                A.insert(i,B[j])
                m += 1
                j += 1
            i += 1    
            
        while j < n:
            A[i] = B[j]
            j +=1
            i += 1        




# Remove Duplicates from Sorted Array II 
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        rep = 1
        i = 0
        m = len(A)
        while i < m-1: 
            if A[i] == A[i+1]:
                if rep >=2:
                    A.pop(i+1)
                    m -=1
                else:
                    rep += 1
                    i += 1
            else:
                rep = 1
                i += 1
        
        
        return len(A)            





# Maximum Subarray
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return None
        temp_max = A[0]
        max_sum = A[0]
        
        for i in range(1,len(A)):
            if temp_max < 0:
                temp_max = 0
            temp_max += A[i]
            max_sum = max(temp_max,max_sum)
            
        return max_sum

# same problem, but could find the index of the subarray
class Solution1:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return None
        temp_max = A[0]
        temp_start = 0
        temp_end = 0
        
        max_sum = A[0]
        max_start = 0
        max_end = 0
        
        for i in range(1,len(A)):
            if temp_max < 0:
                temp_max = 0
                temp_start = i
                temp_end = i-1
                
            temp_max += A[i]
            temp_end += 1
            if temp_max > max_sum:
                max_sum = temp_max
                max_start = temp_start
                max_end = temp_end
            
            
        result = 0
        for i in range(max_start,max_end+1):
            result += A[i]
            
        return result  



# Unique Paths
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in xrange(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]


# Minimum Path Sum
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [[grid[0][0]]*n for i in xrange(m)]
        
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        
        return dp[m-1][n-1]
        
  





# Unique Paths II
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1]*n for i in xrange(m)]
        
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
                







# Binary Tree Preorder Traversal 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
        result = []
        self.traversalHelper(root,result)
        return result
    
    def traversalHelper(self,root,result):
        if root != None:
            result.append(root.val)
            self.traversalHelper(root.left,result)
            self.traversalHelper(root.right,result)
        



class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
        stack = []
        result = []
        
        while root != None or len(stack) > 0:
            if root != None:
                result.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return result







# Binary Tree Inorder Traversal 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        self.helper(root,result)
        return result
    
    def helper(self,root,result):
        if root != None:
            self.helper(root.left,result)
            result.append(root.val)
            self.helper(root.right,result)



class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        stack = []
        
        while root != None or len(stack) > 0:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
                
        return result  




# Binary Tree Postorder Traversal
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []
        
        result = []
        self.helper(root,result)
        return result
    
    def helper(self,root, result):
        if root != None:
            self.helper(root.left,result)
            self.helper(root.right,result)
            result.append(root.val)  


class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []
        
        result = []
        stack = []
        while root != None or len(stack) > 0:
            if root != None:
                result.append(root.val)
                stack.append(root.left)
                root = root.right
            else:
                root = stack.pop()
        
        result.reverse()
        return result
        




# Sort Colors
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) == 0:
            return
        red = 0
        white = 0
        blue = 0
        for num in A:
            if num == 0:
                red += 1
            elif num == 1:
                white +=1
            else:
                blue += 1
        for i in range(len(A)):
            if red > 0:
                A[i] = 0
                red -= 1
            elif white > 0:
                A[i] = 1
                white -= 1
            else:
                A[i] = 2        



class Solution2:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) == 0:
            return
        p0 = 0
        p2 = len(A)-1
        i = 0
        
        while i <= p2:
            if A[i] == 0 and i != p0:
                temp = A[p0]
                A[p0] = 0
                A[i] = temp
                p0 += 1
                i -= 1
                
            elif A[i] == 2 and i!= p2:
                temp = A[p2]
                A[p2] = 2
                A[i] = temp
                p2 -=1
                i -=1
            i += 1





# Insertion Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        
        while cur.next != None:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val <= cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                
        return dummy.next



# Sort List 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head
            
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        head1 = head
        head2 = slow.next
        slow.next = None # break head into head1 and head2, have to set the tail of head1
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1,head2)
        
    def merge(self,head1,head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        dummy = ListNode(0)
        p = dummy
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        
        if head1 == None:
            p.next = head2
        else:
            p.next = head1
            
        return dummy.next
        
        
        


# Single Number
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for i in range(1,len(A)):
            result ^= A[i]
        return result


# Valid Sudoku 
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        #row
        rep_set = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rep_set:
                    return False
                else:
                    rep_set.add(board[i][j])
            
            rep_set.clear()
        
        #column
        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in rep_set:
                    return False
                else:
                    rep_set.add(board[j][i])
            
            rep_set.clear()
        
        
        # each sub grid
        for k in range(9):
            for i in range(k/3*3,k/3*3+3):
                for j in range((k%3)*3,(k%3)*3+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in rep_set:
                        return False
                    else:
                        rep_set.add(board[i][j])
            rep_set.clear()
                        
        
        return True


# Maximum Depth of Binary Tree
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
    



# Same Tree 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None:
            if q == None:
                return True
            return False
        
        if q == None:
            return False
        
        return p.val == q.val and self.isSameTree(p.left,q.left) and  self.isSameTree(p.right,q.right)
        




# Balanced Binary Tree
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.helper(root) != -1
    
    def helper(self,root):
        if root == None:
            return 0
        
        leftHeight = self.helper(root.left)
        if leftHeight == -1:
            return -1
            
        rightHeight = self.helper(root.right)
        if rightHeight == -1:
            return -1
            
        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight,rightHeight) + 1        



class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        
        if  abs(self.helper(root.left)-self.helper(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def helper(self,root):
        if root == None:
            return 0
        
        return max(self.helper(root.left),self.helper(root.right)) +1




# Binary Tree Level Order Traversal

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        queue = [root]        
        while len(queue) > 0:
            curlevel = []
            nextlevel = []
            for node in queue:
                curlevel.append(node.val)
                if node.left != None:
                    nextlevel.append(node.left) 
                if node.right != None:
                    nextlevel.append(node.right) 
            
            result.append(curlevel)
            queue = nextlevel
        
        return result   


class Solution2:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        self.levelHelper(root,0,result)
        return result
    
    def levelHelper(self,root,level,result):
        # if root == None:
        #     return 
        # else:
        if len(result) > level:
            result[level].append(root.val)
        else:
            result.append([root.val])
        if root.left != None:
            self.levelHelper(root.left, level+1,result)
            
        if root.right != None:    
            self.levelHelper(root.right, level+1,result)     
            


# Binary Tree Zigzag Level Order Traversal

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
        
        queue = [root]
        reverse = False
        while len(queue) > 0:
            curlevel = []
            nextlevel = []
            for node in queue:
                curlevel.append(node.val)
                if node.left != None:
                    nextlevel.append(node.left)
                if node.right != None:
                    nextlevel.append(node.right)
            
            if reverse:
                curlevel.reverse()
                reverse = False
            else:
                reverse = True
            
            result.append(curlevel)
            queue = nextlevel
                
        return result        



# Word Ladder
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        fifo = [(start,1)]
        met = set()
        while fifo:
            current = fifo.pop(0)
            for i in range(0,len(current[0])):
                str1 = current[0][:i]
                str2 = current[0][i+1:]
                for c in characters:
                    next_str = str1 + c + str2
                    if next_str == end:
                        return current[1]+1
                    if next_str in dict:
                        if next_str not in met:
                            met.add(next_str)
                            fifo.append((next_str,current[1]+1))
        return 0





# Convert Sorted List to Binary Search Tree
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.arrayToBST(array)
    
    
    def arrayToBST(self,array):
        length = len(array)
        root = None
        if length == 0:
            return root
        elif length == 1:
            root = TreeNode(array[0])
            return root
        else:
            root = TreeNode(array[length/2])
            root.left = self.arrayToBST(array[:length/2])
            root.right = self.arrayToBST(array[length/2+1:])
        return root
        

# do not use any extra space
class Solution2:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        fast = head
        slow = head
        pre = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


# Sqrt(x)
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 1:
            return x
        min = 1
        max = x
        mid = min
        while min <= max:
            mid = (min+max)/2
            if mid == min:
                return mid
            if mid**2 > x:
                max = mid
            elif mid**2 == x:
                return mid
            else:
                min = mid
            
                
        return mid

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self,x):
        min = 0
        max = x
        while min < max:
            mid = (min + max)/2+1
            if mid ** 2 > x:
                max = mid -1
            elif mid ** 2 == x:
                return mid
            else:
                min = mid
        return max # or return min


# Pow(x, n)
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.pow(x,-n)
        elif n % 2 == 0:
            return self.pow(x*x, n/2)
        else:
            return self.pow(x*x, n/2)*x
            
 


# Add Binary
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        flag = 0
        s = ''
        a_len = len(a)
        b_len = len(b)
        while a_len > 0 and b_len > 0:
            sum = int(a[a_len-1])+int(b[b_len-1])+flag
            flag = sum/2
            s = str(sum%2) + s
            a_len -= 1
            b_len -= 1
            
        while a_len > 0:
            sum = int(a[a_len - 1]) + flag
            flag = sum/2
            s = str(sum%2) + s
            a_len -= 1
            
        while b_len > 0:
            sum = int(b[b_len -1]) + flag
            flag = sum/2
            s = str(sum%2) + s
            b_len -= 1
            
        if flag == 1:
            s = str(1) + s
            
        return s
            
        

# Divide Two Integers
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        flag = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) :
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
            
        i = 0
        while dividend >= divisor:
            small = divisor
            count = 1
            while small + small < dividend:
                small += small
                count += count
            dividend -= small
            i += count
        if flag == 0:
            return i if i < 2**31-1 else 2**31-1
        else:
            return -i if -i > -2**31 else -2**31
    
    
        
    
    
# Factorial Trailing Zeroes
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        x = 5
        result = 0
        while n >= x:
            result += n/x
            x *= 5
            
        return result      
        



# Gray Code
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        result = self.grayCode(n-1)
        number = 1 << (n-1)
        result2 = []
        for elem in result:
            result2.append(elem + number)
        
        return result + result2        



# Generate Parentheses


class Solution1:
    # DFS searching all possible solutions
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        if n == 0:
            return []
        self.helper(n,n,'',result)
        return result
    
    def helper(self,left,right,chosen,result):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(chosen)
        if left > 0:
            self.helper(left-1,right,chosen+"(",result)
        if right > 0:
            self.helper(left,right-1,chosen+")",result)        



class Solution2:
    # recursive backtracking!!
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        if n == 0:
            return []
        self.helper(n,n,'',result)
        return result
    
    def helper(self,left,right,chosen,result):
        if left > right:
            return
        elif left == 0:
            if right == 0:
                result.append(chosen)
            else:
                self.helper(left,right-1,chosen+")",result)
        else:
            self.helper(left-1,right,chosen+"(",result)
            self.helper(left,right-1,chosen+")",result)




# Permutations
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        result = []    
        self.helper(num,[],result)
        return result
        
    def helper(self,num,chosen,result):
        if len(chosen) == len(num):
            result.append(chosen)
        else:
            for elem in num:
                if elem not in set(chosen):
                    self.helper(num,chosen+[elem],result)


# Combinations
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        self.helper(1,n,k,[],result)
        return result
    
    def helper(self,start,n,k,chosen,result):
        if len(chosen) == k:
            result.append(chosen)
            return
        for i in xrange(start,n+1):
            self.helper(i+1,n,k,chosen+[i],result)




# Subsets
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = [[]]
        for elem in sorted(S):
            new_val = []
            for val in result:
                new_val.append(val + [elem])
            result += new_val
        return result   

class Solution2:
    def subsets(self,S):
        S.sort()
        result = []
        self.helper(result,0,S,[])
        return result
        
    def helper(self,result,start,S,chosen):
        result.append(chosen)
        if start == len(S):
            return
        else:
            for i in range(start,len(S)):
                self.helper(result,i+1,S,chosen + [S[i]])         



class Solution3:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): 
                return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res



# Subsets II 
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        result = []
        self.helper(S,0,[],result)
        return result
    
    def helper(self,S,start,chosen,result):
        if chosen not in result:
            result.append(chosen)
        if start == len(S):
            return
        else:
            for i in range(start,len(S)):
                self.helper(S,i+1,chosen+[S[i]],result)




# Combination Sum
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.helper(result,[],0, candidates,target)
        return result
        
    def helper(self,result,chosen,start, candidates,target):
        if 0 > target:
            return 
        if 0 == target:
            result.append(chosen)
        else:
            length = len(candidates)
            for i in range(start,length):
                if candidates[i] > target:
                    return
                self.helper(result,chosen+[candidates[i]],i,candidates,target-candidates[i])
                
            
# Letter Combinations of a Phone Number 
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        result = []
        if len(digits) == 0:
            return result
        self.helper(0,dict,digits,'',result)
        return result
        
    def helper(self,start,dict,digits,chosen,result):
        if start == len(digits):
            result.append(chosen)
        else:
            letters = dict[digits[start]]
            for i in range(len(letters)):
                self.helper(start+1,dict,digits,chosen+letters[i],result)


# Palindrome Partitioning
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        if len(s) == 0:
            return result
        self.dfs(result,s,[])
        return result
    
    def dfs(self,result,s,chosen):
        if len(s) == 0:
            result.append(chosen)
        else:
            for i in range(len(s)):
                if self.isPal(s[:i+1]):
                    self.dfs(result,s[i+1:],chosen+[s[:i+1]])
    
    def isPal(self,s):
        length = len(s)
        for i in range(1+length/2):
            if s[i] != s[length-1-i]:
                return False
        return True






# Search for a Range
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        index = self.helper(A,0,len(A)-1,target)
        if index == -1:
            return [-1,-1]
        index1 = index
        index2 = index
        for i in range(0,index+1):
            if A[i] == target:
                index1 = i
                break
        for i in range(len(A)-1,index-1,-1):
            if A[i] == target:
                index2 = i
                break
        return [index1,index2]        


    def helper(self,A,start,end,target):
        if start > end:
            return -1
        mid = (start+end)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.helper(A,start,mid-1,target)
        else:
            return self.helper(A,mid+1,end,target)    





class Solution2:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        index = self.helper(A,0,len(A)-1,target)
        if index == -1:
            return [-1,-1]
        index1 = self.searchLeft(A,0,index,target)
        index2 = self.searchRight(A,index,len(A)-1,target)
        return [index1,index2]
        
    def helper(self,A,start,end,target):
        if start > end:
            return -1
        mid = (start+end)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.helper(A,start,mid-1,target)
        else:
            return self.helper(A,mid+1,end,target)
            
    def searchLeft(self,A,start,end,target):
        if start == end:
            return start
        mid = (start + end)/2
        if A[mid] == target:
            return self.searchLeft(A,start,mid,target)
        else:
            return self.searchLeft(A,mid+1,end,target)
            
    def searchRight(self,A,start,end,target):
        if start == end:
            return start
        mid = (start + end)/2+1
        if A[mid] == target:
            return self.searchRight(A,mid,end,target)
        else:
            return self.searchRight(A,start,mid-1,target)






# Search in Rotated Sorted Array
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        index = 0
        if len(A) != 1:
            index = self.findPivot(A,0,len(A)-1)
        result = self.binarySearch(A,0,index,target)
        if result == -1:
            result = self.binarySearch(A,index,len(A)-1,target)
        return result
    
    def findPivot(self,A,start,end):
        if start == end:
            return 0
        mid = (start + end)/2
        if A[mid] > A[mid+1]:
            return mid+1
        else:
            left = self.findPivot(A,start,mid)
            right = self.findPivot(A,mid+1,end)
            if left == 0:
                return right
            else:
                return left
    
    def binarySearch(self,A,start,end,target):
        if start > end:
            return -1
        mid = (start + end)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.binarySearch(A,start,mid-1,target)
        else:
            return self.binarySearch(A,mid+1,end,target)

  
class Solution2:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        index = 0
        if len(A) != 1:
            index = self.findPivot(A,0,len(A)-1)
        result = self.binarySearch(A,0,index,target)
        if result == -1:
            result = self.binarySearch(A,index,len(A)-1,target)
        return result
    
    def findPivot(self,A,start,end):
        mid = (start + end)/2
        if A[mid] > A[mid+1]:
            return mid+1
        elif A[mid] > A[end]:
            return self.findPivot(A,mid,end)
        elif A[mid] < A[start]:
            return self.findPivot(A,start,mid)
        else:
            return start
    
    def binarySearch(self,A,start,end,target):
        if start > end:
            return -1
        mid = (start + end)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            return self.binarySearch(A,start,mid-1,target)
        else:
            return self.binarySearch(A,mid+1,end,target)

            

class Solution3:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0 
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[mid] >= A[left]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1   



# Search in Rotated Sorted Array II  
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        index = 0
        if len(A) != 1:
            index = self.findPivot(A,0,len(A)-1)
        result = self.binarySearch(A,0,index,target)
        if result == False:
            result = self.binarySearch(A,index,len(A)-1,target)
        return result
    
    def findPivot(self,A,start,end):
        if start > end:
            return 0
        mid = (start + end)/2
        if A[mid] == A[start] and A[start] == A[end]:
            return self.findPivot(A,start+1,end)  
        elif A[mid] > A[mid+1]:
            return mid+1
        elif A[mid] > A[end]:
            return self.findPivot(A,mid,end)
        elif A[mid] < A[start]:
            return self.findPivot(A,start,mid)
        else:
            return start
    
    def binarySearch(self,A,start,end,target):
        if start > end:
            return False
        mid = (start + end)/2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            return self.binarySearch(A,start,mid-1,target)
        else:
            return self.binarySearch(A,mid+1,end,target)        



class Solution2:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left=0
        right=len(A)-1
        while left<=right:
            mid=(left+right)/2
            if A[mid]==target: 
                return True
            if A[left]==A[mid]==A[right]:
                left+=1
                right-=1
            elif A[left]<=A[mid]:
                if A[left]<=target<A[mid]: 
                    right=mid-1
                else: 
                    left=mid+1
            else:
                if A[mid]<=target<A[left]: 
                    left=mid+1
                else:
                    right=mid-1
        return False

        
class Solution3:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        index = self.findPivot(A,0,len(A)-1)
        result = self.binarySearch(A,0,index-1,target)
        if result == False:
            result = self.binarySearch(A,index,len(A)-1,target)
        return result
    
    def findPivot(self,A,start,end):
        while start < end and A[start] >= A[end]:
            mid = (start + end)/2
            if A[mid] == A[start] == A[end]:
                start += 1
            elif A[mid] > A[end]:
                start = mid + 1
                if A[mid+1] < A[mid]:
                    break
            else:
                end = mid
        return start
    
    def binarySearch(self,A,start,end,target):
        if start > end:
            return False
        mid = (start + end)/2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            return self.binarySearch(A,start,mid-1,target)
        else:
            return self.binarySearch(A,mid+1,end,target)        



# Remove Duplicates from Sorted Array
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length == 0:
            return 0
        j = 0
        for i in range(0,length):
            if A[i] != A[j]:
                if i != j+1:
                    tmp = A[i]
                    A[i] = A[j+1]
                    A[j+1] = tmp
                j += 1
        return j+1



# Find Minimum in Rotated Sorted Array
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        while start < end and num[start] > num[end]:
            mid = (start + end)/2
            if num[mid] > num[end]:
                start = mid +1
            else:
                end = mid
        return num[start]        



# Find Minimum in Rotated Sorted Array II 
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num)-1
        while start < end and num[start] >= num[end]:
            mid = (start + end)/2
            if num[start] == num[mid] == num[end]:
                start += 1
            elif num[mid] > num[end]:
                start = mid +1
            else:
                end = mid
        return num[start]



# Climbing Stairs
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]