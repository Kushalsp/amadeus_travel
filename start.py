from amadeus import Client, ResponseError
import credential

amadeus = Client(
    client_id= credential.secret["key"],
    client_secret= credential.secret["secret"]
)

try:
    response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
    print(response.data)
except ResponseError as error:
    print(error)