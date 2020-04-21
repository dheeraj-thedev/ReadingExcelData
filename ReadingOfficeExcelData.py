from xlrd import open_workbook
from Usecasemodel import UseCaseModel
from SQLdatabase import MySQLUtils

class Excel(object):
    def __init__(self, No, OMSUseCase, TotalUsecaseCount, UsecasePass, UsecaseFail, FalseTriggerTestcasesCount,
                 FalseTriggerPassCount, FalseTriggerFailcount, TotalTestcase, TotalPass, TotalFail):
        self.No = No
        self.OMSUseCase = OMSUseCase
        self.TotalUsecaseCount = TotalUsecaseCount
        self.UsecasePass = UsecasePass
        self.UsecaseFail = UsecaseFail
        self.FalseTriggerTestcasesCount = FalseTriggerTestcasesCount
        self.FalseTriggerPassCount = FalseTriggerPassCount
        self.FalseTriggerFailcount = FalseTriggerFailcount
        self.TotalTestcase = TotalTestcase
        self.TotalPass = TotalPass
        self.TotalFail = TotalFail
    @property
    def __str__(self):
        return ("Excel object:\n"
                "No = {0}\n"
                "OMSUseCase = {1}\n"
                "TotalUsecaseCount = {2}\n"
                "UsecasePass = {3}\n"
                "UsecaseFail = {4}\n"
                "FalseTriggerTestcasesCount = {5}\n"
                "FalseTrigger(PassCount) = {6}\n"
                "FalseTrigger(FailCount) = {7}\n"
                "TotalTestcase = {8}\n"
                "TotalPass = {9}\n"
                "TotalFail = {10}\n"
                .format(self.No, self.OMSUseCase,
                        self.TotalUsecaseCount,
                        self.UsecasePass,
                        self.UsecaseFail,
                        self.FalseTriggerTestcasesCount,
                        self.FalseTriggerPassCount,
                        self.FalseTriggerFailcount,
                        self.TotalTestcase,
                        self.TotalPass,
                        self.TotalFail))
wb = open_workbook("OMS_UseCase_GoldenVideosRegression_Testing_Report_Min_R9.3.4.0-M_15Nov_session2.xlsx")
def getUCDetails(sheetref):
    sheetNames = wb.sheet_names()
    ctr = 0
    for shName in sheetNames:
        if shName == sheetref:
            return wb.sheets()[ctr]
        ctr = ctr + 1
def excel_to_listoflist2(filename):
    sheet = wb.sheets()[1]
    rows = []
    for row in range(sheet.nrows):
        no = sheet.cell(row, 1).value  # [row][1]
        omsUseCase = sheet.cell(row, 2).value
        totalUseCaseCount = sheet.cell(row, 3).value
        if no != "" and type(totalUseCaseCount) != str:
            if int(totalUseCaseCount) >= 0:
                rows.append([no, omsUseCase, totalUseCaseCount])
    return rows
def excel_to_listoflist(filename):
    wb = open_workbook(filename)
    sheet = wb.sheets()[1]
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    # Reading UseCaseSummary sheet
    for row in range(number_of_rows):
        no = sheet.cell(row, 1)  # [row][1]
        omsUseCase = sheet.cell(row, 2)
        totalUseCaseCount = sheet.cell(row, 3)
        validlines = []
        # If string is found in the rows, it should throw error for that i am using Exceptions
        try:
            totalUseCaseCount = float(totalUseCaseCount.value)
            if totalUseCaseCount > 0:
                # Total usecase count is non zero click and open corresponding sheet which has the data
                myName = "{}_{}".format(no.value, str(omsUseCase.value).replace(" ", "_"))
                sheetNames = wb.sheet_names()
                ctr = 0
                for shName in sheetNames:
                    if shName == myName:
                        lsheet = wb.sheets()[ctr]
                        number_of_rowsl = lsheet.nrows
                        number_of_columnsl = lsheet.ncols
                        # Read the data which has in sheet
                        for rowl in range(0, number_of_rowsl):
                            columns = []
                            for coll in range(1, number_of_columnsl):
                                localCol = wb.sheets()[ctr].cell(rowl, coll).value
                                if localCol != '':
                                    # print(wb.sheets()[ctr].cell(rowl,coll).value)
                                    columns.append(wb.sheets()[ctr].cell(rowl, coll).value)
                            if len(columns) == 14:
                                validlines.append(columns)
                    ctr = ctr + 1
        except (Exception) as e:
            if type(e) is float:
                pass
    return validlines
def getUseCaseMode(row,uscSheet):
    excelObject = UseCaseModel(
        TestCaseId=uscSheet.cell(row, 0).value,
        Module=uscSheet.cell(row, 1).value,
        CarId=uscSheet.cell(row, 2).value,
        RecordingId=int(uscSheet.cell(row, 3).value),
        Steeringwheel=uscSheet.cell(row, 4).value,
        TripParts=uscSheet.cell(row, 5).value,
        Interior=uscSheet.cell(row, 6).value,
        TestPerformedby=uscSheet.cell(row, 7).value,
        OccupiedSeats=uscSheet.cell(row, 8).value,
        TestcaseDescription=uscSheet.cell(row, 9).value,
        ObjectId=uscSheet.cell(row, 10).value,
        Evaluation=uscSheet.cell(row, 11).value,
        DATfile=uscSheet.cell(row, 12).value,
        FalseTriggers=uscSheet.cell(row, 13).value,
        Result=uscSheet.cell(row, 14).value)
    return excelObject
if __name__ == '__main__':
    object=[]
    excel_sheet = excel_to_listoflist2('OMS_UseCase_GoldenVideosRegression_Testing_Report_Min_R9.3.4.0-M_15Nov_session2.xlsx')
    namesOfWorkBook =[workbook for workbook in excel_sheet if workbook[2]>0]
    names=[book[0]+"_"+book[1] for book in namesOfWorkBook]
    for name in names:
        sheet=getUCDetails(name)
        if sheet is not None:
            for row in range(2,sheet.nrows):
                object.append(getUseCaseMode(row,sheet))
    utils = MySQLUtils()
    for row in object:
        utils.saveData(row)

