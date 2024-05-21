class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        s = ''
        
        while num > 0:
            num_str = str(num)[0]
            if num_str in ['4', '9']:
                s, num = self.get_special(num)
            else:
                s, num = self.get_section(num)
            
            result.append(s)

        return ''.join(result)

    def get_section(self, num):
        val = ''
        if num >= 1000:
            num -= 1000
            val = 'M'
        elif num >= 500:
            val = 'D'
            num -= 500
        elif num >= 100:
            val = 'C'
            num -= 100
        elif num >= 50:
            val = 'L'
            num -= 50
        elif num >= 10:
            val = 'X'
            num -= 10
        elif num >= 5:
            val = 'V'
            num -= 5
        elif num >= 1:
            val ='I'
            num -= 1 

        return (val, num)
    
    def get_special(self, num):
        my_dict = {900:'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
        for key, val in my_dict.items():
            if key <= num:
                num -= key
                return (val, num)


