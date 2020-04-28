using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace lab2
{

    public partial class newWebForm : System.Web.UI.Page
    {

        public string rememberedByRequest;
        public string rememberedBySession;
        public string rememberedByCookie;
        public string rememberedByFormSession;
        public string rememberedByFormCookie;

        protected void Page_Load(object sender, EventArgs e)
        {
            System.Diagnostics.Debug.WriteLine("New Run");



            String action = Request["action"];
            String parameter = Request.QueryString["parameter"];

            switch (action)
            {
                case "refresh":

                    break;
                case "tryToRemember":
                    System.Diagnostics.Debug.WriteLine("remembering param " + parameter);
                    rememberedByRequest = parameter;
                    break;

                case "rememberInSession":
                    Session["sessionParam"] = parameter;
                    
                    break;

                case "deleteFromSession":
                    Session["sessionParam"] = null;
                    break;

                case "rememberWithCookie":
                    var myCookie = new HttpCookie("MyCookie");
                    myCookie.Values.Add("parameterToRemember", parameter);
                
                    myCookie.Expires = DateTime.Now.AddDays(100);

                    Response.Cookies.Add(myCookie);
                    break;

                case "forgetWithCookie":

                    if (Response.Cookies["MyCookie"] != null)
                    {
                        Response.Cookies["MyCookie"].Expires = DateTime.Now.AddDays(-1000);
                    }                               
                    break;

                case "form":
                    String type = Request.Form["type"];
                    String name = Request.Form["name"];

                    switch(type)
                    {
                        case "session":
                            Session["sessionFormParam"] = name;
                            break;

                        case "cookie":

                     var cookie = new HttpCookie("MyCookie");
                         cookie.Values.Add("parameterToRememberForm", name);
                
                         cookie.Expires = DateTime.Now.AddDays(100);
    
                    Response.Cookies.Add(cookie);
                    break;
                    }

                    break;
            }

            rememberedBySession = (string)Session["sessionParam"];
            rememberedByFormSession = (string)Session["sessionFormParam"];


            rememberedByCookie = (string)Request.Cookies["MyCookie"]?.Values["parameterToRemember"];
            rememberedByFormCookie = (string)Request.Cookies["MyCookie"]?.Values["parameterToRememberForm"];
        }
    }
}