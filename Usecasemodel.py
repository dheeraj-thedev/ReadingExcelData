class UseCaseModel(object):
    def __init__(self,TestCaseId,Module,CarId,RecordingId,Steeringwheel,TripParts,Interior,TestPerformedby,OccupiedSeats,TestcaseDescription,ObjectId,Evaluation,DATfile,FalseTriggers,Result):
        self.TestCaseId = TestCaseId
        self.Module = Module
        self.CarId = CarId
        self.RecordingId = RecordingId
        self.Steeringwheel = Steeringwheel
        self.TripParts = TripParts
        self.Interior = Interior
        self.TestPerformedby = TestPerformedby
        self.OccupiedSeats = OccupiedSeats
        self.TestcaseDescription = TestcaseDescription
        self.ObjectId = ObjectId
        self.Evaluation = Evaluation
        self.DATfile = DATfile
        self.FalseTriggers = FalseTriggers
        self.Result = Result

    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(self.TestCaseId,self.Module,self.CarId,self.RecordingId,self.Steeringwheel,self.TripParts,self.Interior,self.TestPerformedby,self.OccupiedSeats,self.TestcaseDescription,self.ObjectId,self.Evaluation,self.DATfile,self.FalseTriggers,self.Result)

