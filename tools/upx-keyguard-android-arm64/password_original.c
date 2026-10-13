#include <stdio.h>
#include <string.h>
#include <termios.h>
#include <unistd.h>

static int input_password(char *pwd, int max_len) {
    struct termios old, mode;
    int has_tty = tcgetattr(STDIN_FILENO, &old) == 0;
    if (has_tty) {
        mode = old;
        mode.c_lflag &= ~(ICANON | ECHO);
        tcsetattr(STDIN_FILENO, TCSANOW, &mode);
    }
    int idx = 0, ch;
    while ((ch = getchar()) != EOF) {
        if (ch == '\r' || ch == '\n') break;
        if (ch == 127 || ch == '\b') {
            if (idx > 0) {
                --idx;
                fputs("\b \b", stdout);
                fflush(stdout);
            }
            continue;
        }
        if (ch >= 32 && ch < 127 && idx < max_len - 1) {
            pwd[idx++] = (char)ch;
            putchar('*');
            fflush(stdout);
        }
    }
    pwd[idx] = 0;
    if (has_tty) tcsetattr(STDIN_FILENO, TCSANOW, &old);
    putchar('\n');
    return idx > 0 || ch != EOF ? idx : -1;
}

int main(void) {
    char password[32];
    const char right_pwd[] = "123456";
    fputs("请输入密码：", stdout);
    fflush(stdout);
    int rc = input_password(password, (int)sizeof(password));
    if (rc < 0) return 2;
    if (strcmp(password, right_pwd) == 0) {
        puts("✅密码正确，登录成功");
        return 0;
    }
    puts("❌密码错误");
    return 1;
}
