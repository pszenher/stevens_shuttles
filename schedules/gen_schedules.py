import datetime
import json
from itertools import cycle
import os


def main():
    for filename in ['red_weekday.json', 'red_morning.json', 'red_sunday.json', 'red_saturday.json',
                     'green_weekday.json',
                     'gray_weekday.json', 'gray_night.json',
                     'blue_weekday.json']:
        with open(os.path.join(os.getcwd(), filename)) as cfg_file:
            cfg = json.load(cfg_file)
        print('-' * len(filename))
        print(filename)
        print('-' * len(filename))
        generated_filename = os.path.join(os.getcwd(), 'generated', f'{filename.split(".")[0]}.csv')
        with open(generated_filename, 'w') as out_file:
            for cur_cfg in cfg:
                start_time = datetime.datetime.strptime(cur_cfg['start_time'], '%I:%M%p')
                end_time = datetime.datetime.strptime(cur_cfg['end_time'], '%I:%M%p')
                col_count = len(cur_cfg['spacing']) + 1
                column_start_times = [start_time]
                column_start_times.extend([start_time + datetime.timedelta(minutes=s) for s in cur_cfg['spacing']])
                column_patterns = [cycle(cur_cfg['pattern']) for _ in range(col_count)]
                column_firsts = [True for _ in range(col_count)]
                while column_start_times[0].time() != end_time.time():
                    for count in range(col_count):
                        pattern = column_patterns[count]
                        if not column_firsts[count]:
                            column_start_times[count] += datetime.timedelta(minutes=pattern.__next__())
                        column_firsts[count] = False
                        print(column_start_times[count].time().strftime('%I:%M%p'), end=',', file=out_file)
                    print(file=out_file)
                print(file=out_file)


if __name__ == '__main__':
    main()
