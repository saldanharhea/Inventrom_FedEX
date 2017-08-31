import requests
import json
from pprint import pprint

tracking_number = raw_input("Enter fedex order number: ")



data = requests.post('https://www.fedex.com/trackingCal/track', data={
    'data': json.dumps({
        'TrackPackagesRequest': {
            'appType': 'wtrk',
            'uniqueKey': '',
            'processingParameters': {
                'anonymousTransaction': True,
                'clientId': 'WTRK',
                'returnDetailedErrors': True,
                'returnLocalizedDateTime': False
            },
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': tracking_number,
                    'trackingQualifier': '',
                    'trackingCarrier': ''
                }
            }]
        }
    }),
    'action': 'trackpackages',
    'locale': 'en_US',
    'format': 'json',
    'version': 99
}).json()
scheduled_delivery =data["TrackPackagesResponse"]["packageList"][0]["displayActDeliveryDateTime"]
ship_date =data["TrackPackagesResponse"]["packageList"][0]["displayPickupDt"]
check =data["TrackPackagesResponse"]["packageList"][0]["isInFedExPossession"]



#jas = json.dumps(data["TrackPackagesResponse"]["res"])
#res = data["TrackPackagesResponse"]["packageList"]["CDOExists"]
#print pprint(res)es"

#pprint(data)
#print tracking_number

#print ship_date # ship date


if check is False:
	status = "Delivered"
	
else:
	status ="In Transit"

#print status
#print scheduled_delivery  # scheduled dilivery

result = {'tracking no': tracking_number, 'ship date': ship_date,'status': status, 'scheduled delivery': scheduled_delivery}


#my_data = json.dumps()


#json_data = json.dumps(my_data)

print json.dumps(result, sort_keys=True, indent=2, separators=(',', ': '))
