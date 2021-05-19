{
    string A;
    int X;
    int Y;
    bool roda;

    A = readln();
    X = 0;
    Y = 3;
    roda = false;

    println("voce: " + A);

    while (!roda && Y>X){
        if (A == "oi" || A=="ola"){
            println ("PC: ola, tudo bem?");
        }
        else{
            println("xau");
        }
        X = X+1;
        println(X);
    }
    if("true"){
        println("TRUEZOU");
    }

    println(Y+X);
    println(A+X);
}