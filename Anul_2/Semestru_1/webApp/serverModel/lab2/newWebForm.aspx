<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="newWebForm.aspx.cs" Inherits="lab2.newWebForm" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <h3> Works! </h3>
    <a href="newWebForm.aspx"> Refresh </a> <br/>
    <a href="newWebForm.aspx?action=tryToRemember&parameter=meMario"> Try to remember action param </a> <br/>
    <a href="newWebForm.aspx?action=rememberInSession&parameter=meMarioSession"> Try to remember action param with session </a> <br/>
    <a href="newWebForm.aspx?action=deleteFromSession"> Delete from session </a> <br/>
    <a href="newWebForm.aspx?action=rememberWithCookie&parameter=meMarioCookie"><input type="button" value="Try to remember action param with cookie"/> </a> <br/>
    <a href="newWebForm.aspx?action=forgetWithCookie&parameter=meMarioCookie"><input type="button" value="Try to forget action param from cookie"/> </a> <br/>

    <br/><br/>

    <form action="newWebForm.aspx" method="post">

        <label> My name is:  </label>
        <input type="text" name="name" />
        <br />
        <input type="submit" value="Handle via session"/>
        <input type="hidden" name="type" value="session" />
        <input type="hidden" name="action" value="form" />
    </form>


        <br/><br/>

    <form action="newWebForm.aspx" method="post">

        <label> My name is still:  </label>
        <input type="text" name="name" />
        <br />
        <input type="submit" value="Handle via cookie"/>
        <input type="hidden"name="type" value="cookie" />
        <input type="hidden" name="action" value="form" />
    </form>




    <% if (rememberedByRequest != null)
        { %>
        
            <br/>
    <h3> Remembered by request: <%=rememberedByRequest %></h3>


    <% } %>


        <% if (rememberedBySession != null)
        { %>
        
            <br/>
    <h3> Remembered by session: <%=rememberedBySession %></h3>


    <% } %>


            <% if (rememberedByCookie != null)
        { %>
        
            <br/>
    <h3> Remembered by cookie: <%=rememberedByCookie %></h3>


    <% } %>




            <% if (rememberedByFormSession != null)
        { %>
        
            <br/>
    <h3> Remembered by form session: <%=rememberedByFormSession %></h3>


    <% } %>


            <% if (rememberedByFormCookie != null)
        { %>
        
            <br/>
    <h3> Remembered by form cookie: <%=rememberedByFormCookie %></h3>


    <% } %>


</body>
</html>
