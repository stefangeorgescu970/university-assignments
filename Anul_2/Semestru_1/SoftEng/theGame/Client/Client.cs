﻿using System;
using System.IO;
using System.Net.Sockets;
using System.Net;
using System.Text;
using Newtonsoft.Json;
using Server;
using System.Runtime.CompilerServices;
using System.Threading;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using Board;

namespace Client
{
    // State object for receiving data from remote device.
    public class StateObject
    {
        // Client socket.
        public Socket WorkSocket = null;
        // Size of receive buffer.
        public const int BufferSize = ServerConstants.ClientBufferSize;
        // Receive buffer.
        public byte[] Buffer = new byte[BufferSize];
        // Received data string.
        public StringBuilder Sb = new StringBuilder();
    }

    public abstract class Client
    {
        // ManualResetEvent instances signal completion.
        private static ManualResetEvent _connectDone = new ManualResetEvent(false);
        private static ManualResetEvent _sendDone = new ManualResetEvent(false);
        private static ManualResetEvent _receiveDone = new ManualResetEvent(false);

        public int Id = -1;
        private bool _isConnected = false;

        /// <summary>
        /// Baord of each individual client
        /// </summary>

        public GameBoard Board = new GameBoard();

        private Socket _mySocket;
        
        protected Client()
        {
            TryConnect(ServerConstants.MaximumNumberOfAttemtps);
            if (!_isConnected)
            {
                //TODO handle case when the client does not manage to esablish connection to server
                _isConnected = false;
            }
        }

        protected void SetId(int id)
        {
            Id = id;
        }
        protected int GetId()
        {
            return Id;
        }
        public void TryConnect(int maximumAttempts)
        {
            int attempts = 0;
            while (!_isConnected && attempts < maximumAttempts)
            {
                try
                {
                    IPEndPoint remoteEp = new IPEndPoint(IPAddress.Loopback, ServerConstants.UsedPort);
                    
                    // Create a TCP/IP socket.
                    Socket client = new Socket(AddressFamily.InterNetwork,
                        SocketType.Stream, ProtocolType.Tcp);
                    
                    // Connect to the remote endpoint.
                    client.BeginConnect(remoteEp,
                        new AsyncCallback(ConnectCallback), client);
                    _connectDone.WaitOne();

                    System.Threading.Thread.Sleep(2000); // fix for mac which sent requests really quickly
                    attempts++;

                    _isConnected = true;
                    _mySocket = client;

                    // Create the state object.
                    StateObject state = new StateObject {WorkSocket = client};

                    // Begin receiving the data from the remote device.
                    client.BeginReceive(state.Buffer, 0, StateObject.BufferSize, 0,
                                        new AsyncCallback(ReceiveMessage), state);
                }
                catch (SocketException)
                {
                    //Console.Clear();
                    Console.WriteLine("Connection Attempts: " + attempts);
                }
            }
         //   Console.Clear();
            if (_isConnected)
                Console.WriteLine("Connected");
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.
                Socket client = (Socket)ar.AsyncState;
                
                // Complete the connection.
                client.EndConnect(ar);
                
                Console.WriteLine("Socket connected to {0}",
                    client.RemoteEndPoint.ToString());
                
                // Signal that the connection has been made.
                _connectDone.Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
        
        private void ReceiveMessage(IAsyncResult asyncResult)
        {
            try
            {
                // Retrieve the state object and the client socket 
                // from the asynchronous state object.
                
                String content = String.Empty;

                // Retrieve the state object and the handler socket
                // from the asynchronous state object.
                StateObject state = (StateObject)asyncResult.AsyncState;
                
                Socket handler = state.WorkSocket;
                Console.WriteLine("packet received step 1111111");
                // Read data from the client socket. 
                int bytesRead = handler.EndReceive(asyncResult);

                if (bytesRead > 0)
                {
                    // There  might be more data, so store the data received so far.
                    state.Sb.Append(Encoding.ASCII.GetString(state.Buffer, 0, bytesRead));
                    
                    // Check for end-of-file tag. If it is not there, read 
                    // more data.
                    content = state.Sb.ToString();
                    int eofIndex = content.IndexOf(ServerConstants.endOfPacket, StringComparison.Ordinal);
                    Console.WriteLine("packet received step 222222");
                    if (eofIndex > -1)
                    {
                        // All the data has been read from the 
                        // client. Display it on the console.
                        Console.WriteLine("Read {0} bytes from socket. \n Data : {1}",
                            content.Length, content);
                        
                        Packet receivedPacket = JsonConvert.DeserializeObject<Packet>(content.Remove(eofIndex));
                        HandleReceivePacket(receivedPacket);
                        Console.WriteLine("packet received step 3333333");
                        state.Sb.Clear();
                        handler.BeginReceive(state.Buffer, ServerConstants.BufferOffset, StateObject.BufferSize,
                            SocketFlags.None,
                            new AsyncCallback(ReceiveMessage), state);
                    }
                    else
                    {
                        // Not all data received. Get more.
                        handler.BeginReceive(state.Buffer, ServerConstants.BufferOffset, StateObject.BufferSize,
                            SocketFlags.None,
                            new AsyncCallback(ReceiveMessage), state);
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void Send(Socket client, String data)
        {
            // Convert the string data to byte data using ASCII encoding.
            byte[] byteData = Encoding.ASCII.GetBytes(data);
            
            // Begin sending the data to the remote device.
            client.BeginSend(byteData, ServerConstants.BufferOffset, byteData.Length, SocketFlags.None,
                new AsyncCallback(SendCallback), client);
        }

        private static void SendCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.
                Socket client = (Socket)ar.AsyncState;
                
                // Complete sending the data to the remote device.
                int bytesSent = client.EndSend(ar);
                
                Console.WriteLine("Sent {0} bytes to server.", bytesSent);
                
                // Signal that all bytes have been sent.
                _sendDone.Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        public void SendPacket(Packet myPacket)
        {
            if (_isConnected)
            {
                String jsonString = JsonConvert.SerializeObject(myPacket);

                jsonString += ServerConstants.endOfPacket;

                Send(_mySocket, jsonString);
            }
            else
            {
                Console.WriteLine("Client with id " + Id + " is not connected to server");
                // TODO maybe create an internal id, since here all ids will be -1 if initial connection fails
            }
        }

        public void RegisterToServerAndGetId(ClientType whoAmI, int numberOfSeats = 0)
        {
            Packet toSend = new Packet(Id, -1, RequestType.Register);
            
            toSend.AddArgument(ServerConstants.ArgumentNames.SenderType, whoAmI);

            if(ClientType.GameMaster == whoAmI) {
                toSend.AddArgument("NumberOfPlayersForGame", numberOfSeats);
            }
            
            SendPacket(toSend);
        }
        public abstract void HandleReceivePacket(Packet receivedPacket);
    }
}
