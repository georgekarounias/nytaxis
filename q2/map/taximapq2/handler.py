# from turtle import distance
# from minio import Minio
# import socket

# def SetMC():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     ipaddress = s.getsockname()[0]
#     s.close()
#     mc = Minio(f"{ipaddress}:9000",
#         access_key='minioadmin',
#         secret_key='minioadmin',
#         secure=False)
#     return mc

# def GetTrips(req):
#     return

# def WriteToBucket(trips):
#     return

# def CalcDistance(trip):
#     return

# def GetTripDuration(trip):
#     return

# def GetPassengers(trip):
#     return

# def DoesTripMeetingRequirements(distance, duration, passengers):
#     return

def handle(req):
    print("Mapper Q2")
    # trips = GetTrips(req)
    # tripsMettingReqs = []
    # for trip in trips:
    #     distance = CalcDistance(trip)
    #     duration = GetTripDuration(trip)
    #     passengers = GetPassengers(trip)
    #     doesTripMeetingRequirements = DoesTripMeetingRequirements(distance, duration, passengers)
    #     if(doesTripMeetingRequirements == True):
    #         tripsMettingReqs.append(trip)
    # WriteToBucket(trips) 
    return req
