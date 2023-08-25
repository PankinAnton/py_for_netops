# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input("Enter the IP network in the format 10.1.1.0/24:")
ip_mask = ip[ip.find('/')::]
ip_mask_max = 32
ip_mask_empty = int(ip_mask_max) - int(ip_mask.replace("/",""))
ip_mask_bin = "1" * int(ip_mask.replace("/","")) + "0" * ip_mask_empty
mask_ost1, mask_ost2, mask_ost3, mask_ost4 = ip_mask_bin[:8], ip_mask_bin[8:16], ip_mask_bin[16:24], ip_mask_bin[24:]
mask_ost1_dect, mask_ost2_dect, mask_ost3_dect, mask_ost4_dect = int(mask_ost1, 2), int(mask_ost2, 2), int(mask_ost3, 2), int(mask_ost4, 2)

oct1, oct2, oct3, oct4 = list(ip.replace(ip_mask,"").split("."))
ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template.format(int(oct1), int(oct2), int(oct3), int(oct4)))
print("Mask:")
print(ip_mask)
mask_template = '''{0:<8} {1:<8} {2:<8} {3:<8}'''
print(mask_template.format(mask_ost1_dect, mask_ost2_dect, mask_ost3_dect, mask_ost4_dect))
print (mask_ost1, mask_ost2, mask_ost3, mask_ost4)
