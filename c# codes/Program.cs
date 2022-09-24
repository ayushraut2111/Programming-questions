class A{
    public void eat()
    {
        Console.Write("dog");
    }
}
class B:A{
     public void eat1()
    {
        Console.Write("cat");
    }
    public static void Main(){
        B b1=new B();
        b1.eat();
    }
}