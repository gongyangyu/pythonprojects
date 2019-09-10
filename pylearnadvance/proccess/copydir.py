import multiprocessing
import os


def copy_files(q,file_name,file_path,new_path):
    f=open(file_path+"/"+file_name,"rb")
    content=f.read()
    cf=open(new_path+"/"+file_name,"wb")
    cf.write(content)
    q.put(file_name)

def main():
    file_path="C:/git_code/myApp/node_modules/babel-runtime/helpers"
    file_list=os.listdir(file_path)
    try:
        new_path=file_path+'bak'
        os.mkdir(new_path)
    except:
        pass
    po=multiprocessing.Pool(5)
    q=multiprocessing.Manager().Queue()
    for file_name in file_list:
        po.apply_async(copy_files,args=(q,file_name,file_path,new_path))
    po.close()
    po.join()
    while True:
        print("copying %s" % q.get())




if __name__ == "__main__":
    main()