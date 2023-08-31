# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

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
ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(int(oct1), int(oct2), int(oct3), int(oct4))
ip_net_bin=ip_bin[0:int(ip_mask.replace("/",""))] + "0" * ip_mask_empty
ip_net_bin1, ip_net_bin2, ip_net_bin3, ip_net_bin4 = ip_net_bin[:8], ip_net_bin[8:16], ip_net_bin[16:24], ip_net_bin[24:]
ip_net_bin1_dect, ip_net_bin2_dect, ip_net_bin3_dect, ip_net_bin4_dect = int(ip_net_bin1, 2), int(ip_net_bin2, 2), int(ip_net_bin3, 2), int(ip_net_bin4, 2)

mask_template = '''{0:<8} {1:<8} {2:<8} {3:<8}'''
print("Network:")
print(mask_template.format(ip_net_bin1_dect, ip_net_bin2_dect, ip_net_bin3_dect, ip_net_bin4_dect))
print(ip_net_bin1, ip_net_bin2, ip_net_bin3, ip_net_bin4)

print("\nMask:")
print(ip_mask)
print(mask_template.format(mask_ost1_dect, mask_ost2_dect, mask_ost3_dect, mask_ost4_dect))
print (mask_ost1, mask_ost2, mask_ost3, mask_ost4)