import time, os
from datetime import datetime, date


def determine(list_file):
    delete = []
    for file in list_file:
        fmt = '%Y-%m-%d %H:%M:%S'
        file_t = time.ctime(os.path.getctime(file))
        t1 = time.mktime(time.strptime(file_t))
        t2 = time.mktime(time.strptime(datetime.now().strftime('%a %b %d %H:%M:%S %Y')))
        total = (t2 - t1) / 60
        if total > 10:
            delete.append(file)
    return delete


def delete_file(list_files):
    for file in list_files:
        os.remove(file)
    return True

def main():
    while True:
        time.sleep(1)
        files = (os.listdir('600'))
        d_files = determine(files)
        delete_file(d_files)


if __name__ == '__main__':
    print("Junk files being removed!")
    main()
