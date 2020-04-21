from com.modals.sheetmodals import UseCaseModel
from com.utils.ExcelLoader import LoadExcelUtil
from com.sql.SQLdatabase import MySQLUtils

mainExcel = "OMS_UseCase_GoldenVideosRegression_Testing_Report_Min_R9.3.4.0-M_15Nov_session2.xlsx"


def get_use_case_details(sheet_ref):
    wb = LoadExcelUtil(mainExcel).get_workbook_instance()
    sheet_names = wb.sheet_names()
    ctr = 0
    for sheet_name in sheet_names:
        if sheet_name == sheet_ref:
            return wb.sheets()[ctr]
        ctr = ctr + 1


def grid_landing_sheet(filename):
    wb = LoadExcelUtil(mainExcel).get_workbook_instance()
    sheet_landing = wb.sheets()[1]
    rows = []
    for row_number in range(sheet_landing.nrows):
        no = sheet_landing.cell(row_number, 1).value  # [row_number][1]
        oms_use_case = sheet_landing.cell(row_number, 2).value
        total_use_case_count = sheet_landing.cell(row_number, 3).value
        if no != "" and type(total_use_case_count) != str:
            if int(total_use_case_count) >= 0:
                rows.append([no, oms_use_case, total_use_case_count])
    return rows


def get_use_case_mode(row_number, sheet_reference):
    use_case_model = UseCaseModel(
        TestCaseId=sheet_reference.cell(row_number, 0).value,
        Module=sheet_reference.cell(row_number, 1).value,
        CarId=sheet_reference.cell(row_number, 2).value,
        RecordingId=int(sheet_reference.cell(row_number, 3).value),
        Steeringwheel=sheet_reference.cell(row_number, 4).value,
        TripParts=sheet_reference.cell(row_number, 5).value,
        Interior=sheet_reference.cell(row_number, 6).value,
        TestPerformedby=sheet_reference.cell(row_number, 7).value,
        OccupiedSeats=sheet_reference.cell(row_number, 8).value,
        TestcaseDescription=sheet_reference.cell(row_number, 9).value,
        ObjectId=sheet_reference.cell(row_number, 10).value,
        Evaluation=sheet_reference.cell(row_number, 11).value,
        DATfile=sheet_reference.cell(row_number, 12).value,
        FalseTriggers=sheet_reference.cell(row_number, 13).value,
        Result=sheet_reference.cell(row_number, 14).value)
    return use_case_model


if __name__ == '__main__':
    object = []
    excel_sheet = grid_landing_sheet(
        'OMS_UseCase_GoldenVideosRegression_Testing_Report_Min_R9.3.4.0-M_15Nov_session2.xlsx')
    namesOfWorkBook = [workbook for workbook in excel_sheet if workbook[2] > 0]
    names = [book[0] + "_" + book[1] for book in namesOfWorkBook]
    for name in names:
        sheet = get_use_case_details(name)
        if sheet is not None:
            for row in range(2, sheet.nrows):
                object.append(get_use_case_mode(row, sheet))
    utils = MySQLUtils()
    for row in object:
        sheet_uc_9 = get_use_case_details(name)
        if sheet_uc_9 is not None:
            for row in range(2, sheet_uc_9.nrows):
                for col in range(2, sheet_uc_9.ncols):
                    print(sheet_uc_9.cell(row, col).value, end='|')
                print()

#       utils.saveData(row)
