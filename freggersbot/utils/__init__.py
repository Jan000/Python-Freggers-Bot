import time

def time_ms():
	return int(round(time.time() * 1000))

def format_time(time):
	seconds = int(time)
	if seconds > 0:
		s = str(seconds % 60) + 'sec'
		minutes = seconds // 60
		if minutes > 0:
			s = str(minutes % 60) + 'min ' + s
			hours = minutes // 60
			if hours > 0:
				s = str(hours % 24) + 'h ' + s
				days = hours // 24
				if days > 0:
					s = str(days) + 'd ' + s
		return s
	else:
		return '0sec'