from pysnmp.hlapi import *
if __name__=='__main__':
    for i in range(0, 1000):
        errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                       CommunityData('public'),
                       UdpTransportTarget(('3.2.119.1', 161)),
                       ContextData(),
                       ObjectType(ObjectIdentity('1.3.6.1.4.1.25506.2.6.1.1.1.1.18.%s' % i)),
                       ObjectType(ObjectIdentity('1.3.6.1.2.1.17.1.1.%s' % i)))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))