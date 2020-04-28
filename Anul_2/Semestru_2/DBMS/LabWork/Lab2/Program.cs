using System.Data.OleDb;
using System;
using System.Data;
using System.Data.SqlClient;


namespace Lab2



{
    internal class Program
    {
        public static void Main(string[] args)
        {
            System.Console.Out.WriteLine("Hello world");
            
            
            SqlConnection sqlConn = new SqlConnection(Program.GetConnectionString());
            DataSet ds;
            SqlDataAdapter agents;
            SqlDataAdapter players;
            SqlCommandBuilder cb;
            

            
            
            
            
            sqlConn.Open();
            
            System.Console.Out.WriteLine("Did work");
           
        }
        
        static string GetConnectionString()
        {
            return             "server=localhost;" +
                               "Initial Catalog=myDatabase;" +
                               "User id=sa;" +
                               "Password=P@55w0rd;" +
                               "Trusted_Connection=yes;" + 
                                "Integrated Security = false";
           
        }
    }
}