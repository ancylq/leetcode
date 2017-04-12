# coding:utf-8
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

    n = 15,
    
    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
'''
class Solution(object):
    '''best score:50.75'''
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num_list = range(1, n+1)
        result = []
        for n in num_list:
            s = ''
            if n%3 == 0:
                s += 'Fizz'
            if n%5 == 0:
                s += 'Buzz'
            if s:
                num_list[n-1] = s
        return map(str, num_list)
    
class SolutionGood(object):
    '''best score:95.81'''
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        result = []
        while i <=n:
            s = ''
            if i%3 == 0:
                s += 'Fizz'
            if i%5 == 0:
                s += 'Buzz'
            if s:
                result.append(s)
            else:
                result.append(str(i))
            i += 1
        return result
    
if __name__ == '__main__':
    s = SolutionGood()
    print s.fizzBuzz(15)