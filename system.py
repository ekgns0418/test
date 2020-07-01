import os

class bl:

    def add_book(self, bk):
        self.add = str(input("도서추가 [제목 저자 발행년도 출판사 카테고리]순으로 입력하세요."))
        bk.append('\n'+self.add+'\n')
        print("추가되었습니다.")
        return bk
    
    def search_book(self, bk):
        search = str(input("검색어를 입력하세요 :"))
        for i in range(0, len(bk)):
            if search in bk[i]:
                print(bk[i])
    
    def modify_book(self, bk):
        for i in range(len(bk)):
            print(i, ',', bk[i])
        number = int(input("수정할 도서 번호를 입력하세요 : "))
        bk[number] = str(input("수정할 책 정보를 입력하세요. [제목 저자 발행년도 출판사 카테고리] 순서로 입력하세요."))
        print("수정되었습니다.")
        return bk
    
    def delete_book(self, bk):
        for i in range(len(bk)):
            print(i, ",", bk[i])
        number = int(input("삭제할 도서 번호를 입력하세요 :"))
        if number >= i:
            print("다시 입력하세요")
            self.delete_book(bk)
        bk.pop(number)
        print("삭제되었읍니다.")
        return bk
    
    def list_book(self, bk):
        print("현재 책 목록")
        print(bk)

    def save_book(self, bk):
        new_book = ''.join(bk)
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'input.txt')
        f_write = open(my_file, 'w')
        f_write.write(new_book)
        f_write.close
        print("저장되었읍니다.")