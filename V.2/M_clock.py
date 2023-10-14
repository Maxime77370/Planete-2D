#!/usr/bin/python  
# -*- coding: UTF-8 -*-

import time, os

def frame_clock(while_start, while_finish, fps_max):

	t_loop = while_finish - while_start

	if t_loop <= 1 / fps_max:

		t_sleep = (1 / fps_max) - t_loop
		fps = 1 / (t_loop + t_sleep)

	else:
		t_sleep = 0
		fps = 1 / t_loop

	return t_sleep, fps