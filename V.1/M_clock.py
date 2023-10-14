#!/usr/bin/python  
# -*- coding: UTF-8 -*-

import time, os
  
fps_max = -1
t_reel = 0

def frame_clock(while_start, while_finish):

	global t_reel
	t_loop = while_finish - while_start

	if t_loop <= 1 / fps_max:

		t_sleep = (1 / fps_max) - t_loop
		time.sleep(t_sleep)
		fps = 1 / (t_loop + t_sleep)

	else:
		t_sleep = 0
		fps = 1 / t_loop

	return fps