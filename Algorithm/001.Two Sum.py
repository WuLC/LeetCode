# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-01-21 09:28:43
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:40
# @Email: liangchaowu5@gmail.com


####################################
#解题思路：
# 1. 正则表达式提取字符串中的数字数组和目标和
# 2. 遍历数字数组得到目标和
# 
# Sample IO:
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
####################################

'''
import re

def get_number_from_string(str):
    str_arr=re.findall(r'{(.*)}',str)
    char_arr=str_arr[0].split(',')
    num_arr=[0]
    for c in char_arr:
        num=int(c)
        num_arr.append(num)

    str_tar=re.findall(r'target=(.*)$',str)
    num_tar=int(str_tar[0])

    return num_arr,num_tar

def find_indices(arr,tar):
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == tar:
                print 'index1=%d,index2=%d' %(i,j)
                return i #为了跳出多个for循环，返回值没有具体作用


if __name__ == '__main__':
    str=raw_input()
    array,target=get_number_from_string(str)
    find_indices(array,target)                    

'''

#实际AC通过代码
#只需要写出函数即可

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indice=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    num_indice.append(i+1)
                    num_indice.append(j+1)
                    return num_indice

