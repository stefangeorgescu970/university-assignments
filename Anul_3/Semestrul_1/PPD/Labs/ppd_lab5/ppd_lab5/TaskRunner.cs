using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

namespace ppd_lab5
{
    public class TaskRunner
    {
        public TaskRunner()
        {
        }

        public void Run() {
            var tasks = CreateMultipleTasksAsync();
            var totalLength = 0;

            foreach (Task<int> task in tasks) {
                totalLength += task.Result;
            }

            Console.WriteLine("Total length {0}", totalLength);
        }


        public Task[] CreateMultipleTasksAsync()
        {

            HttpClient client =
                new HttpClient() { MaxResponseContentBufferSize = 1000000 };


            Task<int> download1 =
                ProcessURLAsync("https://msdn.microsoft.com", client);
            Task<int> download2 =
                ProcessURLAsync("https://msdn.microsoft.com/library/hh156528(VS.110).aspx", client);
            Task<int> download3 =
                ProcessURLAsync("https://msdn.microsoft.com/library/67w7t67f.aspx", client);
            Task<int> download4 =
                ProcessURLAsync("https://www.google.com", client);
            Task<int> download5 =
                ProcessURLAsync("https://www.apple.com", client);

            Task[] tasks = new Task[5];
            tasks[0] = download1;
            tasks[1] = download2;
            tasks[2] = download3;
            tasks[3] = download4;
            tasks[4] = download5;

            return tasks;
        }

        async Task<int> ProcessURLAsync(string url, HttpClient client)
        {
            var byteArray = await client.GetByteArrayAsync(url);
            DisplayResults(url, byteArray);
            return byteArray.Length;
        }

        private void DisplayResults(string url, byte[] content)
        {
            var bytes = content.Length;
            var displayURL = url.Replace("https://", "");

            Console.WriteLine(string.Format("\n{0,-58} {1,8}", displayURL, bytes));
        }
    }
}
