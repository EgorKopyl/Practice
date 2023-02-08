import pygsheets
from pygsheets.client import Client
from typing import List, Union

class GoogleTable:
    def __init__(
        self, credence_service_file: str = "", googlesheet_file_url: str = ""
    ) -> None:
        self.credence_service_file: str = credence_service_file
        self.googlesheet_file_url: str = googlesheet_file_url

    def _get_googlesheet_by_url(
        self, googlesheet_client: pygsheets.client.Client
    ) -> pygsheets.Spreadsheet:
        """Get Google.Docs Table sheet by document url"""
        sheets: pygsheets.Spreadsheet = googlesheet_client.open_by_url(
            self.googlesheet_file_url
        )
        return sheets.sheet1

    def _get_googlesheet_client(self) -> Client:
        """It is authorized using the service key and returns the Google Docs client object"""
        return pygsheets.authorize(
            service_file=self.credence_service_file
        )

    def search_abonement(
        self,
        data: List[List[Union[str, bool]]],
        search_col: int = 1,
        firstlesson_col: int = 2,
        secondlesson_col: int = 3,
        thirdlesson_col: int = 4,
        forlesson_col: int = 5,
        fivelesson_col: int = 6,
        sixlesson_col: int = 7,
    ) -> int:
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(data, matchEntireCell=True, cols=(search_col, search_col))[0]
        except:
            return -1
        find_cell_row = find_cell.row
        firstlesson = wks.get_value((find_cell_row, firstlesson_col))
        secondlesson = wks.get_value((find_cell_row, secondlesson_col))
        thirdlesson = wks.get_value((find_cell_row, thirdlesson_col))
        forlesson = wks.get_value((find_cell_row, forlesson_col))
        fivelesson = wks.get_value((find_cell_row, fivelesson_col))
        sixlesson = wks.get_value((find_cell_row,sixlesson_col))
        return [firstlesson,secondlesson, thirdlesson,forlesson,fivelesson,sixlesson]