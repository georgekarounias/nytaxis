from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

def GetData():
    data = [
  {
    "id": "id2875421",
    "vendor_id": 2,
    "pickup_datetime": "2016-03-14 17:24:55",
    "dropoff_datetime": "2016-03-14 17:32:30",
    "passenger_count": 1,
    "pickup_longitude": -73.9821548461914,
    "pickup_latitude": 40.76793670654297,
    "dropoff_longitude": -73.96463012695312,
    "dropoff_latitude": 40.765602111816406,
    "store_and_fwd_flag": "N",
    "trip_duration": 455
  },
  {
    "id": "id2377394",
    "vendor_id": 1,
    "pickup_datetime": "2016-06-12 00:43:35",
    "dropoff_datetime": "2016-06-12 00:54:38",
    "passenger_count": 1,
    "pickup_longitude": -73.98041534423828,
    "pickup_latitude": 40.738563537597656,
    "dropoff_longitude": -73.99948120117188,
    "dropoff_latitude": 40.73115158081055,
    "store_and_fwd_flag": "N",
    "trip_duration": 663
  },
  {
    "id": "id3858529",
    "vendor_id": 2,
    "pickup_datetime": "2016-01-19 11:35:24",
    "dropoff_datetime": "2016-01-19 12:10:48",
    "passenger_count": 1,
    "pickup_longitude": -73.9790267944336,
    "pickup_latitude": 40.763938903808594,
    "dropoff_longitude": -74.00533294677734,
    "dropoff_latitude": 40.710086822509766,
    "store_and_fwd_flag": "N",
    "trip_duration": 2124
  },
  {
    "id": "id3504673",
    "vendor_id": 2,
    "pickup_datetime": "2016-04-06 19:32:31",
    "dropoff_datetime": "2016-04-06 19:39:40",
    "passenger_count": 1,
    "pickup_longitude": -74.01004028320312,
    "pickup_latitude": 40.719970703125,
    "dropoff_longitude": -74.01226806640625,
    "dropoff_latitude": 40.70671844482422,
    "store_and_fwd_flag": "N",
    "trip_duration": 429
  },
  {
    "id": "id2181028",
    "vendor_id": 2,
    "pickup_datetime": "2016-03-26 13:30:55",
    "dropoff_datetime": "2016-03-26 13:38:10",
    "passenger_count": 1,
    "pickup_longitude": -73.97305297851562,
    "pickup_latitude": 40.793209075927734,
    "dropoff_longitude": -73.9729232788086,
    "dropoff_latitude": 40.78252029418945,
    "store_and_fwd_flag": "N",
    "trip_duration": 435
  },
  {
    "id": "id0801584",
    "vendor_id": 2,
    "pickup_datetime": "2016-01-30 22:01:40",
    "dropoff_datetime": "2016-01-30 22:09:03",
    "passenger_count": 6,
    "pickup_longitude": -73.98285675048828,
    "pickup_latitude": 40.74219512939453,
    "dropoff_longitude": -73.99208068847656,
    "dropoff_latitude": 40.749183654785156,
    "store_and_fwd_flag": "N",
    "trip_duration": 443
  },
  {
    "id": "id1813257",
    "vendor_id": 1,
    "pickup_datetime": "2016-06-17 22:34:59",
    "dropoff_datetime": "2016-06-17 22:40:40",
    "passenger_count": 4,
    "pickup_longitude": -73.9690170288086,
    "pickup_latitude": 40.75783920288086,
    "dropoff_longitude": -73.95740509033203,
    "dropoff_latitude": 40.76589584350586,
    "store_and_fwd_flag": "N",
    "trip_duration": 341
  },
  {
    "id": "id1324603",
    "vendor_id": 2,
    "pickup_datetime": "2016-05-21 07:54:58",
    "dropoff_datetime": "2016-05-21 08:20:49",
    "passenger_count": 1,
    "pickup_longitude": -73.96927642822266,
    "pickup_latitude": 40.79777908325195,
    "dropoff_longitude": -73.92247009277344,
    "dropoff_latitude": 40.76055908203125,
    "store_and_fwd_flag": "N",
    "trip_duration": 1551
  },
  {
    "id": "id1301050",
    "vendor_id": 1,
    "pickup_datetime": "2016-05-27 23:12:23",
    "dropoff_datetime": "2016-05-27 23:16:38",
    "passenger_count": 1,
    "pickup_longitude": -73.99948120117188,
    "pickup_latitude": 40.738399505615234,
    "dropoff_longitude": -73.98578643798828,
    "dropoff_latitude": 40.73281478881836,
    "store_and_fwd_flag": "N",
    "trip_duration": 255
  },
  {
    "id": "id0012891",
    "vendor_id": 2,
    "pickup_datetime": "2016-03-10 21:45:01",
    "dropoff_datetime": "2016-03-10 22:05:26",
    "passenger_count": 1,
    "pickup_longitude": -73.98104858398438,
    "pickup_latitude": 40.74433898925781,
    "dropoff_longitude": -73.9729995727539,
    "dropoff_latitude": 40.78998947143555,
    "store_and_fwd_flag": "N",
    "trip_duration": 1225
  },
  {
    "id": "id1436371",
    "vendor_id": 2,
    "pickup_datetime": "2016-05-10 22:08:41",
    "dropoff_datetime": "2016-05-10 22:29:55",
    "passenger_count": 1,
    "pickup_longitude": -73.98265075683594,
    "pickup_latitude": 40.76383972167969,
    "dropoff_longitude": -74.00222778320312,
    "dropoff_latitude": 40.73299026489258,
    "store_and_fwd_flag": "N",
    "trip_duration": 1274
  },
  {
    "id": "id1299289",
    "vendor_id": 2,
    "pickup_datetime": "2016-05-15 11:16:11",
    "dropoff_datetime": "2016-05-15 11:34:59",
    "passenger_count": 4,
    "pickup_longitude": -73.99153137207031,
    "pickup_latitude": 40.74943923950195,
    "dropoff_longitude": -73.95654296875,
    "dropoff_latitude": 40.7706298828125,
    "store_and_fwd_flag": "N",
    "trip_duration": 1128
  }
]
    return data

###############
class Q1MR(MRJob):
  def steps(self):
    return[
      MRStep(mapper=self.mapper, reducer=self.reducer)
    ]

  #Mapper function 
  def mapper(self, _, line):
    print("This is mapper")

  #Reducer function
  def reducer(self, key, values):
    print("This is reducer")
############



def handle(req):
  data = GetData()
  Q1MR.run()
  return req
