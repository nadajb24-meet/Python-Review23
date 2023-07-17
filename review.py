def create_youtube_video(title,description):
	youtube_video = {"title" : title,"description" : description,"likes" :0,"dislikes":0,'comments':{'username':userame}}
	return youtube_video

def like(video):
	if likes in video:
		video['likes']+=1

def dislike(video):
	if dislikes in video:
		video['dislikes']+=1


def add_comment(youtubevideo,username,comment_text):
	video["comment"][username]=comment_text
	return video

nada=create_youtube_video('beach', 'love love love')
print(nada)
like(nada)
dislike(nada)
add_comment(nada,'nada','we love the beach')
print(nada)
for i in range(495):
	like(nada)
print(nada)
