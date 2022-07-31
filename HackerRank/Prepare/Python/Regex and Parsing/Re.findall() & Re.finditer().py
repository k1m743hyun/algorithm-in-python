# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'

result = re.findall("(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), flags=re.I)

print('\n'.join(result or ['-1']))
