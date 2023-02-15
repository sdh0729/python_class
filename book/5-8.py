int map[9][9] = {{2, 2, 2, 2, 2, 2, 2, 2, 2},
             {2, 0, 0, 0, 0, 0, 0, 0, 2},
             {2, 0, 1, 1, 1, 0, 0, 0, 2},
             {2, 0, 1, 0, 1, 0, 0, 0, 2},
             {2, 0, 1, 0, 1, 0, 0, 0, 2},
             {2, 0, 1, 1, 1, 0, 0, 0, 2},
             {2, 0, 0, 0, 0, 0, 0, 0, 2},
             {2, 0, 0, 0, 0, 0, 0, 0, 2},
             {2, 2, 2, 2, 2, 2, 2, 2, 2}};

int visit(int x, int
y);
void
print();

int
success;
int
start_x, start_y;
int
end_x, end_y;
int
sp, ri[100], rj[100];

void
main()
{
    sp = 0;
start_x = 1;
start_y = 1; // 시작지점 \
                // end_x = 7;
// end_y = 7; // 최종도착지점

success = 0;

// printf("미로 찾기\n");

visit(1, 1);

print();
}

int
visit(int
x, int
y)
{
    map[x][y] = 1; // 지나간
위치를
표시

if (map[x][y + 1] == 0)
visit(x, y + 1);
if (map[x + 1][y] == 0)
visit(x + 1, y);
if (map[x][y - 1] == 0)
visit(x, y - 1);
if (map[x - 1][y] == 0)
visit(x - 1, y);

return success;
}

void
print()
{
int
i, j;

for (i=0; i < 9; i++)
    {
    for (j=0; j < 9; j++)
    printf("%d ", map[i][j]);
    printf("\n");
    }
}