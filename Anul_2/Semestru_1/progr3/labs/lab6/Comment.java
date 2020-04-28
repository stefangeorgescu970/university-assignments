
public class Comment {
	
	private Integer postId;
	private Integer id;
	private String name;
	private String email;
	private String body;
	
	public Comment(Integer postId, Integer id, String name, String email, String body){
		this.postId = postId;
		this.id = id;
		this.name = name;
		this.email = email;
		this.body = body;
	}
	
	public String toString(){
		return "Author: " + this.email + "\n" + "Comment:" + this.body + "\n\n";
	}
	
	
	public Boolean doesEmailMatch(String toMatch){
		return this.email.endsWith(toMatch);
	}
}
