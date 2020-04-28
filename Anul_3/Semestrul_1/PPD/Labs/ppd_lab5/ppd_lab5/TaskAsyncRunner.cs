using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace ppd_lab5
{
    public class TaskAsyncRunner
    {
        public TaskAsyncRunner()
        {
        }

        public void Run() {
            Task<int> t = CreateMultipleTasksAsync();
            Console.WriteLine(string.Format("\r\n\r\nTotal bytes returned:  {0}\r\n", t.Result));
        }

        public async Task<int> CreateMultipleTasksAsync()
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


            // Await each task.  
            int length1 = await download1;
            int length2 = await download2;
            int length3 = await download3;
            int length4 = await download4;
            int length5 = await download5;

            int total = length1 + length2 + length3 + length4 + length5;

            return total;
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
