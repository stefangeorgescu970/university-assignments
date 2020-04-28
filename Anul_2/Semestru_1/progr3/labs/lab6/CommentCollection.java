
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class CommentCollection {
	
	private List<Comment> myComments = new ArrayList<Comment>();
	
	public CommentCollection(String fileName){
		 JSONParser parser = new JSONParser();
	        try
	        {
	            Object object = parser.parse(new FileReader(fileName));
	            

	            JSONArray comments = (JSONArray)object; 
	           
	            
	            for(Object comment : comments)
	            {
	            	JSONObject currentComment = (JSONObject)comment;
	            	Integer postId = ((Long)currentComment.get("postId")).intValue();
	            	Integer id = ((Long)currentComment.get("id")).intValue();
	            	String name = (String) currentComment.get("name");
	            	String email = (String) currentComment.get("email");
	            	String body = (String) currentComment.get("body");
	            	Comment gotComment = new Comment(postId, id, name, email, body);
	            	this.myComments.add(gotComment);
	            }
	        }
	        catch(FileNotFoundException fe)
	        {
	            fe.printStackTrace();
	        }
	        catch(Exception e)
	        {
	            e.printStackTrace();
	        }
	}
	
	public void printElements(String toMatch){
		for(Comment com : this.myComments) {
			if (com.doesEmailMatch(toMatch)){
				System.out.println(com);
			}
		}
	}
	
}
