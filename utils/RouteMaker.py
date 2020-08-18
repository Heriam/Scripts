import random, sys

skip_net = [1,2,3,4,5,6,7,8,9,10,20,30,40,100,127,224,255]
ip_list = []
if __name__ == '__main__':
    with open('route.txt','w+') as f:
        while len(ip_list) < 100000:
            while True:
                byte1 = random.randint(1, 200)
                if byte1 not in skip_net:
                    break
            assert byte1 not in skip_net
            byte2 = random.randint(0,255)
            byte3 = random.randint(0,255)
            byte4 = random.randint(1,254)
            ip = '%s.%s.%s.%s' % (byte1, byte2, byte3, byte4)
            if ip not in ip_list:
                ip_list.append(ip)
                f.writelines('ip route-static %s 32 NULL 0\n' % ip)