#!/usr/bin/env python

###############################################################################

import os
import socket
import sys

import pdb
import rrdtool

###############################################################################

if __name__ == "__main__":

	filepath = '/nfshome0/troskajk/tcds/monitoring/'
	for crate in ['s1e02-36','s1e02-27','s1e02-18','s1e02-10','s1e03-36','s1e03-27','s1e03-18']:

		for sched in ['daily' , 'weekly', 'monthly']:
			if sched == 'weekly':
				period = 'w'
			elif sched == 'daily':
				period = 'd'
			elif sched == 'monthly':
				period = 'm'
			ret = rrdtool.graph( "{0}{1}-{2}-temp.png".format(filepath,crate,period), 
				"--start", "-1{0}".format(period), 
				"--vertical-label=Temperature (degC)",
				 "-w 400", "-h 200",
				 "-t Crate {0}".format(crate),
				 "DEF:t1={0}{1}.rrd:AMC1temp:AVERAGE".format(filepath,crate),
				 "DEF:t2={0}{1}.rrd:AMC2temp:AVERAGE".format(filepath,crate),
				 "DEF:t3={0}{1}.rrd:AMC3temp:AVERAGE".format(filepath,crate),
				 "DEF:t4={0}{1}.rrd:AMC4temp:AVERAGE".format(filepath,crate),
				 "DEF:t5={0}{1}.rrd:AMC5temp:AVERAGE".format(filepath,crate),
				 "DEF:t6={0}{1}.rrd:AMC6temp:AVERAGE".format(filepath,crate),
				 "DEF:t7={0}{1}.rrd:AMC7temp:AVERAGE".format(filepath,crate),
				 "DEF:t8={0}{1}.rrd:AMC8temp:AVERAGE".format(filepath,crate),
				 "DEF:t9={0}{1}.rrd:AMC9temp:AVERAGE".format(filepath,crate),
				 "DEF:t10={0}{1}.rrd:AMC10temp:AVERAGE".format(filepath,crate),
				 "DEF:t11={0}{1}.rrd:AMC11temp:AVERAGE".format(filepath,crate),
				 "DEF:t12={0}{1}.rrd:AMC12temp:AVERAGE".format(filepath,crate),
				 "DEF:t13={0}{1}.rrd:AMC13temp:AVERAGE".format(filepath,crate),
				 "DEF:t14={0}{1}.rrd:CU1temp:AVERAGE".format(filepath,crate),
				 "DEF:t15={0}{1}.rrd:CU2temp:AVERAGE".format(filepath,crate),
				 "LINE:t1#000000:AMC1",
				 "LINE:t2#FF0000:AMC2",
				 "LINE:t3#FF6600:AMC3",
				 "LINE:t4#FFFF00:AMC4",
				 "LINE:t5#99CC00:AMC5",
				 "LINE:t6#00FF00:AMC6",
				 "LINE:t7#00CC99:AMC7",
				 "LINE:t8#0099CC:AMC8",
				 "LINE:t9#0000FF:AMC9",
				 "LINE:t10#6600FF:AMC10",
				 "LINE:t11#FF00FF:AMC11",
				 "LINE:t12#FF0099:AMC12",
				 "LINE:t13#FF99CC:AMC13",
				 "LINE:t14#CC0000:CU1",
				 "LINE:t15#660000:CU2",)
			
			ret = rrdtool.graph( "{0}{1}-{2}-curr.png".format(filepath,crate,period), 
				"--start", "-1{0}".format(period), 
				"--vertical-label=Current (A)",
				 "-w 400", "-h 200",
				 "--upper-limit=3.0", "--lower-limit=0.0","--rigid",
				 "-t Crate {0}".format(crate),
				 "DEF:t1={0}{1}.rrd:AMC1curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t2={0}{1}.rrd:AMC2curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t3={0}{1}.rrd:AMC3curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t4={0}{1}.rrd:AMC4curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t5={0}{1}.rrd:AMC5curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t6={0}{1}.rrd:AMC6curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t7={0}{1}.rrd:AMC7curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t8={0}{1}.rrd:AMC8curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t9={0}{1}.rrd:AMC9curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t10={0}{1}.rrd:AMC10curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t11={0}{1}.rrd:AMC11curr1V0:AVERAGE".format(filepath,crate),
				 "DEF:t12={0}{1}.rrd:AMC12curr1V0:AVERAGE".format(filepath,crate),
				 "CDEF:t1cal=t1,1.88,/",
				 "CDEF:t2cal=t2,1.88,/",
				 "CDEF:t3cal=t3,1.88,/",
				 "CDEF:t4cal=t4,1.88,/",
				 "CDEF:t5cal=t5,1.88,/",
				 "CDEF:t6cal=t6,1.88,/",
				 "CDEF:t7cal=t7,1.88,/",
				 "CDEF:t8cal=t8,1.88,/",
				 "CDEF:t9cal=t9,1.88,/",
				 "CDEF:t10cal=t10,1.88,/",
				 "CDEF:t11cal=t11,1.88,/",
				 "CDEF:t12cal=t12,1.88,/",
				 "VDEF:t1avg=t1cal,LAST",
				 "VDEF:t2avg=t2cal,LAST",
				 "VDEF:t3avg=t3cal,LAST",
				 "VDEF:t4avg=t4cal,LAST",
				 "VDEF:t5avg=t5cal,LAST",
				 "VDEF:t6avg=t6cal,LAST",
				 "VDEF:t7avg=t7cal,LAST",
				 "VDEF:t8avg=t8cal,LAST",
				 "VDEF:t9avg=t9cal,LAST",
				 "VDEF:t10avg=t10cal,LAST",
				 "VDEF:t11avg=t11cal,LAST",
				 "VDEF:t12avg=t12cal,LAST",
				 "LINE:t1cal#000000:AMC1",
				 "GPRINT:t1avg:  %4.1lf %SA    ",
				 "LINE:t2cal#FF0000:AMC2",
				 "GPRINT:t2avg:  %4.1lf %SA    ",
				 "LINE:t3cal#FF6600:AMC3",
				 "GPRINT:t3avg:  %4.1lf %SA\l",
				 "LINE:t4cal#FFFF00:AMC4",
				 "GPRINT:t4avg:  %4.1lf %SA    ",
				 "LINE:t5cal#99CC00:AMC5",
				 "GPRINT:t5avg:  %4.1lf %SA    ",
				 "LINE:t6cal#00FF00:AMC6",
				 "GPRINT:t6avg:  %4.1lf %SA\l",
				 "LINE:t7cal#00CC99:AMC7",
				 "GPRINT:t7avg:  %4.1lf %SA    ",
				 "LINE:t8cal#0099CC:AMC8",
				 "GPRINT:t8avg:  %4.1lf %SA    ",
				 "LINE:t9cal#0000FF:AMC9",
				 "GPRINT:t9avg:  %4.1lf %SA\l",
				 "LINE:t10cal#6600FF:AMC10",
				 "GPRINT:t10avg:%2.1lf %SA  ",
				 "LINE:t11cal#FF00FF:AMC11",
				 "GPRINT:t11avg:%2.1lf %SA ",
				 "LINE:t12cal#FF0099:AMC12",
				 "GPRINT:t12avg:%2.1lf %SA")