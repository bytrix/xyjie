from django.shortcuts import render_to_response
def test(req, x, y, z):
	return render_to_response('test.html',{'name':x, 'age':y, 'job':z})

def index(req):
	return render_to_response('index.html')
