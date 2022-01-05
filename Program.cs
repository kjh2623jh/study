namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("GHelllo World");
            string userName;
            Console.WriteLine("What is your name?");
            userName = Console.ReadLine(); // ReadLine 은 항상 string 으로 반환하기때문. 이미 변수의 타입이 string이 아닌 타입으로 지정되어있으면 오류.
            Console.WriteLine($"Hello {userName}.");

            Console.Write("readlinetest : ");
            var readlinetest = Console.ReadLine(); // var 의 경우 노란 줄이 생기지 않음.
            readlinetest = Convert.ToString(readlinetest);  // 형변환.

            // var : 타입을 따로 정해주지않고 맡김. 파이썬처럼.
            var test = 10;
            Console.WriteLine(test);
            // 변수 값을 따로 정해줄 수 없음.
            /*
            var test;
            test = 10;
            */

            //const 값을 변경할 수 없는 값을 지정.
            const double PI = 3.14;
            Console.WriteLine(PI);
            // PI = 3; : error

            // 단순한 식은 파이썬처럼 가능.
            Console.WriteLine($"test : {test}");
            test += 10;
            Console.WriteLine($"test : {test}");
            // C 처럼도 가능.
            test++;
            Console.WriteLine($"test : {test}");

            int test_x;
            int test_y;
            // Prefix
            test_x = 3;
            test_y = ++test_x;
            // x is 4, y is 4

            // Postfix
            test_x = 3;
            test_y = test_x++;
            // x is 4, y is 3

            // if
            if (test < 10)
            {
                Console.WriteLine("test < 10");
            } else if (test < 20)
            {
                Console.WriteLine("test < 20");
            } else
            {
                Console.WriteLine("tes >= 20");
            }

            // switch 
            int test_num = 3;
            switch (test_num)
            {
                case 1:
                    Console.WriteLine("One");
                    break;
                case 2:
                    Console.WriteLine("Two");
                    break;
                case 3:
                case 4:
                    Console.WriteLine("Three or Four");
                    break;
                default:
                    Console.WriteLine("default");
                    break;
            }

            // while 
            test_num = 1;
            while (test_num < 6) // 1 2 3 4 5
            {
                Console.WriteLine(test_num);
                test_num ++;
            }
            Console.WriteLine();
            test_num = 0;
            while (++test_num < 6) // 1 2 3 4 5
            {
                Console.WriteLine(test_num);
            }
            Console.WriteLine();
            test_num = 0;
            while (test_num++ < 6) // 1 2 3 4 5 6
            {
                Console.WriteLine(test_num);
            }
            // while (true){} : infinite loop

            // for
            for (int x = 10; x < 15; x++)
            {
                Console.WriteLine("Value of x: {0}", x);
            }
            for (int x = 0; x < 10; x+=2)
            {
                Console.WriteLine(x);
            }
            int fortest = 10;
            for ( ; fortest > 0; fortest-=3){
                Console.WriteLine(fortest);
            }
            fortest = 10;
            for ( ; fortest > 0 ; ){
                Console.WriteLine(fortest);
                fortest -= 3;
            }
            // for ( ; ;){} : infinite loop

            // do while
            test_num = 0;
            do {
                Console.WriteLine(test_num);
                test_num++;
            } while (test_num < 5); // 0 1 2 3 4
            do {
                Console.WriteLine("test_num: {0}", test_num);
                test_num--;
            } while (test_num > 10);

            // break and continue

            // and: a && b, or: a || b, not: !a

            // 삼항연산자.   value = (a > b) ? A : B;    if (a>b) is true => A , false => B

            // x + y
             do {
                Console.Write("x = ");
                string str = Console.ReadLine();
                if (str == "exit")
                    break;

                int x = Convert.ToInt32(str);

                Console.Write("y = ");
                int y = Convert.ToInt32(Console.ReadLine());

                int sum = x + y;
                Console.WriteLine("Result: {0}", sum);
            } while (true);
        }
    }
}