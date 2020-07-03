import sys
import copy
import os

this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, 'TrainList.txt')
f = open(my_file, 'r')
trainlist = []
indlist = []
while True:
    tl = f.readline().split()
    trainlist.append(tl)
    if not tl:
        break
f.close()
trainlist.pop(0)
trainlist.pop(-1)

modylist = copy.deepcopy(trainlist)
reserve_list = []
ind = None

for i in range(len(modylist)):
     modylist[i].pop(2)
     modylist[i][0] = modylist[i][0].replace(":", "")
     modylist[i][0] = int(modylist[i][0])

class train:

    def menu(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매하기")
            print("2. 전체 기차 편성 보기")
            print("3. 예매 현황 보기, 에매 취소하기")
            print("4. 프로그램 종료")
            try:
                number = int(input("메뉴를 선택하세요 : "))
            except ValueError:
                print("다시 고르세요.")
                self.menu()
            if number == 1:  
                self.select_train() #빠른 시간 기차 검색 및 예매로
            elif number == 2:
                self.all_train() #전체 기차 편성 보기
            elif number == 3:
                self.reserve_train() #예매 현황, 취소
            elif number == 4:
                self.off_train() #프로그램 종료
                break
            else:
                print("다시 입력하세요.")
                self.menu() #다시 메뉴 보기

    def select_train(self): #1번메뉴
        print("가까운 시간대의 기차 조회는 1번")
        print("뒤로가기 2번")
        select_train_number = int(input("숫자를 입력하세요 : "))
        
        if select_train_number == 1: #가까운 시간대 기차 조회
            want_train = list(input("시간, 출발역, 도착역, 열차종류 입력 ex) 07:20 서울 부산 KTX").split())
            delete_seat = copy.deepcopy(modylist)
            
            tmp_mytime = want_train[0].replace(":", "")
            mytime = int(tmp_mytime[:2]) * 60 + int(tmp_mytime[2:4])
            want_train[0] = close_time(mytime)

            for i in range(len(modylist)):
                delete_seat[i].pop()
            
            final_list = []
            for j in range(len(delete_seat)):
                if delete_seat[j] == want_train:
                    final_list = delete_seat[j].copy()
                    final_list.append(trainlist[j][5])
                    ind = j
            
            a, b = divmod(final_list[0], 100)
            a = str(a)
            b = str(b)
            final_list[0] = ''.join(['0', a, ':', b])
            print("가장 가까운 기차입니다.")
            print(final_list)

            reservation = input("\n 해당 기차표를 예매하시겠습니까? [Y/N]")
            if reservation == 'Y':
                if trainlist[ind][5] != 0:
                    reserve_list.append(trainlist[ind])
                    trainlist[ind][5] = int(trainlist[ind][5]) - 1
                    print("\n 예매가 완료됐습니다.")
                else:
                    print("\n매진입니다.")
                    self.menu()
            
            elif reservation == 'N':
                self.menu()

            else:
                print("다시 입력하세요.")
                self.menu()
            
        

        elif select_train_number == 2: #뒤로가기
            self.menu()
        
        else:
            print("다시 입력하세요.")
            self.select_train()
        return ind, reserve_list
        
    def all_train(self):
        print("1. 전체 편성 보기")
        print("2. 뒤로 가기")
        all_train_number = int(input("입력 : "))
        copyTrainlist = copy.deepcopy(trainlist)
        if all_train_number == 1:
            p = 0
            while p < len(trainlist):
                if copyTrainlist[p][5] == 0:
                    copyTrainlist[p][5] = '매진'
                a, b, c, d, e, f = copyTrainlist[p]
                print(a, b, c, d, e, f)
                p += 1

        elif all_train_number == 2:
            self.menu()
        
        else:
            print("다시 입력하세요.")
            self.all_train()

    def reserve_train(self): 
        print("1. 예매내역 출력")
        print("2. 예매내역 취소")
        print("3. 뒤로가기")
        reserve_train_number = int(input("입력 : "))
        if reserve_train_number == 1:
            print("예매 내역")
            print(reserve_list)
            if not reserve_list:
                print("예매한 기록이 없습니다.")
                self.menu()
             
        elif reserve_train_number == 2:
            cancel = input("예매를 취소하시겠습니까? [Y/N]")
            if cancel == 'Y':
                print("예매 번호는 0번 부터입니다.")
                print(reserve_list)
                cancel_number = int(input("몇 번을 취소하시겠습니까?"))
                for p in range(len(trainlist)):
                    if not reserve_list:
                        print("예매한 기록이 없습니다.")
                        self.menu()
                    else:
                        if reserve_list[cancel_number] == trainlist[p]:
                            trainlist[p][5] = trainlist[p][5] + 1
                            reserve_list.pop(cancel_number)
                            print("예매가 취소 되었습니다.")
                            break
            elif cancel == 'N':
                print("취소되었습니다.")
                self.menu()    
                
            else:
                print("다시 입력하세요")
                self.reserve_train()

        elif reserve_train_number == 3:
            self.menu()
        else:
            print("다시 입력하세요.")
            self.reserve_train()

    def off_train(self):
        sys.exit()

def close_time(mytime):
    onlylist = [3+6, 395, 435, 522]
    real_time = [605, 635, 715, 842]
    abs_list = []
    for i in range(len(onlylist)):
        abs_list.append(abs(mytime - onlylist[i]))
    ind = abs_list.index(min(abs_list))
    return real_time[ind]


if __name__ == "__main__":
    mytrain = train()
    print(mytrain.menu())
