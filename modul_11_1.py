from multiprocessing import Pool
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()

def linear():
    filenames = [f'file {_}.txt' for _ in range(1, 5)]
    time = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    print('линейный:', datetime.datetime.now() - time)

def multi():
    filenames = [f'file {_}.txt' for _ in range(1, 5)]
    time = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print('многопроцессный:', datetime.datetime.now() - time)

if __name__ == '__main__':
    linear()
    multi()