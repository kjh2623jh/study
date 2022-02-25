namespace SoloLearn
{
    class Program
    {
        // static: not public
        // The static keyword will be discussed later; it is used to make methods accessible in Main.
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

            // foreach   like for in Python
            foreach (char txt in "test")
            {
                Console.WriteLine($"foreach_test.txt: {txt}");
            }

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
            Console.WriteLine();
            Console.WriteLine("X + Y Program.");
            Console.WriteLine("input 'exit' for exit Program.");
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

            Console.WriteLine(Sqr(5));
            SayHi();
            Console.WriteLine(Sum(4, 5));
            int sumFuncTest = Sum(5, 6);
            Console.WriteLine(sumFuncTest);

            Console.WriteLine(Pow(6)); // result: 36
            Console.WriteLine(Pow(2, 4)); // result: 16

            Console.WriteLine(namedArguments(3, 4)); // a: 3, b: 4
            Console.WriteLine(namedArguments(b: 6, a: 2)); // a: 2, b: 6

            int reftest = 3;
            refFunc(ref reftest);  // The ref keyword is used both when defining the method and when calling it.
            Console.WriteLine(reftest); // outputs 9

            int outtestA, outtestB;
            outfunc(out outtestA, out outtestB);
            // outtestA: 5, outtestB: 13

            Print(5);
            Print(5.12);
            Print("double a: ", 3.14);

            Console.WriteLine(Fact(4)); // outputs 24

            DrawPyramid(5);


            //class
            Person p1 = new Person();
            p1.sayHi();

            Dog bob = new Dog();
            bob.name = "Bobby";
            bob.age = 3;

            Console.WriteLine(bob.age);


            // Encapsulation ( information hiding )

            // In summary, the benefits of encapsulation are:
            // - Control the way data is accessed or modified.
            // - Code is more flexible and easy to change with new requirements.
            // - Change one part of code without affecting other parts of code.
            BankAccount b = new BankAccount();
            b.Deposit(199);
            b.Withdraw(42);
            Console.WriteLine(b.GetBalance());


            // Constructors
            // i think it is like __init__ in python
            ConstructorsClass constructorsValue = new ConstructorsClass();

            Person2 p2 = new Person2("David");
            Console.WriteLine(p2.getName());
        }

        static int Sqr(int x)  // void is a basic data type that defines a valueless state.
        {
            int result = x*x;
            return result;
        }

        static void SayHi()
        {
            Console.WriteLine("Hello");
        }

        static int Sum(int x, int y)
        {
            return x+y;
        }

        static int Pow(int x, int y=2) // default value
        {
        int result = 1;
        for (int i = 0; i < y; i++)
        {
            result *= x;
        }
        
        return result;
        }

        static int namedArguments(int a, int b)
        {
            return a * b;
        }

        static void refFunc(ref int x) // return 을 사용하지 않아도 값을 변경 python 의 global 같은??
        {
            x = x*x;
        }

        static void outfunc(out int x, out int y)
        {
            x = 5;
            y = 13;
        }

        static void Print(int a)
        {
            Console.WriteLine("Value: "+a);
        }
        static void Print(double a)
        {
            Console.WriteLine("Value: "+a);
        }
        // Now, the same Print method name will work for both integers and doubles.
        static void Print(string label, double a)
        {
            Console.WriteLine(label + a);
        }

        static int Fact(int num) {
            if (num == 1) {
                return 1;
            }
            return num * Fact(num - 1);
        }

        static void DrawPyramid(int n)
        {
            for (int i = 1; i <= n; i++){
                for (int j = i; j <= n; j++){
                    Console.Write("  ");
                }
                for (int k = 1; k <= 2*i-1; k++){
                    Console.Write("*" + " ");
                }
                Console.WriteLine();
            }
        }

        class Person
        {
            int age;
            string name;
            public void sayHi()  // the member is private by default.
                                 // private (static?) 함수는 해당 클래스에서만 사용됨. 타 클래스에서 접근 불가능.
            {
                Console.WriteLine("Hi");
            }
        }
    
        class Dog
        {
            public string name;
            public int age;
        }
    
        class BankAccount
        {
            private double balance = 0;
            public void Deposit(double n)
            {
                balance += n;
            }
            public void Withdraw(double n)
            {
                balance -= n;
            }
            public double GetBalance()
            {
                return balance;
            }
        }
    
        class ConstructorsClass
        {
            public ConstructorsClass()
            {
                Console.WriteLine("Hello");
            }
        }

        class Person2
        {
            private int age;
            private string name;
            public Person2(string nm)
            {
                name = nm;
            }
            public string getName()
            {
                return name;
            }
        }
    }
}