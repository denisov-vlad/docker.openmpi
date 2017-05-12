# -*- coding: utf-8 -*-

from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank == 0:
	time.sleep(2)
	print 'MPI Host'
	for i in range(1, 4):
		elem = comm.recv(source=i, tag=11)
		print 'Received %s from node #%s ' % (elem, i)

else:
	arr = [int(1000*random.random()) for i in xrange(10)]
	print 'MPI Node (%s): %s' % (rank, arr)
	comm.send(arr[0], dest=0, tag=11)
