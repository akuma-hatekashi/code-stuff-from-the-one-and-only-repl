using System;
using System.Threading;

class ThreadExample 
{
	public void MyThread()
	{
        for (int x = 0; x < 1000; x++) 
        {
            Console.WriteLine(x);
        }
	}
}

class MainClass 
{
	public static void Main()
    {
		var obj = new ThreadExample();
		Thread thr = new Thread(new ThreadStart(obj.MyThread));

        Console.WriteLine("Start the thread");
		thr.Start();

        Console.WriteLine("Abort the thread");
        thr.Abort();

        Console.WriteLine("Finished!");
	}
}
