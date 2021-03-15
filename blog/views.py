from django.shortcuts import render,redirect
from pytube import YouTube
from django.http import FileResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def getdetails(request):
	if(request.method=='POST'):
		try:
			link = request.POST['link']
			yt = YouTube(link)
			image = yt.thumbnail_url
			title = yt.title
			views_count = yt.views
			streams = yt.streams
			available_streams = streams.filter(progressive = True)
			print("Got streams")
			quality=[]
			for i in available_streams:
				quality.append(i.resolution)
			print(quality)
			context = {'link':link,'title':title,'views_count':views_count,'quality':quality,'image_url':image}
			return render(request,'blog/got.html',{'context':context})
			# return render(request,"blog.index.html")
		except:
			return redirect('/')
def download(request):
	if request.method=='POST':
		quality = request.POST['quality']
		link = request.POST['link']
		yt = YouTube(link)
		streams = yt.streams

		available_streams = streams.filter(progressive = True)
		messages.success(request,"Downloading FileResponse")
		if(quality=='360p'):
			vid = available_streams.filter(resolution = '360p')
			return FileResponse(open(vid[0].download(),'rb'),as_attachment = True)
		elif(quality=='720p'):
			vid = streams.get_highest_resolution()
			return FileResponse(open(vid.download(),'rb'),as_attachment = True)
	else:
		return redirect('/')

