{
    /*RECEBE A B E maior, se maior = 0 ele retorna o menor entre a e b, caso contrário, o menor. Faz isso 2 vezes*/
    {
        C = 0;
        while(C<2){
            A = readln();
            B = readln();
            maior = readln();
            if(!(maior == 0)){
                if((A>B)){
                    println(A);
                }
                else{
                    println(B);
                }
            }else{
                if((A<B)){
                    println(A);
                }
                else{
                    println(B);
                }
            }
            C = C + 1;
        }
    }

    println(100000000);

    /*RECEBE X e Y, se um dos dois for maior que 10, e o outro menor que 5, printa 1000. Caso contrario printa 0*/
    {
        X = readln();
        Y = readln();
        if (((X>10)||(Y>10)) && ((X<5)||(Y<5))){
            println(1000);
        } else {
            println(0);
        }
    }

    println(100000000);

    /*Recebe Z e W enquanto Z for maior que W, e os dois forem maior que 10, e printa Z*/
    {
        Z = readln();
        W = readln();
        while(Z>W && !(Z<10 || W<10)){
            println(Z);
            W = readln();
            Z = readln();
        }
    }
}