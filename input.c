int soma(int x, int y) {
    int a;
    a = x + y;
    println(a);
    return a;
}

int fatorial(int n){
    if(n == 0){
        return 1;
    }

    return n*fatorial(n-1);
}

int main() {
    int a;
    int b;
    int x;
    a = 3;
    x = 4;
    b = soma(a, 4);
    x = fatorial(x);
    println(x);
    println(a);
    println(b);
}
