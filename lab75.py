def create_youtube_video(title, description):
	new_video={"title":title, "description":description, "likes":0, "dislikes":0, "comments": {}}
	return new_video
def like(new_video):
		if "likes" in new_video:
			new_video["likes"]+=1
			return new_video
def dislike(new_video):
	if "dislikes" in new_video:
		new_video["dislikes"]+=1
		return new_video
def add_comment(youtube_video,username,comment):
	new_video['comments']["username"] = comment
	return comments
video=create_youtube_video("wow its my first day","i will take with me to the first day of MEET :)")





