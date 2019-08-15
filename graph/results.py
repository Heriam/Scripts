import datetime
import sys
import matplotlib.pyplot as plt
import re
import numpy as np
from matplotlib.dates import DateFormatter, MinuteLocator

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as logfile:
        trackTwoDelays = []
        trackThreeDelays = []
        bierDelays = []
        bierTestDelays = []
        bierTest5Delays = []
        linkStats = {}
        t1loss    = {1:0,2:0,3:0,4:0}
        t2loss    = {1:0,2:0,3:0,4:0}
        t3loss    = {1:0,2:0,3:0,4:0}
        t4loss    = {1:0,2:0,3:0,4:0}
        t5loss    = {1:0,2:0,3:0,4:0}

        t2Offset = 48
        t3Offset = 61

        t1Delay = 8
        t4Delay = 8
        t5Delay = 14

        pktInterval = 2000

        t1Name = 'Multipath in parallel without snooping'
        t2Name = 'Upper path'
        t3Name = 'Lower path'
        t4Name = 'Multipath in parallel with snooping'
        t5Name = 'Multipath with full replication'


        for line in logfile :
            splitline = line.split(' ')

            if (not line.startswith('2016')) or (not splitline[3].startswith('9')):
                print "Skipping line {0}".format(line)
                continue
                
            date = splitline[0].split('-')
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])

            time = splitline[1].split(':')
            hour = int(time[0])
            min = int(time[1])
            sec = int(time[2].split(',')[0])
            microsec = int(time[2].split(',')[1])*1000

            mote = splitline[3]

            component = splitline[4][1:-1]

            msg = ' '.join(splitline[5:])

            datet = datetime.datetime(year,month,day,hour,min,sec,microsecond=microsec)+datetime.timedelta(hours=2)

            if 'Non-BIER test msg received on track 2. SlotOffset :' in msg :
                delay = int(msg[-3:])-t2Offset
                if delay < 4 or delay > 12 :
                    delay = -1
                bitmap = ''
                trackTwoDelays += [{'datetime': datet, 'delay' : delay, 'bitmap' : bitmap}]

            elif 'Non-BIER test msg received on track 3. SlotOffset :' in msg :
                delay = int(msg[-3:])-t3Offset
                if delay < 4 or delay > 12 :
                    delay = -1
                bitmap = ''
                trackThreeDelays += [{'datetime': datet, 'delay' : delay, 'bitmap' : bitmap}]

            elif 'BIER message forwarded to upper layer. First 16 bits of the bitmap :' in msg :
                delay = t1Delay
                bitmap = msg[-17:]
                bierDelays += [{'datetime':datet, 'delay' : delay, 'bitmap': bitmap}]

            elif 'BIER test msg received on track 4' in msg :
                delay = t4Delay
                bitmap = msg[-17:]
                bierTestDelays += [{'datetime':datet, 'delay' : delay, 'bitmap': bitmap}]

            elif 'BIER test msg received on track 5' in msg:
                delay = t5Delay
                bitmap = msg[-17:]
                bierTest5Delays += [{'datetime': datet, 'delay': delay, 'bitmap': bitmap}]

            elif 'TX stats of slot' in msg :
                nums = map(int, re.findall(r'\d+', msg))
                if not linkStats.has_key(mote) :
                    linkStats[mote]={}
                if not linkStats[mote].has_key(nums[0]) :
                    linkStats[mote][nums[0]] = {'tx' : 0, 'ack' : 0,'rx' : 0}
                linkStats[mote][nums[0]]['tx'] += nums[1]
                linkStats[mote][nums[0]]['ack'] += nums[2]

            elif 'RX stats of slot' in msg :
                nums = map(int, re.findall(r'\d+', msg))
                if not linkStats.has_key(mote) :
                    linkStats[mote]={}
                if not linkStats[mote].has_key(nums[0]) :
                    linkStats[mote][nums[0]] = {'tx' : 0, 'ack' : 0,'rx' : 0}
                linkStats[mote][nums[0]]['rx'] += nums[1]

        print linkStats

        newtrackTwoDelays = trackTwoDelays[:]
        for i in range(len(trackTwoDelays)-1):
            losslist = []
            datet = trackTwoDelays[i]['datetime']
            while datet + datetime.timedelta(milliseconds=2*pktInterval) < trackTwoDelays[i + 1]['datetime'] :
                datet += datetime.timedelta(milliseconds=pktInterval)
                losslist += [{'datetime': datet, 'delay': -1, 'bitmap' : ''}]
            newtrackTwoDelays = newtrackTwoDelays[:newtrackTwoDelays.index(trackTwoDelays[i])+1] + losslist + newtrackTwoDelays[newtrackTwoDelays.index(trackTwoDelays[i])+1:]
        trackTwoDelays = newtrackTwoDelays

        newtrackThreeDelays = trackThreeDelays[:]
        for i in range(len(trackThreeDelays)-1):
            losslist = []
            datet = trackThreeDelays[i]['datetime']
            while datet + datetime.timedelta(milliseconds=2*pktInterval) < trackThreeDelays[i + 1]['datetime'] :
                datet += datetime.timedelta(milliseconds=pktInterval)
                losslist += [{'datetime': datet, 'delay': -1, 'bitmap' : ''}]
            newtrackThreeDelays = newtrackThreeDelays[:newtrackThreeDelays.index(trackThreeDelays[i])+1] + losslist + newtrackThreeDelays[newtrackThreeDelays.index(trackThreeDelays[i])+1:]
        trackThreeDelays = newtrackThreeDelays

        newbierDelays = bierDelays[:]
        for i in range(len(bierDelays)-1):
            losslist = []
            datet = bierDelays[i]['datetime']
            while datet + datetime.timedelta(milliseconds=2*pktInterval) < bierDelays[i + 1]['datetime'] :
                datet += datetime.timedelta(milliseconds=pktInterval)
                losslist += [{'datetime': datet, 'delay': -1, 'bitmap' : ''}]
            newbierDelays = newbierDelays[:newbierDelays.index(bierDelays[i])+1] + losslist + newbierDelays[newbierDelays.index(bierDelays[i])+1:]
        bierDelays = newbierDelays

        newbierTestDelays = bierTestDelays[:]
        for i in range(len(bierTestDelays) - 1):
            losslist = []
            datet = bierTestDelays[i]['datetime']
            while datet + datetime.timedelta(milliseconds=2 * pktInterval) < bierTestDelays[i + 1]['datetime']:
                datet += datetime.timedelta(milliseconds=pktInterval)
                losslist += [{'datetime': datet, 'delay': -1, 'bitmap': ''}]
            newbierTestDelays = newbierTestDelays[:newbierTestDelays.index(bierTestDelays[i]) + 1] + losslist + newbierTestDelays[
                                                                                                newbierTestDelays.index(
                                                                                                    bierTestDelays[i]) + 1:]
        bierTestDelays = newbierTestDelays

        newbierTest5Delays = bierTest5Delays[:]
        for i in range(len(bierTest5Delays) - 1):
            losslist = []
            datet = bierTest5Delays[i]['datetime']
            while datet + datetime.timedelta(milliseconds=2 * pktInterval) < bierTest5Delays[i + 1]['datetime']:
                datet += datetime.timedelta(milliseconds=pktInterval)
                losslist += [{'datetime': datet, 'delay': -1, 'bitmap': ''}]
            newbierTest5Delays = newbierTest5Delays[
                                :newbierTest5Delays.index(bierTest5Delays[i]) + 1] + losslist + newbierTest5Delays[
                                                                                              newbierTest5Delays.index(
                                                                                                  bierTest5Delays[
                                                                                                      i]) + 1:]
        bierTest5Delays = newbierTest5Delays

        i = 0
        while True:
            if bierDelays[i].get('delay') == -1:
                if bierDelays[i+1].get('delay') != -1:
                    t1loss[1] += 1
                    i += 2
                elif bierDelays[i+2].get('delay') != -1:
                    t1loss[2] += 1
                    i += 3
                elif bierDelays[i+3].get('delay') != -1:
                    t1loss[3] += 1
                    i += 4
                else:
                    while bierDelays[i+4].get('delay') == -1:
                        i +=1
                    t1loss[4] += 1
                    i += 5
            else:
                i += 1
            if i+3 >= len(bierDelays):
                break

        i = 0
        while True:
            if trackTwoDelays[i].get('delay') == -1:
                if trackTwoDelays[i+1].get('delay') != -1:
                    t2loss[1] += 1
                    i += 2
                elif trackTwoDelays[i+2].get('delay') != -1:
                    t2loss[2] += 1
                    i += 3
                elif trackTwoDelays[i+3].get('delay') != -1:
                    t2loss[3] += 1
                    i += 4
                else:
                    while trackTwoDelays[i+4].get('delay') == -1:
                        i +=1
                    t2loss[4] += 1
                    i += 5
            else:
                i += 1
            if i+3 >= len(trackTwoDelays):
                break

        i = 0
        while True:
            if trackThreeDelays[i].get('delay') == -1:
                if trackThreeDelays[i + 1].get('delay') != -1:
                    t3loss[1] += 1
                    i += 2
                elif trackThreeDelays[i + 2].get('delay') != -1:
                    t3loss[2] += 1
                    i += 3
                elif trackThreeDelays[i + 3].get('delay') != -1:
                    t3loss[3] += 1
                    i += 4
                else:
                    while trackThreeDelays[i+4].get('delay') == -1:
                        i +=1
                    t3loss[4] += 1
                    i += 5
            else:
                i += 1
            if i+3 >= len(trackThreeDelays):
                break

        i = 0
        while True:
            if bierTestDelays[i].get('delay') == -1:
                if bierTestDelays[i + 1].get('delay') != -1:
                    t4loss[1] += 1
                    i += 2
                elif bierTestDelays[i + 2].get('delay') != -1:
                    t4loss[2] += 1
                    i += 3
                elif bierTestDelays[i + 3].get('delay') != -1:
                    t4loss[3] += 1
                    i += 4
                else:
                    while bierTestDelays[i+4].get('delay') == -1:
                        i +=1
                    t4loss[4] += 1
                    i += 5
            else:
                i += 1
            if i+3 >= len(bierTestDelays):
                break

        i = 0
        while True:
            if bierTest5Delays[i].get('delay') == -1:
                if bierTest5Delays[i + 1].get('delay') != -1:
                    t5loss[1] += 1
                    i += 2
                elif bierTest5Delays[i + 2].get('delay') != -1:
                    t5loss[2] += 1
                    i += 3
                elif bierTest5Delays[i + 3].get('delay') != -1:
                    t5loss[3] += 1
                    i += 4
                else:
                    while bierTest5Delays[i+4].get('delay') == -1:
                        i +=1
                    t5loss[4] += 1
                    i += 5
            else:
                i += 1
            if i+3 >= len(bierTest5Delays):
                break

        trackTwoDelayStats = {}
        for delay in trackTwoDelays :
            if trackTwoDelayStats.has_key(delay['delay']) :
                trackTwoDelayStats[delay['delay']] += 1
            else :
                trackTwoDelayStats[delay['delay']] = 1
        
        print trackTwoDelayStats
        print 'total : {0}'.format(len(trackTwoDelays))

        trackThreeDelayStats = {}
        for delay in trackThreeDelays:
            if trackThreeDelayStats.has_key(delay['delay']):
                trackThreeDelayStats[delay['delay']] += 1
            else:
                trackThreeDelayStats[delay['delay']] = 1

        print trackThreeDelayStats
        print 'total : {0}'.format(len(trackThreeDelays))

        bierDelayStats = {}
        for delay in bierDelays:
            if bierDelayStats.has_key(delay['delay']):
                bierDelayStats[delay['delay']] += 1
            else:
                bierDelayStats[delay['delay']] = 1

        print bierDelayStats
        print 'total : {0}'.format(len(bierDelays))

        bierTestDelayStats = {}
        for delay in bierTestDelays:
            if bierTestDelayStats.has_key(delay['delay']):
                bierTestDelayStats[delay['delay']] += 1
            else:
                bierTestDelayStats[delay['delay']] = 1

        print bierTestDelayStats
        print 'total : {0}'.format(len(bierTestDelays))

        bierTest5DelayStats = {}
        for delay in bierTest5Delays:
            if bierTest5DelayStats.has_key(delay['delay']):
                bierTest5DelayStats[delay['delay']] += 1
            else:
                bierTest5DelayStats[delay['delay']] = 1

        print bierTest5DelayStats
        print 'total : {0}'.format(len(bierTest5Delays))

        print trackTwoDelayStats
        print trackThreeDelayStats



        f1 = plt.figure()
        ax = f1.add_subplot(111)
        ax.plot([d['datetime'] for d in trackTwoDelays], [d['delay'] for d in trackTwoDelays], marker='+', linestyle='None')
        plt.ylim((-2,20))
        plt.ylabel('Delay (time slots)')
        plt.xlabel('Time')
        plt.title(t2Name)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

        f2 = plt.figure()
        ax = f2.add_subplot(111)
        ax.plot([d['datetime'] for d in trackThreeDelays], [d['delay'] for d in trackThreeDelays], marker='+', linestyle='None')

        plt.ylim((-2,20))
        plt.ylabel('Delay (time slots)')
        plt.xlabel('Time')
        plt.title(t3Name)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

        f3 = plt.figure()
        ax = f3.add_subplot(111)
        ax.plot([d['datetime'] for d in bierDelays], [d['delay'] for d in bierDelays], marker='+', linestyle='None')

        plt.ylim((-2,20))
        plt.ylabel('Delay (time slots)')
        plt.xlabel('Time')
        plt.title(t1Name)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

        f4 = plt.figure()
        ax = f4.add_subplot(111)
        ax.plot([d['datetime'] for d in bierTestDelays], [d['delay'] for d in bierTestDelays], marker='+', linestyle='None')

        plt.ylim((-2,20))
        plt.ylabel('Delay (time slots)')
        plt.xlabel('Time')
        plt.title(t4Name)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

        f5 = plt.figure()
        ax = f5.add_subplot(111)
        ax.plot([d['datetime'] for d in bierTest5Delays], [d['delay'] for d in bierTest5Delays], marker='+', linestyle='None')
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

        plt.ylim((-2, 20))
        plt.ylabel('Delay (time slots)')
        plt.xlabel('Time')
        plt.title(t5Name)

        for i in trackTwoDelayStats.keys() :
            trackTwoDelayStats[i] *= (100.0/len(trackTwoDelays))

        f6 = plt.figure()
        plt.bar([d - 0.3 for d in trackTwoDelayStats.keys()], trackTwoDelayStats.values(), color='r', width=0.3, label=t2Name)
        plt.ylim((0,100))
        plt.xlim((-2,20))
        plt.ylabel('Frequency')
        plt.xlabel('Delay')
        # plt.plot([-2, 20], [trackTwoDelayStats[4],trackTwoDelayStats[4]], "k--")
        #plt.title('Upper path')
        
        for i in trackThreeDelayStats.keys() :
            trackThreeDelayStats[i] *= (100.0/len(trackThreeDelays))

        #f5 = plt.figure()
        plt.bar([d - 0.6 for d in trackThreeDelayStats.keys()], trackThreeDelayStats.values(), color='b', width=0.3, label=t3Name)
        plt.ylim((0,100))
        plt.xlim((-2,20))
        plt.ylabel('Frequency')
        plt.xlabel('Delay')
        #plt.title('Lower path')

        for i in bierDelayStats.keys() :
            bierDelayStats[i] *= (100.0/len(bierDelays))

        #f6=plt.figure()
        plt.bar([d + 0 for d in bierDelayStats.keys()], bierDelayStats.values(), color='g', width=0.3, label=t1Name)
        plt.ylim((0,100))
        plt.xlim((-2,20))
        plt.ylabel('Frequency')
        plt.xlabel('Delay')
        #plt.title('Multipath with replication and elimination')

        for i in bierTestDelayStats.keys():
            bierTestDelayStats[i] *= (100.0 / len(bierTestDelays))

        # f7=plt.figure()
        plt.bar([d + 0.3 for d in bierTestDelayStats.keys()], bierTestDelayStats.values(), color='y', width=0.3, label=t4Name)
        plt.ylim((0, 100))
        plt.xlim((-2, 20))
        plt.ylabel('Frequency')
        plt.xlabel('Delay')
        # plt.plot([-2, 20], [bierTest5DelayStats[t5Delay], bierTest5DelayStats[t5Delay]], "k--")
        # plt.title('Multipath without replication and elimination')


        for i in bierTest5DelayStats.keys():
            bierTest5DelayStats[i] *= (100.0 / len(bierTest5Delays))

        # f7=plt.figure()
        plt.bar([d + 0.6 for d in bierTest5DelayStats.keys()], bierTest5DelayStats.values(), color='m', width=0.3, label=t5Name)
        plt.ylim((0, 100))
        plt.xlim((-2, 20))
        plt.ylabel('Frequency')
        plt.xlabel('Delay')
        # plt.plot([-2, 20], [bierTest5DelayStats[t5Delay], bierTest5DelayStats[t5Delay]], "k--")
        plt.legend(loc=2)
        plt.title('Frequency-Delay(timeslots) Graph')

        # for i in t2loss.keys():
        #     t2loss[i] *= (100.0 / len(trackTwoDelays))

        f7 = plt.figure()
        plt.bar([d - 0.2 for d in t2loss.keys()], t2loss.values(), color='r', width=0.1,
                label=t2Name)
        plt.xlim((0, 5))
        plt.ylabel('Occurrence among {0} packets'.format(len(bierDelays)))
        plt.xlabel('Number of loss in a row')
        #
        # for i in t3loss.keys():
        #     t3loss[i] *= (100.0 / len(trackThreeDelays))

        plt.bar([d + 0 for d in t3loss.keys()], t3loss.values(), color='b', width=0.1,
                label=t3Name)
        plt.xlim((0, 5))
        # plt.ylabel('Occurrence rate')
        # plt.xlabel('Number of loss in a row')
        #
        # for i in t1loss.keys():
        #     t1loss[i] *= (100.0 / len(bierDelays))

        plt.bar([d - 0.1 for d in t1loss.keys()], t1loss.values(), color='g', width=0.1,
                label=t1Name)
        plt.xlim((0, 5))
        # plt.ylabel('Occurrence rate')
        # plt.xlabel('Number of loss in a row')
        #
        # for i in t4loss.keys():
        #     t4loss[i] *= (100.0 / len(bierTestDelays))

        plt.bar([d + 0.1 for d in t4loss.keys()], t4loss.values(), color='y', width=0.1,
                label=t4Name)
        plt.xlim((0, 5))
        # plt.ylabel('Occurrence rate')
        # plt.xlabel('Number of loss in a row')
        #
        # for i in t5loss.keys():
        #     t5loss[i] *= (100.0 / len(bierTest5Delays))

        plt.bar([d + 0.2 for d in t5loss.keys()], t5loss.values(), color='m', width=0.1,
                label=t5Name)
        plt.xlim((0, 5))
        # plt.ylabel('Occurrence rate')
        # plt.xlabel('Number of loss in a row')

        plt.legend(loc=0)
        # plt.title('Occurrence rate - Number of loss in a row')

        plt.show()
