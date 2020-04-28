using System;
using System.IO;
using System.Net;
using System.Threading.Tasks;

namespace ppd_lab5
{
    class Program
    {
        static void Main(string[] args)
        {
            //RunTaskAsyncRunner();
            RunTaskRunner();
        }

        static void RunTaskRunner() {
            TaskRunner taskRunner = new TaskRunner();
            taskRunner.Run();
        }

        static void RunTaskAsyncRunner() {
            TaskAsyncRunner taskAsyncRunner = new TaskAsyncRunner();
            taskAsyncRunner.Run();
        }
    }
}
