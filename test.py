from operator import itemgetter
import time

my_dict = {'0': 5, '4':6, '3': 2}

start_time = time.time()

sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))
end_time = time.time()

print(sorted_dict)

print(f'elpased Time: {end_time - start_time} seconds')
