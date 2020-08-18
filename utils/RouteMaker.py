import random
ip_list = []
if __name__ == '__main__':
    with open('route.txt','w+') as file:
        while len(ip_list) < 100000:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1, 9)
            e = random.randint(1, 9)
            f = random.randint(1, 9)
            g = random.randint(1, 9)
            h = random.randint(1, 9)
            i = random.randint(1, 9)
            j = random.randint(1, 9)
            k = random.randint(1, 9)
            l = random.randint(1, 9)
            m = random.randint(1, 9)
            n = random.randint(1, 9)
            o = random.randint(1, 9)
            p = random.randint(1, 9)
            ip = '2000::%s%s%s%s:%s%s%s%s:%s%s%s%s:%s%s%s%s' % (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
            if ip not in ip_list:
                ip_list.append(ip)
                file.writelines('ipv6 route-static %s 128 NULL 0\n' % ip)