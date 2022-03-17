from mrjob.protocol import JSONValueProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class Q1MR(MRJob):
  def configure_args(self):
    super(Q1MR, self).configure_args()
  #   self.files("<data.json")
  #   #self.add_file_arg("<data.json")
  #   # self.add_passthru_arg("<data.json")

  def steps(self):
    return[
      MRStep(mapper=self.mapper, reducer=self.reducer)
    ]

  #Mapper function 
  def mapper(self, key, jsonArray):
    dataArray = json.loads(jsonArray)
    for rec in dataArray:
      yield rec['id'], 1

  #Reducer function
  def reducer(self, id, rec):
    yield id, sum(rec)

if __name__ == "__main__":
    Q1MR.run()