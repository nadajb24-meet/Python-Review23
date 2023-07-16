def create_youtube_video(title,description):
	youtube_video = {"title" : title,"description" : description,"likes" :0,"dislikes":0,'comments':{}}
	return youtube_video

def like(video):
	if likes in video:
		likes+=1

def dislike(video):
	if dislikes in video:
		dislikes+=1


def add_comment(youtubevideo,username,comment_text):
	video["comment"][username]=comment_text
	return video