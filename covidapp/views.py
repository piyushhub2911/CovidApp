from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "c11e37766amshec2677cc21bbd65p16f04ejsn2b39e3b52521",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloview(request):
    
    mylist = []
    noofresults = int(response['results'])
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method=="POST":
      selectedcountry= request.POST['selectedcountry']
      noofresults = int(response['results'])
      for x in range(0,noofresults):
        
          if selectedcountry==response['response'][x]['country']:
              new = response['response'][x]['cases']['new']
              active= response['response'][x]['cases']['active']
              critical= response['response'][x]['cases']['critical']
              recovered= response['response'][x]['cases']['recovered']
              total= response['response'][x]['cases']['total']
              deaths= int(total)-int(active)-int(recovered)
      context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}      
      return render(request,'helloview.html',context)
    
    
    context={'mylist': mylist}
    return render(request,'helloview.html',context)
