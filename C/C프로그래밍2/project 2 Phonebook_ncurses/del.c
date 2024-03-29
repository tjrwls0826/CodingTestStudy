// Ncurses를 이용한 구현

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ncurses.h>

#define MAX_Contacts 100

struct Contact {
    char name[30];
    char phone[20];
    char memo[40];
};


int compare(const void *a, const void *b) { // qsort에 사용될 비교 함수
    struct Contact *contactA = (struct Contact *)a;
    struct Contact *contactB = (struct Contact *)b;
    return strcmp(contactA->name, contactB->name); // 반환값에 따라 요소 순서 결정 (name)을 기준으로 정렬
}

int main() {
    initscr();
    cbreak();
    noecho();


    char message[]="Phonebook management Program";
    int ymax,xmax;
    int cury,curx;
    getmaxyx(stdscr,ymax,xmax);


    start_color();
    init_pair(1,COLOR_GREEN,COLOR_WHITE);

    attron(COLOR_PAIR(1));
    attron(A_BOLD);
    mvprintw(ymax/2,(xmax-strlen(message))/2,"%s",message);
    attroff(COLOR_PAIR(1));
    attroff(A_BOLD);

    mvprintw(ymax-1,0,"Press any key to continue.\n",ymax,xmax);
    refresh();
    getch();
    mvprintw(ymax-12,5,"Select what you want.(Press Enter)\n");
    refresh();
    WINDOW *menuwin = newwin(7,xmax-12,ymax-7,0);
    box(menuwin,0,0);
    refresh();
    wrefresh(menuwin);

    keypad(menuwin,TRUE);

    char *choices[5] = {"Search : by Name or Number or Memo","Add : new contact form is name number memo(optional)","Delete: Find it by Name or Number or Memo.","List : Alphabet order","Exit"};
    int choice;
    int highlight = 0;
    char name[30];
    char number[20];
    char memo[40];
    char keyword[40];


    while (1) {
        for (int i = 0; i < 5; i++) {
                if (i == highlight) {
                    wattron(menuwin,A_REVERSE); // 선택된 항목을 강조
                }
                mvwprintw(menuwin, i+1, 1, choices[i]);
                wattroff(menuwin,A_REVERSE);
            }
            choice = wgetch(menuwin);

            switch (choice) {
                case KEY_UP:
                    highlight--;
                    if (highlight <= -1)
                        highlight = 0;
                    break;
                case KEY_DOWN:
                    highlight++;
                    if (highlight >= 5)
                        highlight = 4;
                    break;
                default:
                    break;
                }
            if (choice == 10)
                break;
    }
    //printw("Your choice is %s",choices[highlight]);
//    wclear(menuwin);




    if (highlight == 1) { //        add 기능 구현
        WINDOW *addwin = newwin(10, 50, 2, 2);
        box(addwin, 0, 0);
        refresh();

        // 입력 필드 생성
        echo();
        mvwprintw(addwin, 1, 2, "name: ");
        mvwprintw(addwin, 2, 2, "number: ");
        mvwprintw(addwin, 3, 2, "memo (You can leave empty if you want.):");
        mvwprintw(addwin, 7, 2, "Enter to save and exit.");



        mvwgetnstr(addwin, 1, 8, name, 30);
        mvwgetnstr(addwin, 2, 10, number, 20);
        mvwgetnstr(addwin, 4, 2, memo, 40);

        char filename[] = "data.txt";
        FILE *file = fopen(filename, "a");

        // 입력 받은 정보 파일에 저장
        fprintf(file, "%s:%s:%s\n", name, number, memo);


        fclose(file);

        // 종료
        noecho();
        delwin(addwin);
        endwin();
        refresh();
        }

    else if (highlight == 2) { // Delete 기능 구현
        WINDOW *delewin = newwin(ymax-2, xmax, 2, 0);
        box(delewin, 0, 0);
        mvwprintw(delewin, 2, 2, "Input keyword you want to find to Delete:");
        wrefresh(delewin);
        echo();
        mvwgetnstr(delewin, 3, 2, keyword, 40);
        noecho();

        char filename[] = "data.txt";
        int found = 0;
        int order = 1;
        FILE *file = fopen(filename, "r");
        char line[93];
        struct Contact contacts[MAX_Contacts];
        int numContacts = 0;

        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            if (strstr(name, keyword) != NULL || strstr(phone, keyword) != NULL || strstr(memo, keyword) != NULL) {
                strcpy(contacts[numContacts].name, name);
                strcpy(contacts[numContacts].phone, phone);
                strcpy(contacts[numContacts].memo, memo);
                numContacts++;
                found = 1;
            }
        }

        fclose(file);

        if (found) {
            mvwprintw(delewin, 5, 2, "Matching contacts found. Select a contact to delete:");
            int highlight = 0;
            int choice;
            keypad(delewin, TRUE);

            while (1) {
                for (int i = 0; i < numContacts; i++) {
                    if (i == highlight) {
                        wattron(delewin, A_REVERSE); // 선택된 항목을 강조
                    }
                    mvwprintw(delewin, i + 6, 2, "%d %s %s %s", i + 1, contacts[i].name, contacts[i].phone, contacts[i].memo);
                    wattroff(delewin, A_REVERSE);
                }
                choice = wgetch(delewin);

                switch (choice) {
                    case KEY_UP:
                        highlight--;
                        if (highlight < 0)
                            highlight = 0;
                        break;
                    case KEY_DOWN:
                        highlight++;
                        if (highlight >= numContacts)
                            highlight = numContacts - 1;
                        break;
                    default:
                        break;
                }
                if (choice == 10)
                    break;
            }
            mvwprintw(delewin, ymax - 4, 2, "Contact deleted: %s %s %s", contacts[highlight].name, contacts[highlight].phone, contacts[highlight].memo);
            wrefresh(delewin);

            if (highlight >= 0 && highlight < numContacts) {

                // 삭제 작업 수행
                FILE *tempFile = fopen("temp.txt", "w");
                if (tempFile == NULL) {
                    mvwprintw(delewin, ymax - 4, 2, "Error deleting contact.");
                    wrefresh(delewin);
                    getch();
                    delwin(delewin);
                    endwin();
                    return 1;
                }

                file = fopen(filename, "r");
                order = 0;
                while (fgets(line, sizeof(line), file) != NULL) {
                    char *name = strtok(line, ":");
                    char *phone = strtok(NULL, ":");
                    char *memo = strtok(NULL, ":");

                    if (strcmp(name, contacts[highlight].name) != 0 || strcmp(phone, contacts[highlight].phone) != 0 || strcmp(memo, contacts[highlight].memo) != 0) {
                        fprintf(tempFile, "%s:%s:%s", name, phone, memo);
                        order++;
                    }
                }

                fclose(file);
                fclose(tempFile);
                remove(filename);
                rename("temp.txt", filename);
            }
            else {
                mvwprintw(delewin, ymax - 4, 2, "Invalid selection. Contact not deleted.");
            }
        }
        else {
            mvwprintw(delewin, 5, 2, "No matching contacts found.");
        }

        wrefresh(delewin);
        delwin(delewin);
        noecho();

    }




        //                          검색기능
    else if (highlight == 0){
        WINDOW *searchwin = newwin(ymax-2, xmax, 2, 0);
        box(searchwin, 0, 0);
        mvwprintw(searchwin,2,2,"Input keyword you want to find:");
        wrefresh(searchwin);
        echo();
        mvwgetnstr(searchwin, 3, 2, keyword, 40);



        char filename[] = "data.txt";
        int found = 0;
        int order = 1;
        FILE *file = fopen(filename, "r");
        char line[93];
        while (fgets(line, sizeof(line), file) != NULL) {
        // 파일에서 데이터를 읽어와서 검색어와 일치하는지 확인
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");
            if (strstr(name, keyword) != NULL || strstr(phone, keyword) != NULL || strstr(memo, keyword) != NULL) {
                getyx(searchwin,cury,curx);
                cury = cury + 1;
                found = 1;
                mvwprintw(searchwin,cury,2, "%d %s %s %s",order,name,phone,memo);
                wrefresh(searchwin);
                order = order + 1;

            }


        }
        if (found != 1) {
            mvwprintw(searchwin,9,2, "There is none of that");
            wrefresh(searchwin);
        }
        getyx(searchwin,cury,curx);
        mvwprintw(searchwin,cury+1,2, "Press any key to Exit");
        wrefresh(searchwin);


    fclose(file);
    }



    getch();
    delwin(menuwin);
    endwin();
    return 0;
}