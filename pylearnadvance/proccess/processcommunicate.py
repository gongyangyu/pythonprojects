import multiprocessing

def write_data(q):

    for i in range(12):
        print("writing data %d " % i)
        q.put(i)

def read_data(q):
    while True:
        if not q.empty():
            d=q.get()
            print("reading data %s" % str(d))
            if d>=11:
                break



def main():
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=write_data,args=(q,))
    p2=multiprocessing.Process(target=read_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()