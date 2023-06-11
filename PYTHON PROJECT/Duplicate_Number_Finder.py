def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
        	return True 
        else:
        	return False      		
      
        			
print(containsDuplicate([1,2,3,1])  )			