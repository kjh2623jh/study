namespace SoloLearn
{
    //   dotnet run --project ./CsStudy
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


            // properties
            Person3 p3 = new Person3();
            p3.Name = "Bob";
            Console.WriteLine(p3.Name);

            // Auto-Implemented Properties
            Person4 p4 = new Person4();
            p4.Name = "Bob";
            Console.WriteLine(p4.Name);


            // array
            int[] Array1 = new int[10];  // create array
            Array1[0] = 5;

            string[ ] names0 = new string[3] {"John", "Mary", "Jessica"};
            // can omit the size declaration
            string[ ] names1 = new string[ ] {"John", "Mary", "Jessica"};
            // can even omit the new operator.
            string[ ] names2 = {"John", "Mary", "Jessica"};

            Console.WriteLine(names0[2]); // outputs: Jessica

            // 빈 배열 생성
            int[ , ] x0 = new int[3,4];  // two-dimensional
            int[ , , ] x1 = new int[3,4,5];  // three
            // 배열 생성
            int[ , ] someNums = { {2, 3}, {5, 6}, {4, 6} }; 

            for (int k = 0; k < 3; k++) {
                for (int j = 0; j < 2; j++) {
                    Console.Write(someNums[k, j]+" ");
                }
                Console.WriteLine();
            }

            // Jagged Array
            int[ ][ ] jaggedArr = new int[ ][ ] 
            {
                new int[ ] {1,8,2,7,9},
                new int[ ] {2,4,6},
                new int[ ] {33,42}
            };
            int jaggedArrx = jaggedArr[2][1];
            Console.WriteLine(jaggedArrx);

            // Arrays Properties
            int[ ] arr0 = {2, 4, 7};
            Console.WriteLine(arr0.Length);  // 배열 길이
            Console.WriteLine(arr0.Rank);  // 배열 차수
            Console.WriteLine(arr0.Max()); // 배열 최댓값
            Console.WriteLine(arr0.Min()); // 배열 최솟값
            Console.WriteLine(arr0.Sum()); // 배열 전체 합


            // Strings
            string a = "some text";
            Console.WriteLine(a.Length);
            //Outputs 9

            Console.WriteLine(a.IndexOf('t'));
            //Outputs 5

             a = a.Insert(0, "This is ");
            Console.WriteLine(a);
            //Outputs "This is some text"

            a = a.Replace("This is", "I am");
            Console.WriteLine(a);
            //Outputs "I am some text"

            if(a.Contains("some"))
                Console.WriteLine("found");
            //Outputs "found"

            a = a.Remove(4);   // 인덱스 4~ 를 제거
            Console.WriteLine(a);
            //Outputs "I am"

            a = a.Substring(2);  // 인덱스 2~ 이외를 제거
            Console.WriteLine(a);
            //Outputs "am"

            Console.WriteLine(a[1]);
            //Outputs "m"

            string text = "This is some text about a dog. The word dog appears in this text a number of times. This is the end.";
            text = text.Replace("dog", "cat");
            text = text.Substring(0, text.IndexOf(".")+1);  // 인덱스 0 부터 ~dog. 까지 이외를 제거
            
            Console.WriteLine(text);


            // type
            int level = 5;
            float strength = 15.5f;
            string playerName = "홍길동";
            bool isFullLevel = false;
            Console.WriteLine(level);
            Console.WriteLine(strength);
            Console.WriteLine(playerName);
            Console.WriteLine(isFullLevel);

            //list
            List<string> items = new List<string>();
            items.Add("생명물약30");
            items.Add("마나물약30");

            Console.WriteLine(items);

            Console.WriteLine(items[0]);
            Console.WriteLine(items[1]);

            items.RemoveAt(0);

            foreach (string txt in items) {
                Console.WriteLine(txt);
            }
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

        class Person3
        {
            private string name; // field
            private int age = 0;
            public string Name // property
            {
                get { return name; }
                set { name = value; }
            }
            public string getName
            {
                get { return name; }
            }

            public int Age
            {
                get { return age; }
                set {
                    if (value > 0)
                        age = value;
                }
            }
        }
    
        // Auto-Implemented Properties
        class Person4
        {
            public string Name { get; set; }
        }
    }
}