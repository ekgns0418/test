import os
import system

this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, 'input.txt')
f = open(my_file,'r')
bk = f.readlines()



class book:

    def __init__(self):
        self.bl_class = system.bl()

    def menu_list(self):
        print("1. 도서 추가")
        print("2. 도서 검색")
        print("3. 도서 정보 수정")
        print("4. 도서 삭제")
        print("5. 현재 총 도서 목록 출력")
        print("6. 저장")
        print("7. 프로그램 나가기")

    
    def menu(self, bk):
        self.menu_list()
        menu_number = int(input("메뉴를 선택하세요 :"))

        if menu_number == 1:
            self.bl_class.add_book(bk)
            self.menu(bk)
        elif menu_number == 2:
            self.bl_class.search_book(bk)
            self.menu(bk)
        elif menu_number == 3:
            self.bl_class.modify_book(bk)
            self.menu(bk)
        elif menu_number == 4:
            self.bl_class.delete_book(bk)
            self.menu(bk)
        elif menu_number == 5:
            self.bl_class.list_book(bk)
            self.menu(bk)
        elif menu_number == 6:
            self.bl_class.save_book(bk)
            self.menu(bk)
        elif menu_number == 7:
            self.bl_class.save_book(bk)
        else:
            print("다시 입력하세요.")
            self.menu(bk)

a = book()
a.menu(bk)