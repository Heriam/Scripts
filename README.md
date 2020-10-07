2020-10-07T16:15:00,180 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(339):device[3.2.20.10] reconnet error:Timeout error: 30
        at com.tailf.jnc.SSHSession.readOne(SSHSession.java:180)
        at com.tailf.jnc.NetconfSession.hello(NetconfSession.java:304)
        at com.tailf.jnc.NetconfSession.<init>(NetconfSession.java:220)
        at com.h3c.itoa.entity.NCSession.openSession(NCSession.java:144)
        at com.h3c.itoa.entity.NCSession.reconnetSession(NCSession.java:163)
        at com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(ApiServiceImpl.java:336)
        at com.h3c.itoa.service.impl.ApiServiceImpl.reloadNCSMap(ApiServiceImpl.java:282)
        at com.h3c.itoa.task.reloadSessionTask.reloadNetconfSession(reloadSessionTask.java:23)
        at sun.reflect.GeneratedMethodAccessor123.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.springframework.scheduling.support.ScheduledMethodRunnable.run(ScheduledMethodRunnable.java:65)
        at org.springframework.scheduling.support.DelegatingErrorHandlingRunnable.run(DelegatingErrorHandlingRunnable.java:54)
        at org.springframework.scheduling.concurrent.ReschedulingRunnable.run(ReschedulingRunnable.java:81)
        at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)

2020-10-07T16:15:00,189 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.entity.NCSession.reconnetSession(157):device:0a591ec5-4344-4150-b170-441b2e5e5779 reconneting..
2020-10-07T16:15:00,189 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.entity.NCSession.reconnetSession(161):device:0a591ec5-4344-4150-b170-441b2e5e5779 close failed!
2020-10-07T16:15:00,337 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(339):device[3.2.20.11] reconnet error:Timeout error: 30
        at com.tailf.jnc.SSHSession.readOne(SSHSession.java:180)
        at com.tailf.jnc.NetconfSession.hello(NetconfSession.java:304)
        at com.tailf.jnc.NetconfSession.<init>(NetconfSession.java:220)
        at com.h3c.itoa.entity.NCSession.openSession(NCSession.java:144)
        at com.h3c.itoa.entity.NCSession.reconnetSession(NCSession.java:163)
        at com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(ApiServiceImpl.java:336)
        at com.h3c.itoa.service.impl.ApiServiceImpl.reloadNCSMap(ApiServiceImpl.java:282)
        at com.h3c.itoa.task.reloadSessionTask.reloadNetconfSession(reloadSessionTask.java:23)
        at sun.reflect.GeneratedMethodAccessor123.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.springframework.scheduling.support.ScheduledMethodRunnable.run(ScheduledMethodRunnable.java:65)
        at org.springframework.scheduling.support.DelegatingErrorHandlingRunnable.run(DelegatingErrorHandlingRunnable.java:54)
        at org.springframework.scheduling.concurrent.ReschedulingRunnable.run(ReschedulingRunnable.java:81)
        at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)

2020-10-07T16:15:00,340 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.entity.NCSession.reconnetSession(157):device:a0e48155-59e4-46e4-a56a-603f6d0cf1f2 reconneting..
2020-10-07T16:15:00,342 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.entity.NCSession.reconnetSession(161):device:a0e48155-59e4-46e4-a56a-603f6d0cf1f2 close failed!
2020-10-07T16:15:00,520 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-13-thread-1 com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(339):device[3.2.20.12] reconnet error:Timeout error: 30
        at com.tailf.jnc.SSHSession.readOne(SSHSession.java:180)
        at com.tailf.jnc.NetconfSession.hello(NetconfSession.java:304)
        at com.tailf.jnc.NetconfSession.<init>(NetconfSession.java:220)
        at com.h3c.itoa.entity.NCSession.openSession(NCSession.java:144)
        at com.h3c.itoa.entity.NCSession.reconnetSession(NCSession.java:163)
        at com.h3c.itoa.service.impl.ApiServiceImpl.loadSession(ApiServiceImpl.java:336)
        at com.h3c.itoa.service.impl.ApiServiceImpl.reloadNCSMap(ApiServiceImpl.java:282)
        at com.h3c.itoa.task.reloadSessionTask.reloadNetconfSession(reloadSessionTask.java:23)
        at sun.reflect.GeneratedMethodAccessor123.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.springframework.scheduling.support.ScheduledMethodRunnable.run(ScheduledMethodRunnable.java:65)
        at org.springframework.scheduling.support.DelegatingErrorHandlingRunnable.run(DelegatingErrorHandlingRunnable.java:54)
        at org.springframework.scheduling.concurrent.ReschedulingRunnable.run(ReschedulingRunnable.java:81)
        at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:748)

2020-10-07T16:15:30,000 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:15:30,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:15:30,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:15:30,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-25 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:15:30,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-61 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:15:30,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-42 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:15:48,891 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: http-nio-8082-exec-9 com.h3c.itoa.utils.HttpServletRequestUtil.getUsername(53):get userName ok null
2020-10-07T16:16:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(54):tunnels GET collector start
2020-10-07T16:16:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:16:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(54):device_up_time GET collector start
2020-10-07T16:16:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(54):device_disk_free GET collector start
2020-10-07T16:16:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(54):link_availability GET collector start
2020-10-07T16:16:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:tunnels COLLECT START!
2020-10-07T16:16:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:16:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:16:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:tunnels, deviceCount:3
2020-10-07T16:16:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_up_time COLLECT START!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-10 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:link_availability COLLECT START!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_disk_free COLLECT START!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_up_time, deviceCount:3
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-26 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-65 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_disk_free, deviceCount:3
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-58 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-26 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-11 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-58 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-50 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:link_availability, deviceCount:3
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-60 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-18 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-16 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-68 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-60 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-18 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-48 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:30,000 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:16:30,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:16:30,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:16:30,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-8 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:16:30,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-36 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:16:30,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-46 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:16:48,908 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: http-nio-8082-exec-10 com.h3c.itoa.utils.HttpServletRequestUtil.getUsername(53):get userName ok null
2020-10-07T16:17:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-4 com.h3c.itoa.collect.NetConfGetter.execute(54):tunnels GET collector start
2020-10-07T16:17:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:17:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-9 com.h3c.itoa.collect.NetConfGetter.execute(54):device_up_time GET collector start
2020-10-07T16:17:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(54):link_availability GET collector start
2020-10-07T16:17:00,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(54):device_disk_free GET collector start
2020-10-07T16:17:00,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:17:00,002 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-4 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:tunnels COLLECT START!
2020-10-07T16:17:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:17:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-4 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:tunnels, deviceCount:3
2020-10-07T16:17:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-12 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-54 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-45 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-9 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_up_time COLLECT START!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_disk_free COLLECT START!
2020-10-07T16:17:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-7 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-1 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_disk_free, deviceCount:3
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-52 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-9 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_up_time, deviceCount:3
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-2 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:link_availability COLLECT START!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-10 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:link_availability, deviceCount:3
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-1 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-69 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-2 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-22 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-52 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-63 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-1 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-71 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-17 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:30,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:17:30,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:17:30,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-3 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:17:30,004 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-70 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:17:30,004 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-3 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:17:30,004 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-38 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:17:48,928 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: http-nio-8082-exec-2 com.h3c.itoa.utils.HttpServletRequestUtil.getUsername(53):get userName ok null
2020-10-07T16:18:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(54):tunnels GET collector start
2020-10-07T16:18:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(54):device_up_time GET collector start
2020-10-07T16:18:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(54):ospf_router_id GET collector start
2020-10-07T16:18:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(54):device_disk_free GET collector start
2020-10-07T16:18:00,001 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(54):link_availability GET collector start
2020-10-07T16:18:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_disk_free COLLECT START!
2020-10-07T16:18:00,003 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-5 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_disk_free, deviceCount:3
2020-10-07T16:18:00,004 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:link_availability COLLECT START!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:tunnels COLLECT START!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-20 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:ospf_router_id COLLECT START!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-57 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-2 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:tunnels, deviceCount:3
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-6 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:ospf_router_id, deviceCount:3
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-57 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-7 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:link_availability, deviceCount:3
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(75):serviceName:device_up_time COLLECT START!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-57 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-21 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-57 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-62 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-21 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-40 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-6 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:18:00,005 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-55 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:18:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-28 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:18:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: DefaultQuartzScheduler_Worker-8 com.h3c.itoa.collect.NetConfGetter.execute(76):serviceName:device_up_time, deviceCount:3
2020-10-07T16:18:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-9 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.12 notready!
2020-10-07T16:18:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-49 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.11 notready!
2020-10-07T16:18:00,006 itoa-collect-multi2-78cf75d765-2zns5 NetconfCollector/INFO    /DIAG_LOG: pool-2-thread-72 com.h3c.itoa.collect.NetConfGetter$1.run(85):device:3.2.20.10 notready!

