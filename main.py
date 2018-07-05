
import core.orderbook as ob
import core.executed as ex


if __name__ == '__main__':

    int_sec = 1 # 몇 초 간격으로 data를 따올 것인지
    orderbook_path_src = 'D:\\Dropbox\\2018-05-10_KOSDAQ_104480_orderbook.csv' # source path

    ### 호가창정보 Preprocess 및 Scailing ###
    machine = ob.OB_Preprocess() # orderbook preprocess 및 scailing 해주는 object
    df = machine.preprocess(orderbook_path_src,int_sec) # preprocess
    df = machine.scail(df) #scailing
    df.to_csv("D:\\test.csv") #save


    ### 체결정보 Preprocess 및 Scailing ###
    executed_path_src = 'D:\\Dropbox\\2018-05-10_KOSDAQ_104480_executed.csv' #source path
    machine = ex.EX_Preprocess()
    df = machine.preprocess(executed_path_src,int_sec) #preprocess
    df = machine.scail(df) # saciling
    df.to_csv("D:\\test_executed.csv") # save